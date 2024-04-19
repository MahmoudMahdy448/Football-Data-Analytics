-- player_dashboard.sql
SELECT
    pv.*,
    p.position,
    p.foot,
    p.height_in_cm
FROM
    {{ ref('player_value') }} pv
JOIN
    `football-data-analytics.football_data_analytics_dataset`.player_data p
ON
    pv.player_id = p.player_id
