Modules/Files to add
- Logger
- Config w/ token (take token from env? or config file? or arg?)
- Database if we use one
- Command handler or means to execute 

=================
====== CLI ======
=================
CLI manages all user input and interface
commands:
- help: list commands and scripts
- run [script]: run a script
- list: list all scripts
- exit: exit the program
- processes: list all running processes
- token [token]: set the token
allow running of scripts by simply file name (no run command)

=================
==== LOGGER =====
=================

TODO: Log timestamps from response to log. Automatically log whenever a request is made

=================
==== CONFIG =====
=================

=================
=== SERIALIZE ===
=================

=================
===== ERROR =====
=================

=================
===== TESTS =====
=================

=================
=== SCRIPTING ===
=================
we can use exec() to execute a string as python code. we can use this to execute scripts
maybe we can execute it in a differnet thread / process?
json.loads() to convert string to a dict

pass client to script (via executor)
- Communication between scripts? (concurrency + database?)

FINISHED: Pass arguments to script from CLI
TODO: Allow scripts to return values
TODO: Script metadata (name, description, etc)
TODO: Run scripts from other scripts
TODO: Spawn process for scripts (concurrency)
FIXME: Executor should catch all exceptions and log them (or pass them to the script)

=================
=== DATABASE ====
=================

