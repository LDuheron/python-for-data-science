import matplotlib.pyplot as plt
from load_csv import load


def main():
    try:
        dataFrame = load("../data/life_expectancy_years.csv")
        France = dataFrame.loc['France']

        plt.plot(France)
        plt.title('France Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.xticks(ticks=France.index[::40])
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
