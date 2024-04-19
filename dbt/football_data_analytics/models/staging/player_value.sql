-- player_value.sql
SELECT
    pp.*,
    p.name AS player_name,
    p.market_value_in_eur
FROM
    {{ ref('player_performance') }} pp
JOIN
    `football_data_analytics_dataset`.player_data p
ON
    pp.player_id = p.player_id
