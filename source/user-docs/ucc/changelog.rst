.. _ucc-changelog:

Changelog
=========

Issue tracker: https://sourceforge.net/p/unicore/issues

Version 2.3.0 (released Dec 15, 2021)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - update to UNICORE 8.3 base libs
 - improvement: "run": paths for local files to upload are resolved
   relative to .u job file
 - improvement: "run": in async mode, write job ID file, but
   add "--quiet" option to allow switching this off
 - improvement: "run" and "workflow-submit" can now add tags
   on submission with "--tags tag1,tag2,..." option
 - fix: UFTP upload/download used obsolete single-file mode
 - fix: UFTP parameters not set
 - only allow a single preferred protocol (option -P, --protocol)
 - fix: setting user preference for group (-Z group:foo) did not
   have any effect
 - fix: "cp": use the transfer protocol specified in the remote URL
 - remove obsolete 'list-attributes' command
 - update bash completion

Version 2.2.1  (released Sep 27, 2021)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - improvement: 'rest' command accepts a list of URLs
 - fix: clearing the screen during password entry
   results in characters displayed in clear text (#290)
 - update to JLine 3.20

Version 2.2.0  (released Aug 04, 2021)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - update to UNICORE 8.2 base libs
 - fix: local imports were left in the job description,
   leading to job runtime erros
 - fix: UCC returns exit code 1 if job failed

Version 2.1.0  (released Feb 25, 2021)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - update to UNICORE 8.1 base libs
 - fix: '-K', '--acceptAllIssuers' option did not work as advertised
 - fix: debian package now depends on "default-jre-headless"
 - fix: setting "uid" preference with "-Z" had no effect
 - new feature: "$_" variable in shell mode containing the last URL
   that was accessed / created.
 - don't write job id/properties files (less clutter)

Version 2.0.2  (released Sep 10, 2020)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - updated workflow support to match workflow server
   release
 - shell: add '!' as an alias for 'system'
 - shell: improve command completion
 - fix: workflow list did not take tags into account

Version 2.0.1  (released May 19, 2020)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - add workflow submission and management
 - default authentication method is now
   username/password
 - remove UNICORE 7 SAML authentication which is no longer
   used with the REST API. Use username/password instead
 - fix: submitted job did not wait for client stage-in 
 
Version 2.0.0  (released Mar 17, 2020)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - update to UNICORE 8 base libs
 - commands ported to use the REST API
 - new feature: expand variables in ucc shell commands
 - new feature: "system" command in "ucc shell" allows
   to run external programs
 - update oidc-agent support to 3.x
 - fix: handle "=" in admin command parameter values
 - drop support for OGSA-BES
 - remove SAML-Push support (#248)
 - workflow system support temporarily not
   included in UCC (can use "ucc rest" if required)

Version 1.7.13 (released Apr 04, 2019)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - fix: update to work with Java 11 (#246)

Version 1.7.12 (released Sep 17, 2018)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - new feature: support for 'oidc-agent' (#227)
 - new feature: "cp": byte range support and recursive dir copy
 - fix: attempt to directly lookup server DNs when not found in
   the registry (#228)
 - remove obsolete get-file, put-file, copy-file (#189)
  

Version 1.7.11 (released Nov 15, 2017)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - new feature: resume mode for "cp" (client/server copy) (#187)
 - query user whether to accept unknown certificates (#42)
 - fix: protocol dependent settings ignored for server-server
   copy (#185)
 - show error info for failed workflows
 - minor documentation fixes
 

Version 1.7.10 (released April 11, 2017)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - remove "cip-query" command

Version 1.7.9 (released Oct 5, 2016)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - document admin commands (#110)
 - list-storages accepts list of storage URLs
 - fix: run: if "--sitename" is given, filter out non-matching sites
   as early as possible
 - fix: WSRF command should work without delegation 
 - fix: show compute budget in list-sites
 - default config uses truststore directory

Version 1.7.8 (released Dec 14, 2015)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - new feature: support workflow template with parameter values
   read from the .u file (https://sourceforge.net/p/unicore/issues/52)
 - new feature: "rename" command for renaming remote files
 - new feature: --dryRun option for workflow submission
 - new feature: --raw option for 'system-info' showing registry content
 - fix: create-sms hangs when specified site or type does not exist
   (https://sourceforge.net/p/unicore/issues/44)
 - fix: local import files uploaded multiple times

Version 1.7.7 (released July 16, 2015)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - improvement: interactively ask for myproxy username if not given
   (https://sourceforge.net/p/unicore/feature-requests/374)
 - improvement: 'job-status' can now show more details and the 
   job's log using the new "-l" and "-a" flags
 - fix: allow creating sweep jobs based on Arguments, Parameters, 
   Environment and Imports tags. Fix the documentation of the sweep 
   feature (https://sourceforge.net/p/unicore/bugs/809)
 - fix: Environment can now alternatively be specified in more
   intuitive NAME: "value" syntax
 - fix: print any error info for file up/download
 - fix: copy the default keystore to newly created ~/.ucc on windows
   (https://sourceforge.net/p/unicore/bugs/803)

Version 1.7.6 (released March 13, 2015)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - new feature: support for resource sharing via service ACLs
   (https://sourceforge.net/p/unicore/feature-requests/343)
 - new feature: allow to set "read-only" flag on imports
   (http://sourceforge.net/p/unicore/feature-requests/280)
 - fix: download-config can also configure Unity address and 
   Unity authentication mode (https://sourceforge.net/p/unicore/bugs/795)
 - fix: contact-registry flag did not work correctly with UCC BES commands
   (https://sourceforge.net/p/unicore/bugs/799)
 - fix: "cp" would not copy workflow files ("c9m:...")

Version 1.7.5 (released December 19, 2014)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - new feature: "exec" command (SF feature #347)
 - new feature: can use OIDC bearer token for authentication
   (authenticationMethod 'unity') (SF feature #344)
 - new feature: add way to read parameters for 'create-storage' 
   and 'create-tss' from file (SF feature #346)
   For example: 'ucc create-storage ... @s3.properties'
 - improvement: create-storage: add "-i" option to only show 
   info about available storage factories

Version 1.7.4 (released September 12, 2014)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - fix: parse error in jobs containing '#' (bug #757)
 - fix: issue-delegation with Unity (bug #749)
 - fix: "-D" option with Unity (bug #748)

Version 1.7.3 (released July 18, 2014)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - new feature: "cp" command for copying files
 - new feature: persistent history of "shell" sessions
 - fix: sitename in job description was ignored
   (SF bug #745)
 - fix: server-to-server copy ignored preferred 
   protocol

Version 1.7.2 (released June 13, 2014)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - fix: when calling UCC with no arguments, show
   help instead of exception
 - improvement: allow comments (via '#') in .u JSON files 
   and fix line numbers when reporting JSON errors
 - fix: specifiying trust delegation ('-D' option) had no
   effect (SF bug #737)
 - fix: connect-to-testgrid on Windows (SF bug #715)

Version 1.7.1 (released Feb 26, 2014)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - new feature: allow to choose whether user pre/post command
   is run on login node or on compute node (SF feature #312)
 - fix: nullpointer exception when using Unity (SF bug #689)
 - fix: job and groovy script samples were out of date (SF bug #695)
 - fix: using Unity did not work (SF bugs #689, #690)
 - fix: allow unescaped "!" characters when entering a password 
   on the console (SF bug #704)
 - fix: 'help-auth' did not work in shell mode
 - improvement: more readable help-auth output (SF bug #688)
 - improvement: documentation on using Unity

Version 1.7.0 (released Dec 20, 2013)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - new feature: using UNICORE 7 base libraries
 - new feature: sweep support for arguments and stage-ins
   (SF feature #286). Stage-in sweep requires UNICORE 7.0 or later
 - new feature: possibility to use the Service Orchestrator
   broker service (ucc run --broker SERVORCH). Requires workflow system
   v6.6.0 or later
 - new feature: "ucc run --dryRun ..." to only list possible resources
   but not submit a job (SF feature #289)
 - new feature: new "job" command for getting status, aborting, 
   and restarting a job. Restart requires UNICORE 7.0 or later
 - new feature: option to get short lived certificate from myproxy
 - new feature: introduced "bes-get-output" command for fetching 
   output files of bes activities (requires UNICORE 7.0 or later)  
 - improvement: better commandline support in shell mode
 - improvement: better performance for list-* operatons
 - improvement: unified commands "job-status", "job-abort" and 
   "job-restart"
 - fix: in 'shell' mode UCC asks for password(s) for
   every command (SF bug #3609866)
 - fix: BES commands ignore '-s' option when contact-registry flag 
   is set to "true" (SF enhancements #3610031)
 - fix: out-of-memory when large truststores are used
   (SF bug #3610013)
 - fix: incomplete documentation (SF bug #3609785)
 - fix: smarter handling of "contact-registry" flag (SF bug #3609914)
 - fix: "broker-run" command fails when resolving "u6://" URLs
 - fix: "broker-run" handles local files correctly and prints job address 
   also in async mode (SF bug #635)
 - fix: security preferences (-Z option) were ignored
 - fix: "Preferred protocols" in .u file and preferences is ignored
   for data staging (SF bug #599)

Version 1.6.0 (released Mar 25, 2013)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - updated to UNICORE 6.6.0 base libraries
 - full support for the EMI common authentication library (CaNL)
   (try "ucc help-auth" to see a full list of CaNL options)
 - improvement: shell: better command line completion and 
   'unset' command to clear a variable
 - new feature: "cat" command for listing a remote file
 - new feature: pluggable authentication mechanisms
 - UFTP does no longer try to 'guess' the correct client IP

Version 1.5.1 (released Dec 3, 2012)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - fix: using resource reservation led to an error
   (SF bug #3528602)
 - improvement: "issue-delegation" does not contact registry if 
   not necessary
 - fix: copy-file "-R" does not need an argument
 - new feature: "reservation" command to create and manage resource
   reservations (SF feature #3021335)
 - improvement: run, get-status, get-output accept multiple arguments
   (SF feature #3571071)
 - fix: add "samples" dir to deb/rpm
 - fix: missing local import files can cause errors in "get-status" 
   and "get-outcome" (SF bug #3570378)

Version 1.5.0 (released May 21, 2012)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - updated to UNICORE 6.5.0 base libraries
 - new feature: SAML push support (SF feature #2141970) 
 - improvement: support for EMI registry (SF enhancements #3438744)
 - improvement: usage information  ("ucc <cmd> --help") reformatted
   and grouped to make it easier to read
 - new "list-transfers" command to list server-server transfers, which is
   supported by 6.5.0 and later servers (SF enhancements #3468402)
 - improvement: removed unnecessary libraries (SF enhancements #3480082)
 - improvement: more useful workflow-info output (show number of jobs, 
   storage URL, tracer URL, list job URLs)
 - improvement: accept common OS names ignoring case
 - improvement: do *not* fallback to demo registry if no registry is given
 - improvement: allow to skip registry connect using a preferences entry 
   "contact-registry=false"
 - fix: missing local files are detected before workflow submission
   (SF bug #3495229)
 - improvement: better sample script "killall.groovy"
 - fix: wildcard exports did not work (SF bug #3502412)
 - improvement: when downloading results, create sub-dir for output files 
   (stdout etc) instead of using job-id as prefix
 - fix: re-try failed imports/exports once using the BFT protocol.
   If import still fails, destroy the job to prevent it staying in READY 
   state. (SF bug #3510021)
 - copy-file: support new reliable server-server file transfer mode
 - new feature: RunTest command for running system tests

Version 1.4.2-p1 (released Dec 15, 2011)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - fix: UFTP transfer uses constant secret (SF bug #3459430)
 - fix: HTTP proxy settings discarded (SF bug #3436456)
 - fix: support "mailto:" URLs for stageout

Version 1.4.2 (released Oct 20, 2011)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - updated to UNICORE 6.4.2 base libraries
 - improvement: display BES Factory in system-info command
   (SF enhancement #3382073)
 - new feature: Add new file operations setacl, chmod, chgrp, stat
 - fix: parameters from UCC properties file are properly used
   (e.g. HTTP timeouts)
 - improvement: allow to override UFTP server host with value
   from UCC properties (SF enhancement #3389004)
 - improvement: show progress information in data movement operations
 - improvement: better semantics for get-file and put-file when
   source/target is a directory (SF enhancements #3297983)
 - fix: error reporting in copy-file (SF bug #3406663) 
 - fix: use user-defined names for stdout/stderr also for exported 
   files (SF bug #3396208)
 - improvement: list-sites: "-l" gives list of logins and groups, 
   "-s" option allows to limit list to a single site
 - suppport for specifying Unix group and (accounting) project 
   in job .u file via "Group" and "Project" tags
 - fix: workflow: validation flag "true"/"false" was reversed
 - metadata: full storage URL can be used (SF enhancements #3390525)
 - new feature: put-file/get-file of whole directories (SF feature #3374325)
 - new feature: ucc-admin module for accessing the AdminService of 
   a UNICORE/X container (SF enhancements #3390537)
 - improvement: OGSA-BES: show full job status in verbose mode
 - improvement: allow to specify ftp/scp credentials in .u file

Version 1.4.1 (released Jul 11, 2011)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - updated to UNICORE 6.4.1 base libraries
 - new feature: support for UFTP
 - fix: metadata option "-m" is ignored (SF bug #3294255)
 - fix: in shell mode, exceptions during command processing 
   do not lead to exiting the UCC
 - fix: use trust delegation for all storage commands, which
   is required when working with the new distributed storage 
   service
 - fix: in shell mode, re-configure security properties for
   each new command
 - improvement: add append option ("-a") in get-file
 - improvement: add helper to guess missing file transfer 
   parameters
 - fix: check whether protocols are invalid (SF bug #3314814)
 - documentation update
 - new feature: in shell command, 'set' can be used to view
   and set properties
 - more readable details output for list-sites and list-storages
 - new WSRF operation to set the termination time of a resource
 
Version 1.4.0 (released Apr 16, 2011)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - Java 1.6 is mandatory
 - update to UNICORE 6.4.0 base libraries
 - fix: "registry" option consumes too many command line arguments
   (SF bug #3103522)
 - fix: remove unused "site" option from list-sites
 - improvement: allow to specify job lifetime in .u file 
   (SF feature #3074707)
 - improvement: allow to set system variables (-D, -X, etc) by
   setting them in an environment variable UCC_OPTS
   (SF feature #3132237)
 - DEB/RPM: change installation paths to ".../unicore/ucc"
 - new feature: wildcards for local file import/export
   (SF feature #2528550)
 - support extended parameters for file transfers
 - documentation converted to Aciidoc format
 - improve data upload for workflow system: if available, 
   use of a storage factory is preferred over shared SMS
 - add "metadata" command for accessing UNICORE's new metadata service
 - fix: file transfer protocol preferences are used consistently
 - improvement: available UCC commands are discovered without the need
   to specify them in the extensions file
 - improvement: documentation in single page HTML and in PDF format

Version 1.3.1 (released Jul 15, 2010)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - allow to configure extra out handlers (SF feature #2969305)
 - more detailed output from "system-info" command
 - workflow commands can properly deal with StorageFactory
 - add Linux packages in RPM and DEB format (SF feature #2952773)
 - fail job if local import fails; optionally ignore this failure using
   a new attribute 'FailOnError' (fix SF bug #2990311)
 - allow to use EPRs for OGSA-BES factories (SF feature #2991277)
 - allow absolute paths in local imports/exports (SF bug #2999259)
 - validate the given JSDL for workflows and single jobs 
   (SF bug #2998673). Validation errors are printed
   to the console in 'verbose' mode, and logged at DEBUG level.

Version 1.3.0 (released Feb 8, 2010)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - support for new StorageFactory service
 - new "create-storage" command
 - new "connect-to-testgrid" command for gaining access to the 
   public testgrid at http://www.unicore.eu/testgrid
 - add "ucc shell" commandline completion for filenames
 - add "mkdir" and "rm" commands
 - fix trust delegation in "copy-file"
 - split code into multiple modules
 - commands to access OGSA-BES services included into the distribution
 - allow to issue a TD assertion using just a site name
 - fix batch mode to exit when not connected to any sites
 - fix non-working "brief" option to "Run" command
 - allow to specify both total cpus and nodes+cpus per node.
 - support specifying remote login via a user assertion (option '-U')
 - consistent non-zero exit code in case of errors

Version 1.2.2 (released Oct 13, 2009)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - depends on UNICORE 6.2.2 libraries
 - bugfix in batch mode (would finish before jobs were all processed)
 - new "list-storages" command
 - provide commandline editing in shell mode
 - add bash completion (in "extras" directory)
 - always write job descriptor in batch "submit only" mode
 
Version 1.2.1 (released Aug 28, 2009)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - batch mode: flag "-X" now means: do not download stdout/err,
   but download exports defined in .u file
 - batch mode: always print statistics on exit
 - batch mode: in case of job, failure write job descriptor (.u file) to output directory (with
   prefix "FAILED\_"
 - consistent syntax for imports/exports and data staging. E.g. "Imports" covers both
   local and remote files, always use "From", "To" and "Mode". The old syntax is still supported. 
 - resolve addresses like "u6://STORAGE-NAME/..." where STORAGE-NAME is a shared SMS 
   listed in the registry
 - connect command: do not print "access denied" if not in verbose mode
 - print line numbers when reporting errors in .u files
 - include the core workflow commands into the UCC base. The command names now are
   "workflow-submit", "broker-run", "system-info", "workflow-control" and "workflow-trace"
 - improve performance of connect, list-sites, run, etc commands by parallelizing the 
   resource lookup
 - timing mode (option "-y") works uniformly for all commands
 - documentation improved (http://www.unicore.eu/documentation/manuals/unicore6/ucc)
 - updated Groovy lib to 1.6.4 
 
Version 1.2.0 (released Mar 25, 2009)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - avoid exception printout in case a site is not accessible
 - do not test the Registry connection in the 'WSRF' command 
   (the user might not want to talk to a registry)
 - Emacs mode: add command to remove job
 - simple interactive mode ("ucc shell")
 - allow to set "verbose" and "timing" mode in preferences file
 - new command "issue-delegation" to issue a trust delegation assertion
 - allow to configure default preferences location 
   (using "-Ducc.preferences=..." in the start scripts)
 - new "find" command (uses server side find new in U6.2.0)
 - support for more than one registry
 - fix finding the installation directory in the 'ucc' shell script
 - commented example user preferences file
 - improved error printout: root error is always printed, but full stack trace only in verbose mode
 - mask password entry on stdin
 - improve weighted site selection in batch mode
 - fix Windows ucc.bat to work in directories with spaces
 - added possibility to query the CIP (CIS InfoProvider) ("ucc query-cip")

Version 1.1.3 (released Oct 28, 2008)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - check more resource requirements (e.g. operating system)
 - allow to redirect stdin (sets the POSIX Input element) 
   (and similarly for stdout and stderr)
 - support JSDL creation flag (overwrite/append/nooverwrite) in stage in/out
 - allow to set site name in job description ("Site: sitename")
 - new "run" option "-H" that prints an example job and quits 
 - print the job log if job fails
 - use log4j, configured by default in conf/logging.properties
 - fix use of non-UNICORE 6 URLs in stage in/out (e.g. plain http or ftp URLs)
 - many new batch mode features and bug fixes (thanks to Richard Grunzke)
    - "submit-only" flag (-S) for batch mode
    - limit on number of new job submissions in batch mode (-M)
    - more fault-tolerant behaviour
    - pluggable site selection
    - .job file names contain the name of the request (.u) file
 - support for custom security handlers
 - improved help output (ucc -h)
 
Version 1.1.2 (released Aug 1, 2008)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - allow setting low-level options (e.g. connection timeouts)
 - fix batch mode problems (files not deleted) under Windows
 - update to unicorex 1.1.2
 
Version 1.1.1 (released May 15, 2008)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - allow to configure separate truststore (SF feature #1943012)
 - add Emacs mode files in the extras/emacs-mode folder
 - batch mode accepts only ".u", ".jsdl" or ".xml" files (fix SF bug #1938686)
 - support JSDL files in batch mode
 - cache results of registry queries in batch mode 
 - cleanup of filetransfer resources
 - minor bugfixes
 
 
Version 1.1 (released Mar 20, 2008)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - support for new UNICORE 6.1 features:
 	- setting the user name
 	- job progess indication (if available)
 - check if application is supported on TSS
 - find storage server identity for trust delegation in file transfers	
 - the 'ls -l' command now shows file modification times
 - bugfixes

Version 1.0.1
~~~~~~~~~~~~~


 - resolve u6:// style URLs also for stage-out
 - bug fixes
 - add ucc.bat startfile for Windows
 - new commands: 'ls' for listing a remote storage, 'abort-job'
 - new filtering option for list-jobs and list-sites commands 


Version 1.0 (released Aug 13, 2007)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - first release.
