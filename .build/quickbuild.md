# Windows:
  1. Install docker desktop, it'll come with all the dependencies required for docker compose
  2. In your terminal navigate to this folder example 'C:\windows\users\nate\documents\coding\ClearCare\.build'
  3. Run `docker compose up -d` to start all the current services defined within the compose file
  4. Running `docker ps` will show you the running containers and their statuses (plus ports they are mapped/listening on)
  5. To stop containers run `docker compose down`

# Linux:
  1. Install docker, docker compose
  2. Navigate to `ClearCare/.build` 
  3. Run `docker compose up --build` or `docker compose up -d`
    - Former command will build everything from scratch recommended on the first run
    - Use latter command after project has been built
  4. Run `docker ps` to confirm container statuses
  5. If a container fails use this command `docker logs {container_name}` replacing from the star of the curly braces to the end of the curly braces with the container name e.g. "my-nginx-container"
  6. To stop containers run `docker compose down`

# MongoDB administration:
  1. Create within the .build folder an file called `.env` this will be used to store our secrets
  2. Add your secrets to the `.env` file, for example `MONGO_ROOT_USERNAME=...` with your actual value e.g. "admin", repeat the process for `MONGO_ROOT_PASSWORD`.
  3. Install and run Mongo Compass which is a GUI tool for managing our database.
  4. Using Mongo Compass, add a new connection, which will have a default string. Navigate to the "advanced connection options" and enter the following:
    - Username: `MONGO_ROOT_USERNAME` (from your `.env` file)
    - Password: `MONGO_ROOT_PASSWORD` (from your `.env` file)
    - Authentication Database: `admin`
    - Authentication Mechanism: `default`
  5. Use the "Save and connect" button and the database should be connected successfully.
  6. Alternatively, if you prefer CLI tools, you can use `mongosh` to connect to the database from the command line. 
    - Use the following flags:
    - `--username`
    - `--password`
    - `--authenticationDatabase`
    - `--host`
    - `--port`
  7. Modify the above flags to values set within .env, host should be `localhost` and port should be `27017` which is the default for MongoDB and for the purposes of the project has been left as is. Optionally omit the `--authenticationDatabase` flag as it defaults to `admin`.

  
# Python Virtual Environment:
  1. Create a virtual environment using `python -m venv .venv` <-- while within the root directory of this project
  2. Activate the virtual environment by running `.venv/scripts/activate` within the powershell terminal while located in the root directory of this project
    - MacOS or Linux based systems should use `source .venv/bin/activate`
  3. Running the app without docker is not recommended. However running `run.py`within the backend folder should run a local webserver with zero frontpage that can be used for troubleshooting. Use the debug flag within the run call within main, though it is highly recommended to make use of the test folder directory to write tests and do white-box testing in there.

# Dockerfiles & Images:
For ARM based systems (specifically Windows) running on snapdragon based processors. Follow the instructions below
  1. All files listed here under build will require modification
      - `.build/flask/flask.Dockerfile`
      - `.build/nextjs/nextjs.Dockerfile`
      - `.build/nginx/nginx.Dockerfile`
      - `.build/docker-compose.yml`
  2. Modify the first line in each `*.Dockerfile` to have `arm64v8/` inserted before the base image for example `FROM python:3.12-slim` --> `FROM arm64v8/python:3.12-slim`
  3. For the compose file modify the block for MongoDB line 35 (as of writing this) to also insert `arm64v8/` before the mongo image

  
# Secrets
  Saving API keys & admin credentials is generally not a good idea in plaintext, thus the solution is to save these in secure files throughout the project `.env`
  Located within `/dev/env.md` from the project's root. States all the locations and expected content stored within these env files which currently should be 2 files.
