import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_multiple_apis(*args, **kwargs):
    """
    Template for loading data from multiple APIs
    """
    urls = ['https://storage.googleapis.com/football-data-analytics-bucket/appearances.csv',
            'https://storage.googleapis.com/football-data-analytics-bucket/players.csv',
            'https://storage.googleapis.com/football-data-analytics-bucket/clubs.csv',
            'https://storage.googleapis.com/football-data-analytics-bucket/competitions.csv',
            'https://storage.googleapis.com/football-data-analytics-bucket/player_valuations.csv']

    identifiers = ['appearances', 'players', 'clubs', 'competitions', 'player_valuations']

    dtypes_dict = {
        identifiers[0]: {
        'appearance_id': 'str',
        'game_id': 'int64',
        'player_id': 'int64',
        'player_club_id': 'int64',
        'player_current_club_id': 'int64',
        'date': 'datetime64[ns]',
        'player_name': 'str',
        'competition_id': 'str',
        'yellow_cards': 'int64',
        'red_cards': 'int64',
        'goals': 'int64',
        'assists': 'int64',
        'minutes_played': 'int64'
        },
        identifiers[1]: {
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
        },
        identifiers[2]: {
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
        },
        identifiers[3]: {
        'competition_id': 'str',
        'name': 'str',
        'sub_type': 'str',
        'country_id': 'int64',
        'country_name': 'str',
        'domestic_league_code': 'str',
        'is_major_national_league': 'bool'
        },
        identifiers[4]: {
        'player_id': 'int64',
        'date': 'datetime64[ns]',
        'market_value_in_eur': 'float64',
        'current_club_id': 'int64',
        'player_club_domestic_competition_id': 'str'
        },
    }

    date_columns = {
        identifiers[0]: ['date'],
        identifiers[1]: ['date_of_birth'],
        identifiers[2]: [],
        identifiers[3]: [],
        identifiers[4]: ['date']  
    }

    data = {}

    for url, identifier in zip(urls, identifiers):
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text), sep=',', parse_dates=date_columns[identifier])
        df = df.astype(dtypes_dict[identifier], errors='ignore')  # convert data types
        data[identifier] = df

    return data