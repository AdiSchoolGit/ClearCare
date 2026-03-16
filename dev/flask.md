# 3/07/26

Create new folder within `.build` called `flask`
  - create requirements.txt with latest version of Flask
  - create Dockerfile with an official Python provided trixie-slim base image
  
Add flask into services within `docker-compose.yml`
  - Simple hello world Flask app displayed

  # 3/08/26
  
  Resolve windows related issues:
    - Expects full path to be provided e.g. /app/server.py versus server.py even with `WORKDIR /app` set to run before copying files over
    - Change python slim image to an stable release version compared to the alpha trixie version
    - Modify docker-compose.yml context from the .build folder to having context of the root path.

# 3/16/26

Add load balancing to nginx.conf and update docker-compose.yml to include multiple flask services
  - Introduce multiple flask containers
  - Update locational routing from root to `/api/` to handle webserver requests

Edits made over couple of days
  - Modify folder structure to `app` which contains all the working parts of webserver
  - `tests` containing test files which are separate from the main app code 
    - A portion of the test files are hardcoded values which are tested
    - External API calls are done which are done through the `real` marker within the pytest suite
  - `server.py` replaced with `run.py` in `backend` and `__init.py__` located within the `app` folder
    - Common expected app format after looking at various tutorials
  - `app` folder structure
    - constants 
      Contains constant values e.g. conversions ensuring consistent formatting
    - clients
      Contains external API calls e.g. Google Places (NEW) API which contains nearbySearch used within `googlePlacesClient` 
    - repositories
      Database interactions e.g. CRUD operations on the database
    - routes
      
    - services
      Contains logic used within 
    - utils
  -
