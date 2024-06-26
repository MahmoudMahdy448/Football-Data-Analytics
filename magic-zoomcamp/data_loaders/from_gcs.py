import io
import pandas as pd
import requests
import json

@data_loader
def load_data_from_multiple_apis(*args, **kwargs):
    """
    Template for loading data from multiple APIs
    """
    urls = [
        'https://storage.googleapis.com/football-data-analytics-bucket/players.csv',
        'https://storage.googleapis.com/football-data-analytics-bucket/clubs.csv',
        'https://storage.googleapis.com/football-data-analytics-bucket/competitions.csv',
        'https://storage.googleapis.com/football-data-analytics-bucket/player_valuations.csv'
    ]

    identifiers = ['players', 'clubs', 'competitions', 'player_valuations']

    dtypes_dict = {
        identifiers[0]: {
            'player_id': 'int64',
            'name': 'str',
            'last_season': 'int64',
            'current_club_id': 'int64',
            'country_of_citizenship': 'str',
            'date_of_birth': 'datetime64[ns]',
            'sub_position': 'str',
            'position': 'str',
            'foot': 'str',
            'height_in_cm': 'float64',
            'current_club_name': 'str',
            'market_value_in_eur': 'float64',
            'highest_market_value_in_eur': 'float64'
        },
        identifiers[1]: {
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
        identifiers[2]: {
            'competition_id': 'str',
            'name': 'str',
            'sub_type': 'str',
            'country_id': 'int64',
            'country_name': 'str',
            'domestic_league_code': 'str',
            'is_major_national_league': 'bool'
        },
        identifiers[3]: {
            'player_id': 'int64',
            'date': 'datetime64[ns]',
            'market_value_in_eur': 'float64',
            'current_club_id': 'int64',
            'player_club_domestic_competition_id': 'str'
        },
    }

    date_columns = {
        identifiers[0]: ['date_of_birth'],
        identifiers[1]: [],
        identifiers[2]: [],
        identifiers[3]: ['date']
    }

    data_dict = {}

    for url, identifier in zip(urls, identifiers):
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text), sep=',', parse_dates=date_columns[identifier])
        df = df.astype(dtypes_dict[identifier], errors='ignore')  # convert data types
        print(f"Type of {identifier}: {type(df)}")  # print the type of df
        data_dict[identifier] = df
    

    return data_dict
    
