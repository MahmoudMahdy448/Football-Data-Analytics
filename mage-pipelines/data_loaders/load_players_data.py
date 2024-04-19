
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@data_loader
def load_players_data(*args, **kwargs):
    """
    Load players data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'football-data-analytics-bucket'
    object_key = 'players.csv'
    players_dtypes = {
        'player_id': pd.Int64Dtype(),
        'first_name': str,
        'last_name': str,
        'name': str,
        'last_season': pd.Int64Dtype(),
        'current_club_id': pd.Int64Dtype(),
        'player_code': str,
        'country_of_birth': str,
        'city_of_birth': str,
        'country_of_citizenship': str,
        'date_of_birth': str,  # If this is a date, use 'parse_dates' parameter in the load function
        'sub_position': str,
        'position': str,
        'foot': str,
        'height_in_cm': pd.Int64Dtype(),
        'contract_expiration_date': str,  # If this is a date, use 'parse_dates' parameter in the load function
        'agent_name': str,
        'image_url': str,
        'url': str,
        'current_club_domestic_competition_id': str,
        'current_club_name': str,
        'market_value_in_eur': float,
        'highest_market_value_in_eur': float
    }
    # Load the data
    df = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).load(
        bucket_name,
        object_key,
        dtype=players_dtypes,  # Specify data types
        parse_dates=['date_of_birth', 'contract_expiration_date']  # Parse dates if needed
    )

    return df