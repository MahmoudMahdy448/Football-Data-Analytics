-- models/transformations/players_enhanced.sql
SELECT 
    player_id,
    name,
    IF(last_season < 2019, TRUE, FALSE) AS is_retired,
    current_club_id,
    IFNULL(country_of_citizenship, 'Unknown Nationality') AS nationality,
    position,
    CASE 
        WHEN foot IN ('right', 'left', 'both') THEN foot
        ELSE 'Unknown Foot'
    END AS foot,
    height_in_cm,
    current_club_name,
    market_value_in_eur,
    highest_market_value_in_eur,
    FLOOR(DATE_DIFF(CURRENT_DATE, DATE(SAFE.TIMESTAMP(date_of_birth)), YEAR)) AS age
FROM 
    `football-data-analytics.football_data_analytics_dataset.players`