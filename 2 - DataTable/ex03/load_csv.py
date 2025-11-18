import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV dataset from the given path and print its dimensions.

    path (str): path to the dataset to load.

Returns:
    pd.DataFrame: Loaded dataset as a pandas DataFrame.
"""
    try:
        assert isinstance(path, str), "Expected 'path' to be str"

        dataFrame = pd.read_csv(path, index_col=0)
        print(f"Loading dataset of dimensions {dataFrame.shape}")
        return dataFrame

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")
