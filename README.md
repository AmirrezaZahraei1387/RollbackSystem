# RollbackSystem

A simple rollback system for functions in order to store
the path of functionalities that must be rolled back if some other
function or process went wrong.

### Actions
An action defines the functionality of a rolling back for a given
request. For example suppose the program has saved a file is created.
Now suppose something went wrong, so the process cannot be finished,
and we should remove the file created. Actions will be used to so
without any extra works.

For creating an action you should give it a name, a predefined function
, and an optional argument for the number of parameters the function accept.
The name given must be unique otherwise a name error will result. The given
name will be used to identify the action passes action.

``` python
import rollbacksys
import os

# an action for removing files
remove_action = rollbacksys.Action("remove", os.remove, 1)
```

### ActionPasses

An action pass would be given by the program to the repository of
ActionPasses. It simply defines that now an event has been occurred, and
in order to roll this event back, you should use the certain Action.

For making an action pass you should provide the name of the
action must be used for rolling back and arguments for it.

``` python
import rollbacksys
import os

# an action for removing files
remove_action = rollbacksys.Action("remove", os.remove, 1)

action_pass = rollbacksys.ActionPass("remove", "__init__.ini")
```

### ActionCon

ActionCon(Action Container) is a container class for saving 
the action passes to the class.
In order to use it, First initializing the actions are needed, then
throughout the program we can add action passes to it, and when
ever needed we can roll back the changes.

``` python
import rollbacksys
import os

# creating the action container
action_con = rollbacksys.ActionCon()

# an action for removing files
remove_action = rollbacksys.Action("remove", os.remove, 1)
action_con.add_action(remove_action)


files = ["config.ini", "hello.py", "pc_cnfg..cnfg", "license.txt"]


for file in files:
    try:
        
        with open(file, 'w') as sample:
            pass
        action_con.add_action_pass(rollbacksys.ActionPass("remove", [file]))
    except Exception as e:
        action_con.rollbackAll()
        raise
```