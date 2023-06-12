# Scripting API
## Arguments
Scripts can be called with a list of arguments that can be accessed inside the script with the "args" global.
```cli
> run test_script.py arg1 arg2 arg3...
```
In test_script.py:
```python [test_script.py]
print(args[0]) # prints "arg1"
print(args[1]) # prints "arg2"
```
## Returning Results
Scripts must return results by writing to the local result variable.
script_1.py:
```python
result = unwrap(client.fleet.get_my_ship(args[0]))
```
script_2.py:
```python
TODO
```

## System Logging
