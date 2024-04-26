-- models/transformations/competitions_enhanced.sql
SELECT 
    competition_id,
    IFNULL(country_name, 'International') AS country_name,
    name,
    sub_type,
    CONCAT(IFNULL(country_name, 'International'), ' - ', sub_type) AS competition_name,
    domestic_league_code,
    is_major_national_league
FROM 
    `football-data-analytics.football_data_analytics_dataset.competitions`