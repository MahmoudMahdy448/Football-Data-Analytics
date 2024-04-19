if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    return data

# Convert 'appearance_id' to int
    data['appearance_id'] = data['appearance_id'].astype(int)

    # Remove records where 'minutes_played' > 120
    data = data[data['minutes_played'] <= 120]

    # Remove records where 'red_cards' > 1
    data = data[data['red_cards'] <= 1]

    # Remove records where 'yellow_cards' > 2
    data = data[data['yellow_cards'] <= 2]

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert output['appearance_id'].dtype == int, 'appearance_id is not of int dtype'
    assert output['minutes_played'].max() <= 120, 'There are records with minutes_played > 120'
    assert output['red_cards'].max() <= 1, 'There are records with red_cards > 1'
    assert output['yellow_cards'].max() <= 2, 'There are records with yellow_cards > 2'
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
