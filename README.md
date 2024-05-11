# README

## SRC
> To be used a reference

- Original Source Code (genv1)


## Inf-Dev
> Infinite Development

- OUTDATED
- Contains the updated code (genv2)


## Docker
> Containerization

- Contains the docker container
- Literally should be a plug and play type scenario


# DEMO
> Contains the working DEMO of the codegen (genv3)

## How to run demo

### Running Command

Through Python:
  ````
    py codegen.py <insert flags>
  ````

Through Executable:

  ```
   ./codegen <insert flags>
  ```

### Flags

```
Shortcut  Full-Flag                Description
-h        --help                   Prints out a help description
-G        --GUI                    Enables GUI (WIP)
-S        --Shell                  Enables Shell Interpreter
-D        --Debug                  Enables Debug Mode
-dR       --DirectoryHandler       Enables the use of DirectoryHandler
-event    --EventCount             Edits number of Events
-const    --GlobalConstCount       Edits number of Global Const Variables
-funct    --FuncCount              Edits number of functions
-actItem  --ActorItems             Edits the numbers of items with an actor
-act      --ActorsNum              Edits the nubmer of Actors
-state    --StateNum               Edits the number of States
-uV       --UnsafeVariableDeclare  Enables unsafe variables (i.e. int a = False)
-uE       --UnsafeEvent            Enables unsafe Events
-depth    --MaxStateDepth          Edits max number of nested states



All numeric values are set to 1, meaning at most 1 of the selected option will be generated.
All boolean values are set to true. Meaning if the flag is used, then that feature is enabled in the code gen.

Flags can be set in any order, and not all flags need to be provided.
```

### Directory Handler
  >  Handles where the generated tests are sent to

  When the `-dR` flag is used the user is prompted with the following:

  ```
  How many fail cases do you want?: <insert number of cases>
  How many passing cases do you want? <insert number of cases>
  What do you want to name them? <give those cases a name>
  ```

#### Finding the Directories

The genereate tests  can be found in `TestingSessions` Directory, where passing and failing cases are in their respective directory

### Autocompile

WIP

### Collaborators

Jose Ocampo, AB Paxtor Garcia, Sam Skidmore, Mohammad Asim Sheikh, Wayne Rasmussen, Jose Martinez, Zori Badkerhanian, German Wong







