# <img alt="Glow Squid from Minecraft" src="images/Glow_Squid_BE1.webp" width="40" height="40" /> Glow Squid <img alt="Glow Squid from Minecraft" src="images/Glow_Squid_BE1.webp" width="40" height="40" />

> **_NOTE:_**  By request, the name of this repository is supposed to be "random".
> Inspired by GitHub's suggestion of "glowing-telegram", I picked "Glow Squid" because it is cuter.

## Running application

### Prerequisites
- [Docker](https://docs.docker.com/engine/install/)

### Steps
1. Start the containers on docker by running the command below:
    ```
    docker compose up -d
    ```

2. Apply changes to the database:
   ```
   docker compose exec wind-farm-service python src/manage.py migrate
   ```

3. Check the results on your browser at http://localhost:3000/


### Importing initial data

1. Start the relevant containers (skip this step if you just run `docker compose up -d`):
   ```
   docker compose up -d wind-farm-service
   ```

2. Import the Projects data
   ```
   docker compose exec -it wind-farm-service python src/manage.py import_projects raw-data/Project_raw_table.csv
   ```

3. Import the WTGs data
   ```
   docker compose exec -it wind-farm-service python src/manage.py import_wtgs raw-data/WTG_raw_table.csv
   ```
