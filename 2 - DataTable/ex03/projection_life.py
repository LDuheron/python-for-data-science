import matplotlib.pyplot as plt
from load_csv import load


def normalize_data(value) -> float:
    """Normalize data.
Args:
    value: The value to normalize.

Returns:
    float : The value normalized."""
    if isinstance(value, str) and value.endswith('k'):
        normalized_value = float(value[:-1]) * 1000
    elif isinstance(value, str) and value.endswith('M'):
        normalized_value = float(value[:-1]) * 1000000
    else:
        normalized_value = float(value)
    return normalized_value


def main():
    try:
        full_life_expectancy = load(
            "../data/life_expectancy_years.csv")
        full_income = load(
            "../data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )

        target_year = "1900"
        life_expectancy = full_life_expectancy[target_year].map(normalize_data)
        income = full_income[target_year]

        plt.xscale("log")

        plt.scatter(income, life_expectancy)
        plt.title(target_year)
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.xticks([300, 1000, 10_000], ["300", "1k", "10k"])
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
