import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV dataset from the given path and print its dimensions.

    path (str): path to the dataset to load.

Returns:
    pd.DataFrame: Loaded dataset as a pandas DataFrame.
"""
    try:
        assert isinstance(path, str), "Expected 'path' to be str"

        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")

        return df

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")
