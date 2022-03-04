#!/usr/bin/python

import argparse
import os
import sys
import logging
import traceback


def parse_row(row, mwidths):
    n = 1
    rows = []
    for i,s in enumerate(row):
        if len(s) > mwidths[i]: 
            s = multirows(s, mwidths[i])
        else:
            s = [s]
        rows.append(s)
        n = max(n, len(s))
    logger.debug(rows)
    return n, rows

# split row into several multirows to fit a specified width            
def multirows(s, width):
    rows = []
    split_chars = [' ', '.', ',', ':', '-', '_', '\/', '=']
    indexes = []
    for split_char in split_chars:
        indexes.append(s[:width].rfind(split_char))
    midx = -1
    for i, idx in enumerate(indexes):
        if idx > midx:
            midx = idx
            split_char = split_chars[i]
    if midx == -1:
        logger.warning('Cannot split substring: {}'.format(s))
        return [s]
    s1 = s[:midx] if split_char == ' ' or split_char == '_' else s[:midx+len(split_char)]
    if split_char == '_':
        s1 += '\_' 
    rows.append(s1)
    for i in range(midx+len(split_char), len(s)):
        if s[i] != ' ':
            s = s[i:]
            break
    if len(s) > width:
        rows.extend(multirows(s, width))
    else:
        rows.append(s)
    return rows

 
def gen_rst_table(table, width=None, widths=None, fixed_width= False, title=None, headers=None, multilines=False):
    
    s = ['.. table:: ']
    if (title):
        s.append(title)
    s.append('\n')
    if width is not None:
        s.append(' :width: {} \n'.format(width))
    if widths is not None:
        s.append(' :widths: {} \n'.format(widths))
    s.append(' :class: tight-table\n\n')
    
    if headers is not None:
        h_lines = headers[0]
        headers = headers[1:][0]
        
    if not fixed_width:
    # find the column widths depending on the content
        cols = len(table[0][1])
        twidths = [0]*cols
        if headers is not None:
            for c, h in enumerate(headers):
                for line in h:
                    twidths[c] = max(twidths[c], len(line))
        for r,row in enumerate(table):
            for c, col in enumerate(row[1]):
                for line in col:
                    twidths[c] = max(twidths[c], len(line))
        logger.debug('twidths: {}'.format(twidths))
    else:
        twidths = [width*int(w.strip())/100-1 for w in widths.split(' ')]
    
    if headers is not None:
        s.append(' +')
        for w in twidths:
            s.extend(['-']*w)
            s.append('+')
        s.append('\n')
        for m in range(h_lines):
            s.append(' ')
            for c, h in enumerate(headers):
                line = h[m] if len(h) > m else ''
                s.append('|')
                s.append(line)
                add_chars = twidths[c] - len(line)
                if add_chars>0:
                    s.extend([' ']*add_chars)
            s.append('|')
            s.append('\n')
            if multilines:
                # insert an additional line
                if h_lines>1 and m<h_lines-1:
                    s.append(' |')
                    for w in twidths:
                        s.extend([' ']*w)
                        s.append('|')
                    s.append('\n')
        s.append(' +')
        for w in twidths:
            s.extend(['=']*w)
            s.append('+')
        s.append('\n')
        
    for r,row in enumerate(table):
        r_lines = row[0]
        for m in range(r_lines):
            s.append(' ')
            for c, r in enumerate(row[1]):
                line = r[m] if len(r) > m else ''
                s.append('|')
                s.append(line)
                add_chars = twidths[c] - len(line)
                if add_chars>0:
                    s.extend([' ']*add_chars)
            s.append('|')
            s.append('\n')
            if multilines:
                # insert an additional line
                if r_lines>1 and m<r_lines-1:
                    s.append(' |')
                    for w in twidths:
                        s.extend([' ']*w)
                        s.append('|')
                    s.append('\n')
        s.append(' +')
        for w in twidths:
            s.extend(['-']*w)
            s.append('+')
        s.append('\n')
    
    return(''.join(s))
            
                
            
                
        
COLUMN_WIDTHS = "25 15 15 45"
        
parser = argparse.ArgumentParser(description='Covert a text table list to the RST table.')
parser.add_argument('-i', dest='file', required=True, help='input file')
parser.add_argument('-l', dest='width', type=int, default=100, help='total table\'s width in characters')
parser.add_argument('-w', dest='widths',
                    help='Column header widths separated by spaces (in %)')
parser.add_argument('-t', dest='tab', action='store_true', default=False, help='if set a tabulator used a a separator (default=end of line)')
parser.add_argument('-f', dest='fixed_widths', action='store_true', default=False,
                    help='set fixed column widths (otherwise they will be calculated dynamically)')
parser.add_argument('-a', dest='add_headers', action='store_true', default=False,
                    help='add colums headers (either pre-defined or read from the input file)')
parser.add_argument('-r', dest='read_headers', action='store_true', default=False,
                    help='if column headers included in the input file')
parser.add_argument('-c', dest='headers', 
                    default="Property name,Type,Default value \/ mandatory,Description",
                    help='Pre-defined column headers separated by commas')
parser.add_argument('-m', dest='multilines', action='store_true', default=False, help='create a multiline table')
parser.add_argument('-d', dest='debug', action='store_true', default=False, help='debug program') 

args = parser.parse_args()

logging.basicConfig()
logger = logging.getLogger('table')
if args.debug:
    logger.setLevel(logging.DEBUG)



if not os.path.isfile(args.file):
    print("File path {} does not exist. Exiting...".format(args.file))
    sys.exit(1)

headers = None   


table = []
try:
    with open(args.file, 'r') as fin:
        lines = fin.readlines()
        i = 0
        if lines[i].startswith('.. table'):
            s = lines[i].strip().split('::')
            title = s[1].strip() if len(s)>1 else None
            i += 1
        else:
            title = ''
        logger.debug('Table title: {}'.format(title))
        if lines[i].strip().startswith(':width:'):
            width = int(lines[i].split(':')[2].strip())
            logger.debug('table width: {}'.format(width))
            i += 1
        else:
            width = args.width
        if lines[i].strip().startswith(':widths:'):
            widths = lines[i].split(':')[2].strip()
            logger.debug('Read widths from the file: {}'.format(widths.split(' ')))
            cwidths = [width*int(w)/100-1 for w in widths.split(' ')]
            cols = len(cwidths)
            i += 1
        else:
            # calculate the pre-defined column widths in characters
            widths = args.widths if args.widths else COLUMN_WIDTHS
            logger.debug('Set pre-defined widths: {}'.format(widths))
            cwidths = [width*int(w.strip())/100-1 for w in widths.split(' ')]
            cols = len(cwidths)
            
        logger.debug('header widths: {}'.format(cwidths))
        
        if args.add_headers:
            if not args.read_headers:
                for h in args.headers.split('\t'):
                    h = h.strip().replace('*', '\*').replace('/', '\/').\
                    replace('>', '\>').replace('<', '\<').replace('-', '\-')
                    headers = parse_row(h, cwidths)
                    logger.debug('headers: {}'.format(headers))
                    if len(headers) != cols:
                        print('ERROR: Invalid number of columns {} or headers {}'.format(cols, len(headers)))
                        sys.exit(1)
            
        if args.read_headers:
            logger.debug("Reading headers from the input file ...")
            row = []
            while lines[i].strip() == '':
                i += 1
            for h in lines[i].strip().split('\t'):
                h = h.strip().replace('*', '\*').replace('/', '\/').\
                replace('>', '\>').replace('<', '\<').replace('-', '\-')
                row.append(h)
            headers = parse_row(row, cwidths)
            logger.debug('headers: {}'.format(headers))
            i += 1
            while i<len(lines) and lines[i].strip() == '':
                logger.debug('#ignore line {}: {}'.format(i, line[i]))
                i += 1
    
        row = []
        n = 0
        logger.debug("Reading table ...")
        while i<len(lines):       
            while i<len(lines) and n < cols:
                line = lines[i].strip()
                line = line.replace('*', '\*').replace('/', '\/').\
                        replace('>', '\>').replace('<', '\<').replace('-', '\-')
                if not args.tab:
                    row.append(line)
                    i += 1
                    while i<len(lines) and lines[i].strip() == '':
                        i += 1
                    n += 1        
                else:
                    row = [s.strip() for s in line.split('\t')]
                    n = len(row)
                    i += 1
                    
                           
            table.append(parse_row(row, cwidths))
            row = []
            n = 0
    
    rst_table = gen_rst_table(table, width, widths, args.fixed_widths, title, headers, multilines=args.multilines)
    logger.debug('RST_TABLE:\n{}'.format(rst_table))

    outfile = os.path.splitext(args.file)[0]+".rest"
    print('\nWriting to the file {} ...'.format(outfile))
    with open(outfile, 'w') as fout:
        fout.write(rst_table)

    print('Finished!')
    

except Exception as e:
    print('ERROR: Cannot parse a table from the file {}: {}'.format(args.file, str(e)))
    print(traceback.format_exc())
    
            
