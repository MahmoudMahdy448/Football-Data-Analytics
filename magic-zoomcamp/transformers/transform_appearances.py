if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.
    """
    # Specify your transformation logic here
    df["date"] = pd.to_datetime(df["date"])
    # Dropping nulls
    df.dropna(inplace=True)
    # Filtering out outliers in minutes_played, yellow and red_cards
    df = df[df['minutes_played'] <= 120]
    df = df[df['red_cards'] <= 1]
    df = df[df['yellow_cards'] <= 2]
    # Checking 
    print('Max minutes_played:', df['minutes_played'].max())
    print('Max red_cards:', df['red_cards'].max())
    print('Max yellow_cards:', df['yellow_cards'].max())

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
