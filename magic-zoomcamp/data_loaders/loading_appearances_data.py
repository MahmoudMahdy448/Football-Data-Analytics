import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://storage.googleapis.com/football-data-analytics-bucket/appearances.csv'
    response = requests.get(url)

    appearance_dtypes = {
        'appearance_id': 'str',
        'game_id': 'int64',
        'player_id': 'int64',
        'player_club_id': 'int64',
        'player_current_club_id': 'int64',
        
        'player_name': 'str',
        'competition_id': 'str',
        'yellow_cards': 'int64',
        'red_cards': 'int64',
        'goals': 'int64',
        'assists': 'int64',
        'minutes_played': 'int64'
    }

    df = pd.read_csv(io.StringIO(response.text), sep=',', dtype=appearance_dtypes, parse_dates=['date'])

    return df

@test
def test_dtypes(output, *args) -> None:
    """
    Test if the output DataFrame has the expected data types.
    """
    expected_dtypes = {
        'appearance_id': 'object',
        'game_id': 'int64',
        'player_id': 'int64',
        'player_club_id': 'int64',
        'player_current_club_id': 'int64',
        'date': 'datetime64[ns]',
        'player_name': 'object',
        'competition_id': 'object',
        'yellow_cards': 'int64',
        'red_cards': 'int64',
        'goals': 'int64',
        'assists': 'int64',
        'minutes_played': 'int64'
    }

    for column, dtype in expected_dtypes.items():
        assert output[column].dtype == dtype, f"The dtype of column '{column}' is not '{dtype}'"
