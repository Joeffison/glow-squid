# <img alt="Glow Squid from Minecraft" src="images/Glow_Squid_BE1.webp" width="40" height="40" /> Glow Squid <img alt="Glow Squid from Minecraft" src="images/Glow_Squid_BE1.webp" width="40" height="40" />

> **_NOTE:_**  By request, the name of this repository is supposed to be "random".
> Inspired by GitHub's suggestion of "glowing-telegram", I picked "Glow Squid" because it is cuter.

## Running application

### Prerequisites
- [Docker](https://docs.docker.com/engine/install/)

### Running with Docker (recommended)
1. Start the containers on docker by running the command below:
    ```shell
    docker compose up -d
    ```

2. Apply changes to the database:
   ```shell
   docker compose exec wind-farm-service python src/manage.py migrate
   ```

3. Check the results on your browser at http://localhost:3000/


### Running without Docker

#### API
1. Make sure you are inside the [wind_farm_service](wind_farm_service) directory at the root
   ```shell
   cd wind_farm_service
   ```

2. Install all dependencies
   ```shell
   poetry install
   ```

3. Have a database running by one of the alternatives:
   - **Recommended:** `docker compose up -d wind-farm-sqldb`
   - Point your application to a **development** database running remotely
   - Install and run a database locally (not a good practice)

4. Make sure you have an `.env` file at the root of [wind_farm_service](wind_farm_service) with
values for the following variables:
   ```text
   MAIN_DB_HOST=
   MAIN_DB_PORT=
   MAIN_DB_DATABASE=
   MAIN_DB_USER=
   MAIN_DB_PASSWORD=
   ```

5. Start the api server
   ```
   dotenv run python src/manage.py runserver
   ```

#### WebApp
1. Open a second terminal tab and make sure you are inside the [wind_farm_webapp](wind_farm_webapp)
directory at the root:
   ```shell
   cd wind_farm_webapp
   ```

2. Install all dependencies
   ```shell
   yarn install
   ```

3. Make sure you have an `.env` file at the root of [wind_farm_webapp](wind_farm_webapp) as in the
example below:
   ```text
   REACT_APP_WIND_FARM_API=http://localhost:8000
   ```

4. Start the webapp server
   ```shell
   yarn start
   ```

5. To see the results, click on the link displayed. 
It will look something like http://localhost:3000/


### Importing initial data

1. Start the relevant containers (skip this step if you just run `docker compose up -d`):
   ```shell
   docker compose up -d wind-farm-service
   ```

2. Import the Projects data
   ```shell
   docker compose exec -it wind-farm-service python src/manage.py import_projects raw-data/Project_raw_table.csv
   ```

3. Import the WTGs data
   ```shell
   docker compose exec -it wind-farm-service python src/manage.py import_wtgs raw-data/WTG_raw_table.csv
   ```

> **_NOTE:_**  If running locally, you can skip the first step and run the main commands replacing
> "docker compose exec -it <service-name>" by "dotenv run"
> (example: `dotenv run wind-farm-service python src/manage.py import_projects raw-data/Project_raw_table.csv`). 
