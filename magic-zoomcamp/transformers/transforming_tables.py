if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd



# @transformer
# def transform(data, *args, **kwargs):
#     players = pd.DataFrame(data['players'])
    
    # print(data['players'])
    # print(data['players'].dtypes)
    # return data['players']
@transformer
def transform(data, *args, **kwargs):
    


    players = pd.DataFrame(data['players'])
    clubs = pd.DataFrame(data['clubs'])
    competitions = pd.DataFrame(data['competitions'])
    player_valuations = pd.DataFrame(data['player_valuations'])
    print(type(players))


    # Transformations for players
    players = players.drop(columns=['first_name', 'last_name','player_code','country_of_birth','current_club_domestic_competition_id','agent_name','contract_expiration_date','image_url', 'url','city_of_birth'])
    players['country_of_citizenship'].fillna('unknown_citizenship', inplace=True)
    mask = players['date_of_birth'].isnull() & (players['last_season'] < 2023)
    players = players[~mask]
    players.loc[players['sub_position'].isnull(), 'sub_position'] = 'unknown_sub_position'
    players.loc[players['foot'].isnull(), 'foot'] = 'unknown_foot'
    players["date_of_birth"] = pd.to_datetime(players["date_of_birth"])
    players = players.astype({
        'player_id': 'int64',
        'name': 'str',
        'last_season': 'int64',
        'current_club_id': 'int64',
        'country_of_citizenship':'str',
        'date_of_birth': 'datetime64[ns]',
        'sub_position': 'str',
        'position': 'str',
        'foot': 'str',
        'height_in_cm': 'float64',
        'current_club_name': 'str',
        'market_value_in_eur': 'float64',
        'highest_market_value_in_eur': 'float64'
    })

    # Transformations for clubs
    clubs = clubs.drop(columns=['club_code','last_season','coach_name','filename', 'url','total_market_value'])
    clubs = clubs.astype({
        'club_id': 'int64',
        'name': 'str',
        'domestic_competition_id': 'str',
        'squad_size': 'int64',
        'average_age': 'float64',
        'foreigners_number': 'int64',
        'foreigners_percentage': 'float64',
        'national_team_players': 'int64',
        'stadium_name': 'str',
        'stadium_seats': 'int64',
        'net_transfer_record': 'str'
    })

    # Transformations for competitions
    competitions = competitions.drop(columns=['competition_code','url', 'type','confederation'])
    competitions = competitions.astype({
        'competition_id': 'str',
        'name': 'str',
        'sub_type': 'str',
        'country_id': 'int64',
        'country_name': 'str',
        'domestic_league_code': 'str',
        'is_major_national_league': 'bool'
    })

    # Transformations for player_valuations
    player_valuations = player_valuations.astype({
        'player_id': 'int64',
        'date': 'datetime64[ns]',
        'market_value_in_eur': 'float64',
        'current_club_id': 'int64',
        'player_club_domestic_competition_id': 'str'
    })

    # Creating datetime_dim table
    datetime_dim = player_valuations[['date']].reset_index(drop=True)
    datetime_dim['date'] = datetime_dim['date']
    datetime_dim['day'] = datetime_dim['date'].dt.day
    datetime_dim['month'] = datetime_dim['date'].dt.month
    datetime_dim['year'] = datetime_dim['date'].dt.year
    datetime_dim['weekday'] = datetime_dim['date'].dt.weekday
    datetime_dim['datetime_id'] = datetime_dim.index
    datetime_dim = datetime_dim[['datetime_id', 'date', 'day', 'month', 'year', 'weekday']]

    # Creating countries_dim table
    countries_dim = competitions[['country_id', 'country_name']].drop_duplicates()

    print(type(players))
    return {
        'players': players.to_dict(orient="dict"),
        'clubs': clubs.to_dict(orient="dict"),
        'competitions': competitions.to_dict(orient="dict"),
        'player_valuations': player_valuations.to_dict(orient="dict"),
        'datetime_dim': datetime_dim.to_dict(orient="dict"),
        'countries_dim': countries_dim.to_dict(orient="dict")
    }