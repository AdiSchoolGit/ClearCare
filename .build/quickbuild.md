Windows:
  1. Install docker desktop, it'll come with all the dependencies required for docker compose
  2. In your terminal navigate to this folder example 'C:\windows\users\nate\documents\coding\ClearCare\.build'
  3. Run `docker compose up -d` to start all the current services defined within the compose file
  4. Running `docker ps` will show you the running containers and their statuses (plus ports they are mapped/listening on)
  
MongoDB administration:
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

  
Python Virtual Environment (Windows):
  1. Create a virtual environment using `python -m venv .venv` <-- while within the root directory of this project
  2. Activate the virtual environment by running `.venv/scripts/activate` within the powershell terminal while located in the root directory of this project
  3. Install the required packages using `pip install -r ./build/flask/requirements.txt`
  4. Run the server using `python server.py` which should host the Flask server at `http://localhost:5000`
  This is only to run the server locally and not spin up the full application e.g. nginx, mongo, plus front-end in the future.
