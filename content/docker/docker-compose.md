```yaml
version: '3'
services:
  container: # this is not the same as container name
	container_name: name # must be defined here, especially in a stack, otherwise it will be named based on the current folder
	ports:
	  - 1234:1234/tcp
	environment:
	  - PUID=1000 # define environment variable in this format
	volumes:
	  - /host/path:/container/path
	restart: unless-stopped
```
A basic docker-compose in home settings will consists of `service name` (container), `container_name` (name), `ports` (1234), [networks](#[Networking](docker-networks.md)), `volumes`, [environments](#Environments)(PUID) and `restart` (unless-stopped). 

```yml
version: '3'
services:
  my-ubuntu: # name = folder-name-my-ubuntu
    image: ubuntu:latest
  my-nginx:
    image: nginx 
    name: compose-nginx # name = compose-nginx
```
- In this example, the container name would be `folder-name-my-ubuntu` and `folder-name-my-nginx`
- Must need to define it under container name for the desired name.

### [Networking](docker-networks.md)
**Adding Container to Custom Network**
```yaml
    networks:
      - net1
      - net2 # attaching to multiple networks
      - default
```
- multiple networks can be specified as a list
- when a container is in multiple networks, it will have multiple interfaces with multiple IP addresses
- when specifying `default` in networks, this is the default network that docker compose will create, eg. `folder-name_default`

Additional Options for each network:
- when specifying additional options with multiple networks, list cannot work
```yaml
    networks:
      net-1:
      net-2:
        ipv4_address: 192.168.120.254
```
- `ipv4_address` is specify custom IP address as long as it's in correct subnet

#### Network Definition
**YAML**
```yaml
networks:
  public:
    name: public
    ipam:
      config:
        - subnet: 192.168.120.0/24
          gateway: 192.168.120.1
```
- however, when defined as such, the network cannot be removed if there is active container, and when changing network configurations
**External**
```yaml
networks:
  net1:
    name: net1
    external: true
```
- the `external: true` specify that the network is managed outside of compose and already exists

### [Volumes](docker-volumes.md)


### Environments
`docker compose config` will print out the file with all the environment variables present
##### environments
```yaml
    environment:
      - PUID=1000
      - SHELL=${SHELL}
      TZ: "America/Vancouver"
```
- the `environment` can be set as a list `X=y` or a dictionary `X: 2`
- it can also consist of shell variables with `${}` syntax
	- `${:-}` default value if such variable is unset, similar to [bash variable](../bash/6.%20Case%20Statements%20&%20Arguments.md#^ccaace)
- environment variables will take precedence over [env_file](#^96654c)
Command substitution such as `$(id -u)` does not work, consider using system variables
##### env_file
```yaml
    env_file:
      - secret.env
      - ../folder/config.env
```
- using `env_file` key, the files are provided at list
- the file's location can be given as relative position or in another folder
- the file that is defined first will take precedence if duplicate arise

### Interactive
```yaml
    stdin_open: true
    tty: true
```
This is equivalent to `docker run -it`
