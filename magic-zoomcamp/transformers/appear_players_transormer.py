if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    """
    Template for transforming data
    """
    # Access each DataFrame using its identifier
    appearance = data['appearances']
    players = data['players']


    appearance.dropna(inplace=True)
    players['country_of_citizenship'].fillna('unknown_citizenship', inplace=True)

    mask = players['date_of_birth'].isnull() & (players['last_season'] < 2023)
    players = players[~mask]

    players.loc[players['sub_position'].isnull(), 'sub_position'] = 'unknown_sub_position'
    players.loc[players['foot'].isnull(), 'foot'] = 'unknown_foot'

    players = players.drop(columns=['first_name', 'last_name', 'player_code', 'country_of_birth', 'current_club_domestic_competition_id', 'agent_name', 'contract_expiration_date', 'image_url', 'url', 'city_of_birth'])

    appearance = appearance[appearance['minutes_played'] <= 120]
    appearance = appearance[appearance['red_cards'] <= 1]
    appearance = appearance[appearance['yellow_cards'] <= 2]

    # Store the transformed DataFrames back in the dictionary
    data['appearances'] = appearance
    data['players'] = players

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert 'appearances' in output, 'The appearances DataFrame is missing'
    assert 'players' in output, 'The players DataFrame is missing'
    assert output['appearances']['date'].dtype == 'datetime64[ns]', 'The date column in the appearances DataFrame is not datetime'
    assert output['players']['date_of_birth'].dtype == 'datetime64[ns]', 'The date_of_birth column in the players DataFrame is not datetime'
    assert output['appearances'].isnull().sum().sum() == 0, 'The appearances DataFrame contains null values'
    assert output['players']['country_of_citizenship'].isnull().sum() == 0, 'The country_of_citizenship column in the players DataFrame contains null values'
    assert output['players']['sub_position'].isnull().sum() == 0, 'The sub_position column in the players DataFrame contains null values'
    assert output['players']['foot'].isnull().sum() == 0, 'The foot column in the players DataFrame contains null values'
    assert 'first_name' not in output['players'].columns, 'The first_name column is still in the players DataFrame'
    assert output['appearances']['minutes_played'].max() <= 120, 'The minutes_played column in the appearances DataFrame contains values greater than 120'
    assert output['appearances']['red_cards'].max() <= 1, 'The red_cards column in the appearances DataFrame contains values greater than 1'
    assert output['appearances']['yellow_cards'].max() <= 2, 'The yellow_cards column in the appearances DataFrame contains values greater than 2'
