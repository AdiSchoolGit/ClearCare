# 3/07/26

Create basic configuration file `nginx.conf`
	- `events` block created to define how connection requests are handled
	- New http block focused on ipv4 based connections for local testing

Create `Dockerfile`
	- Pulls alpine-slim based image of nginx reducing footprint compared to the trixie (debian) based image
	- Replace the default conf file within the container with the new version
	- Expose port 80 for networking 

Create a compose file

Issue faced:
-  Attempting to spin up docker container without the `events{}` block within `nginx.conf` causes the container to fail

Solution:
- Adding `events{}` block before the main `http{}` block which defines reverse-proxy and load-balancing behavior.

# 3/8/26

Adjusted upstream {}
  - Docker networks change the way containers communicate, updated the server address to use the service name (`flask`) instead of `localhost` to resolve correctly.
  - Removed port block within the docker-compose.yml file since the service name resolves internally and is therefore redundant.
  
Adjust block in dockerfile
  - Redundant COPY usage, when volume mounting config in the compose file
  - Modify compose file context to root path, update paths references due to new context change

# 3/16/26

Adjust dockerfile image options for ARM developers
