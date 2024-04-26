-- models/staging/players_with_appearances_high_value.sql
SELECT 
    p.name,
    p.is_retired,
    p.current_club_id,
    comp.competition_name as current_club_league,
    p.nationality,
    p.age,
    p.position,
    p.foot,
    p.height_in_cm,
    p.market_value_in_eur,
    p.highest_market_value_in_eur,
    a.minutes_played,
    a.goals,
    a.assists,
    a.yellow_cards,
    a.red_cards,
    EXTRACT(YEAR FROM a.date) as year
FROM 
    `football-data-analytics.dbt_mahmoudmahdy448.players_enhanced` p
JOIN 
    `football-data-analytics.dbt_mahmoudmahdy448.appearances_cleaned` a
ON 
    p.player_id = a.player_id
JOIN
    `football-data-analytics.dbt_mahmoudmahdy448.clubs_simplified` c
ON
    a.player_club_id = c.club_id
JOIN
    `football-data-analytics.dbt_mahmoudmahdy448.competitions_enhanced` comp
ON
    a.competition_id = comp.competition_id
WHERE 
    p.market_value_in_eur >= 15000000.0