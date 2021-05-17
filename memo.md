# Memo

- `Dockerfile`: settings for building a docker image
- `docker-compose.yml`: settings for running docker images
- If you want to use developement mode, then you need to bind mount the folder that contains `app.py` and set the environment variable `FLASK_ENV: development` in `docker-compose.yml`