```Dockerfile
FROM base:container 
USER root # the user which the container runs
COPY ./host/file /container/file
ENV myenvironment=admin\
    myenv2=password

RUN commands to be executed # eg. apt install software
USER myuser # switch back to user with less permission

ENTRYPOINT ["./entrypoint.sh"] # what the command container should run when starting the container
```
`FROM` the base container
`ENV` define environmental variables
- the env variable would be visible in the container by `env` function
`RUN` execute Linux commands in the container 
- split `RUN` commands to multiple lines
- run `apt update && apt install` in the same `RUN` command
- remove the apt cache afterward
```bash
    && rm -rf /var/lib/apt/lists/*
    && apt clean # officla ubuntu Docker image does this automatically
```
`COPY` copy file from host directory to container
`CMD` translate to entry point that runs after container starts, <font color=DC143C>the CMD argument has to be in double quotes.</font>

### Multi-arch Build
```bash
docker buildx build --platform linux/arm64 . -t caddytest
```
- using `docker buildx`, we can build an image that is compatible with many architectures
### Multi-stage Build

