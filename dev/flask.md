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
