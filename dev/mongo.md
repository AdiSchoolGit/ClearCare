# 3/8/26

Create a new MongoDB container
  - Default Docker Hub image 
  - Working however there is no management interface

# 3/9/26

Attempt to build a smaller image of MongoDB
  - Build a custom Docker image using Alpine, to reduce image size. 
  - Removed custom alpine based dockerfile
  - Switch from latest image to Ubuntu based image (8.2.5-noble)
  - Remove MongoDB dockerfile & integrate into existing Docker-Compose.yml

# 3/10/26
  
Create .env file to store credentials

Attempt to build  Mongo-Express from Docker Hub
  - Image deprecated as of 2024
  - Replace with Mongo Compass, and have admin/management interface ran on host machine
  - Removed Mongo port mappings from NGINX --> Mongo documentation states to not attempt http configurations and avoid TCP connections

# 3/11/26

Resolve docker networking issues with Mongo
  - Added port mappings to expose Mongo to host machine
  - Despite the mongo container already getting hosted on default to port 27017 without needing the compose file, docker networking isolated the container and makes it inaccessible from the host machine without port mappings.

# 3/13/26

How to login to mongo through compass 
  - Enter in the string below into the connection string field:
    - mongodb://{user}:{password}@localhost:27017/
    - Replace {user} and {password} with your actual credentials
  - Alternatively if the connection fails despite `docker ps` returning that the container is running and actively listening on the default port
    - append `?authSource=admin` to the connection string
