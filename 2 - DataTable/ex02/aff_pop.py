import matplotlib.pyplot as plt
from load_csv import load


def normalize_data(value) -> float:
    if value.endswith('k'):
        normalized_value = float(value[:-1]) * 1000
    elif value.endswith('M'):
        normalized_value = float(value[:-1]) * 1000000
    else:
        normalized_value = float(value)
    return normalized_value


def main():
    try:
        dataFrame = load("../data/population_total.csv")
        Belgium = dataFrame.loc['Belgium'].map(normalize_data)
        France = dataFrame.loc['France'].map(normalize_data)

        plt.figure()
        plt.plot(Belgium[:'2050'], label='Belgium')
        plt.plot(France[:'2050'], label='France')

        plt.title('Populations Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.xticks(ticks=France[:'2050'].index[::40])
        plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])

        plt.legend()
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
