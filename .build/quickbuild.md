Windows:
  1. Install docker desktop, it'll come with all the dependencies required for docker compose
  2. In your terminal navigate to this folder example 'C:\windows\users\nate\documents\coding\ClearCare\.build'
  3. Run `docker compose up -d` to start all the current services defined within the compose file
  4. Running `docker ps` will show you the running containers and their statuses (plus ports they are mapped/listening on)
  
MongoDB administration:
  1. Create within the .build folder an file called `.env` this will be used to store our secrets
  2. Add your secrets to the `.env` file, for example `Mongo_Root_User=...` with your actual value e.g. "admin", repeat the process for `Mongo_Root_Password`.
  3. Install and run Mongo Compass which is a GUI tool for managing our database.
  4. Using Mongo Compass, add a new connection, which will have a default string. Navigate to the "advanced connection options" and enter the following:
    - Username: `Mongo_Root_User` (from your `.env` file)
    - Password: `Mongo_Root_Password` (from your `.env` file)
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
  7. Modify the above flags to values set within .env, host should be `localhost` and port should be `27017`. Optionally omit the `--authenticationDatabase` flag as it defaults to `admin`.
