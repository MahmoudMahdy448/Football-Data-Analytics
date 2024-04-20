# Football-Data-Analytics
Interactive Dashboard for Football Kaggle dataset from Transfermarkt.

## Data is extracted from Kaggle
 - https://www.kaggle.com/datasets/davidcariboo/player-scores

What does it contain?
The dataset is composed of multiple CSV files with information on competitions, games, clubs, players and appearances that is automatically updated once a week. Each file contains the attributes of the entity and the IDs that can be used to join them together.

### What's case about? (Problem description)
- providing analytics and statistics on all players during the tournaments, along with comprehensive statistics on European players' performance. This includes analyzing their goals, assists, and other relevant metrics. By examining the data, managers can gain insights into the performance of European players and make informed decisions when scouting for talent to join the top five leagues, such as the Premier League.


### Technology Stack

- **Terraform** (Infrastructure as Code)
    - **Deployment**: Used to deploy all the needed resources on GCP.
        - create a gcp service account
        - authenticate terraform with gcp using service account credentials key
        - apply gcs bucket an bigquery dataset resources using main.tf and variables.tf files  

- **Docker**
    - **Containerization**: running a docker compose up command to run in container.

- **Google Cloud Platform** (GCP)
    - **Google Cloud Storage (Datalake)**: Where data lands from the bash script that we run on Google Cloud VM
    - **BigQuery (Datawarehouse)**: Where data is stored in dimensional modeling.

- **Mage**
    - **Orchestration Tool**: Used for our data pipeline flow.

- **DBT** (Data Build Tool)
    - **Reporting Layer**: Built in models.

- **Looker Data Studio** 
    - **Dashboard**: - [Google Looker Studio](https://lookerstudio.google.com/overview).


### Data Pipeline Flow

![alt text](resources/image.jpeg)

As shown in image our data flow consists of below section:

**1. Data Ingestion**:
- Landing the raw data which fetched using Kaggle API token into google cloud storage into 9 csv format files using the download from kaggle to gcs bash script to land it directly to gcs  .
    - types of files: 
        - file for all players appearances in all europe competition.
        - file for all players data.
        - file for all competitions data etc.

        ![alt text](resources/image2.png)

    - steps to ingest the data directly to gcs:
        - Import your Kaggle API Key (kaggle.json file)to Cloud Shell
        - Get your GCP Project-ID and the dataset you want to downlaod
        - execute it on Cloud Shell

        ```bash
        #run this command into you vm cloud bash
        ./download_from_kaggle.sh [DATASET] [Your-GCP-Project-ID]
        ```
        - data is unzipped and are ready in the gcs bucket

        ![alt text](resources/image3.png)


**2. Data orchestration**:
- setting up mage instance:
    ```bash
    git clone https://github.com/mage-ai/mage-zoomcamp.git mage-zoomcamp
    ```
- Navigate to the repo:
    ```bash
    cd mage-data-engineering-zoomcamp
    ```
- Rename dev.env to simply .env— this will ensure the file is not committed to Git by accident, since it will contain credentials in the future.

- Now, let's build the container
    ```bash
    docker compose build
    ```
- Now, navigate to http://localhost:6789 in your browser! Voila! You're ready to get started with Mage.

- create our pipelines: (from GCS, transforming, to Biquery dataset )

    - appearances pipeline:


    ![alt text](resources/appearances_pipeline.png)

    - players pipeline: 

    ![alt text](resources/players_pipeline.png)


**3. DBT transformations**:
- will be using dbt cloud cli and github actions, authenticated with our bigquery dataset to do our data model
- our 3 models are aimed to manipulate our to get the data to the analytics ready phase, 3 models are create with a schema:
    - models > schema.yml file:
    ```yml
    version: 2

    models:
    - name: player_performance
        description: Aggregated performance metrics at the player level
        columns:
        - name: player_id
            description: The ID of the player
            tests:
            - not_null
            - unique
        - name: total_goals
            description: The total number of goals scored by the player
            tests:
            - not_null
        - name: total_assists
            description: The total number of assists made by the player
            tests:
            - not_null
        - name: total_yellow_cards
            description: The total number of yellow cards received by the player
            tests:
            - not_null
        - name: total_red_cards
            description: The total number of red cards received by the player
            tests:
            - not_null
        - name: total_minutes_played
            description: The total number of minutes played by the player
            tests:
            - not_null
    ```
    - after building our models, our analytics ready data are exported to Bigquery:
        ![alt text](resources/dbt_models_data.png)

4. **Dashboarding:**
    - create a data source on looker studio using the resulting data from DBT model on Bigquery
    - Check out the dashboards below:
    - **Player Performance Analysis** 
    - https://lookerstudio.google.com/reporting/c35d78dd-2bdb-4e86-a8b9-dff903235ddd
    - Dashboard showing the Performance stats of players such as Goals, Assists, Market Value and more.
    
     ![alt text](resources/dashboard.png)