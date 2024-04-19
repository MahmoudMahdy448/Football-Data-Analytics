if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Transformer block for players data.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Transformed DataFrame
    """
    import pandas as pd

    # Convert 'date_of_birth' and 'contract_expiration_date' to datetime format
    data['date_of_birth'] = pd.to_datetime(data['date_of_birth'])
    data['contract_expiration_date'] = pd.to_datetime(data['contract_expiration_date'])

    # Convert categorical columns to category data type
    for col in ['country_of_birth', 'city_of_birth', 'country_of_citizenship', 'sub_position', 'position', 'foot', 'current_club_name', 'current_club_domestic_competition_id']:
        data[col] = data[col].astype('category')

    # Handle missing values in 'height_in_cm'
    data['height_in_cm'].fillna(round(data['height_in_cm'].mean()), inplace=True)

    # Convert 'market_value_in_eur' and 'highest_market_value_in_eur' to numeric data type
    data['market_value_in_eur'] = pd.to_numeric(data['market_value_in_eur'])
    data['highest_market_value_in_eur'] = pd.to_numeric(data['highest_market_value_in_eur'])

    # Drop 'image_url' and 'url' columns
    data.drop(['image_url', 'url'], axis=1, inplace=True)

    return data

@test
def test_output(output, *args) -> None:
    """
    Test the output of the block.
    """
    import pandas as pd

    assert output is not None, 'The output is undefined'
    assert pd.api.types.is_datetime64_ns_dtype(output['date_of_birth']), 'date_of_birth is not datetime dtype'
    assert pd.api.types.is_datetime64_ns_dtype(output['contract_expiration_date']), 'contract_expiration_date is not datetime dtype'
    assert pd.api.types.is_categorical_dtype(output['country_of_birth']), 'country_of_birth is not category dtype'
    assert pd.api.types.is_integer_dtype(output['height_in_cm']), 'height_in_cm is not integer dtype'
    assert pd.api.types.is_numeric_dtype(output['market_value_in_eur']), 'market_value_in_eur is not numeric dtype'
    assert pd.api.types.is_numeric_dtype(output['highest_market_value_in_eur']), 'highest_market_value_in_eur is not numeric dtype'
    assert 'image_url' not in output.columns, 'image_url column is not dropped'
    assert 'url' not in output.columns, 'url column is not dropped'