-- models/transformations/datetime_dim_simplified.sql
SELECT 
    datetime_id,
    date,
    year
FROM 
    `football-data-analytics.football_data_analytics_dataset.datetime_dim`