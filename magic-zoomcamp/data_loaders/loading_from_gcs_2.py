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
    urls = ['https://storage.googleapis.com/football-data-analytics-bucket/clubs.csv',
            'https://storage.googleapis.com/football-data-analytics-bucket/competitions.csv',
            'https://storage.googleapis.com/football-data-analytics-bucket/player_valuations.csv']

    identifiers = [ 'clubs', 'competitions', 'player_valuations']

    dtypes_dict = {
        identifiers[0]: {
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
        identifiers[1]: {
        'competition_id': 'str',
        'name': 'str',
        'sub_type': 'str',
        'country_id': 'int64',
        'country_name': 'str',
        'domestic_league_code': 'str',
        'is_major_national_league': 'bool'
        },
        identifiers[2]: {
        'player_id': 'int64',
        'date': 'datetime64[ns]',
        'market_value_in_eur': 'float64',
        'current_club_id': 'int64',
        'player_club_domestic_competition_id': 'str'
        },
    }

    date_columns = {
        identifiers[0]: [],
        identifiers[1]: [],
        identifiers[2]: ['date']  
    }

    data = {}

    for url, identifier in zip(urls, identifiers):
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text), sep=',', parse_dates=date_columns[identifier])
        df = df.astype(dtypes_dict[identifier], errors='ignore')  # convert data types
        data[identifier] = df

    return data