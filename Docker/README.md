# Docker

## About

- A containerzation of both Proteusi

## Dependencies

- Docker Desktop or Equivalent

## How to use

1. Clone repo
2. Create image
3. Run via container

### Creating an image

```
   docker build -t proteus:latest .
```


### Running a container

```
  docker run -p 1337:22 -it proteus:latest
```

- Afterwards, type `fish` to get an easier terminal if you don't know sh/bash/st

### Leave container running in the background

CTRL-P, then CTRL-Q

- To return to the containser ssh to localhost:1337, and use creds given in the dockerfile

### Swapping Modes 

- To use SwiftProteus
  ```
    SwiftProteus
  ```

- To use C++Proteus
  ```
   C++Proteus  
  ```

## Other stuff in the container

### Text Editors
- nano
- helix

### SSH
- openssh



  