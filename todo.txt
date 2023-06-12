=================
====== CLI ======
=================
CLI manages all user input and interface
commands:
- help: list commands and scripts
- run [script]: run a script
- list: list all scripts and their metadata
- exit: exit the program
- processes: list all running processes
- token [token]: set the token

=================
==== LOGGER =====
=================
TODO: Log timestamps from response to log. Automatically log whenever a request is made (juicy data)
TODO: Saving to logfile

=================
==== CONFIG =====
=================
Using simple .env file for now
os.getenv() to fetch env var

=================
===== ERROR =====
=================

=================
===== TESTS =====
=================
TODO: Implement pytest

=================
=== SCRIPTING ===
=================
FINISHED: Pass arguments to script from CLI
FINISHED: Allow scripts to return values
TODO: Script metadata (name, description, etc) <- Use docstrings for this
TODO: Run scripts from other scripts
TODO: Spawn process for scripts (concurrency)
FIXME: Executor should catch ALL exceptions and log them

=================
=== DATABASE ====
=================
TODO: Implement database
TODO: Implement caching middleware (low priority)

