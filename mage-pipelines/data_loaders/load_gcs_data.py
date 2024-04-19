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
def load_from_google_cloud_storage(*args, **kwargs):
    """
    Template for loading data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'football-data-analytics-bucket'
    object_key = 'appearances.csv'
    appearances_dtypes = {
        'appearance_id': str,  # Change this to str
        'game_id': pd.Int64Dtype(),
        'player_id': pd.Int64Dtype(),
        'player_club_id': pd.Int64Dtype(),
        'player_current_club_id': pd.Int64Dtype(),
        'player_name': str,
        'competition_id': str,  # Change this to str
        'yellow_cards': pd.Int64Dtype(),
        'red_cards': pd.Int64Dtype(),
        'goals': pd.Int64Dtype(),
        'assists': pd.Int64Dtype(),
        'minutes_played': pd.Int64Dtype()
    }
    # Load the data
    df = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).load(
        bucket_name,
        object_key,
        dtype=appearances_dtypes,  # Specify data types
        parse_dates=['date']  # Parse dates
    )

    return df