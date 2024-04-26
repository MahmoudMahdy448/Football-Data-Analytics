from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path
import pandas as pd
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    bigquery = BigQuery.with_config(ConfigFileLoader(config_path, config_profile))

    for key, value in data.items():
        table_id = f'football-data-analytics.football_data_analytics_dataset.{key}'
        bigquery.export(
            pd.DataFrame.from_dict(value),
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )