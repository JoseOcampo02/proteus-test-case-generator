# Proteus Test Case Generator

## Project Overview

  This project aims to create an accesible automatic test case generator for all versions of the Proteus Programming Languages, for which is to be employed in the improvement of the Proteus Compilers by finding bugs between the compiler and grammar of the language.

## Key Features

### Implemented Features

These are features which have been fully implemented to the project.

- One-to-One Translation of Proteus Grammar to Proteus Code
  - The Generator works by translating a production of the Proteus Grammar to a Python Function Equivalent.
- Toggleables
  - Allows the customization of test cases by enabling how many of a certain production can occur at most
- Directory Management
  - Stores multiple generated file into their respective directory

### Tentative Features

By tentative, the project contains early versions of these features, but these have yet to be fully finalized.

- Graphical User Interface
  - The GUI appears through the `-G` Flag, but functionality between GUI and Test Case Generator have yet to be implemented.
- Shell Interpreter
  - The interpreter appears through the `-S` flag, but functionality between Interpreter and Test Case Generator have yet to be implemented.
- Auto-Compilation
  - This can be found within the `/src/generatorv-v2/SafeTestGenerator.py`, but this has not been implemented into the working demo version


## How it works

### General Overview
  As stated before, the generator is designed to be a one-to-one translation of the Proteus grammar to a Proteus code via python functions. For instance, the Proteus grammar states an actor state can contain actors, so we a have a python function which allows this to be generatred as Proteues code.


#### Passing Cases

  Passing Cases are generated via the SafeTestCaseGenerator.py.
#### Failing Cases
  
  Failing Test Cases are generated via the fail_case_gen.py.

Both of which can be found within the `/demo` directory

## Prequisites

- Python Version 3.10 or later
- Both versions of Proteus (C++ and Swift)

## Getting Started

### Building from source

#### Clone the Repo

1. Clone
   ```
   git clone https://github.com/JoseOcampo02/proteus-test-case-generator.git
   ```
2. Change Directory to Demo after opening the file
   ```
    cd demo
    python3 codegen.py [insert flags]
   ```

#### Running the Application

The application can be initialized via the following commands:

If using Python:
  ```
  py codegen.py [insert flags]
  ```

If using the executable:
  ```
  ./codegen.exe [insert flags]
  ```


#### Flags

  ```
  Shortcut  Full-Flag                Description
  -h        --help                   Prints out a help description
  -G        --GUI                    Enables GUI (WIP)
  -S        --Shell                  Enables Shell Interpreter (WIP)
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

#### Directory Handler

  When the `-dR` flag is used the user is prompted with the following:

  ```
  How many fail cases do you want?: <insert number of cases>
  How many passing cases do you want? <insert number of cases>
  What do you want to name them? <give those cases a name>
  ```

#### Finding the Directories

The genereate tests can be found in `TestingSessions` Directory, where passing and failing cases are in their respective directory


### Alternate Method: Docker

#### Prequisites

- Docker Desktop or equivalent

#### Pull the image
  ```
  docker image pull abpaxtor10/proteus:latest
  ```

#### Docker Run
  ```
  docker run -p 1337:22 -it abpaxtor10/proteus:latest
  ```

#### Leave container running in the background

CTRL-P, then CTRL-Q

- To return to the containser ssh to localhost:1337, and root credentials are default

#### Swapping Modes 

- To use SwiftProteus
  ```
    SwiftProteus
  ```

- To use C++Proteus
  ```
   C++Proteus  
  ```

- To use Test Case Generator
  ```
  cd proteus-test-case-generator/demo
  python3 codegen.py [insert flags]
  ```


## Collaborators

- Jose Ocampo
- Sam Skidmore
- Wayne Rasmussen
- Zori Badkerhanian
- Mohammad Asim Sheikh
- German Wong
- Jose Martinez
- AB Paxtor Garcia
- Elliot Fayman


