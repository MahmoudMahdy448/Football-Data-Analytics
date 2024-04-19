-- player_performance.sql
SELECT
    player_id,
    SUM(goals) AS total_goals,
    SUM(assists) AS total_assists,
    SUM(yellow_cards) AS total_yellow_cards,
    SUM(red_cards) AS total_red_cards,
    SUM(minutes_played) AS total_minutes_played
FROM
    football_data_analytics_dataset.appearances_data
GROUP BY
    player_id
