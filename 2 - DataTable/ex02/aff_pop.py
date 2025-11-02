import matplotlib.pyplot as plt
import matplotlib.ticker
from load_csv import load


def main():
    try:
        dataFrame = load("../data/population_total.csv")
        Belgium = dataFrame.loc['Belgium']
        France = dataFrame.loc['France']

        plt.figure()
        plt.plot(Belgium, label='Belgium')
        plt.plot(France, label='France')

        plt.title('Populations Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.xticks(ticks=France.index[::40])
        # plt.yticks(ticks=France.index[20:80])
        # locator = matplotlib.ticker.MultipleLocator(base=20, offset=60)
        # ax.yaxis.set_minor_locator(locator)
        # ax.yaxis.set_major_locator(locator)
        plt.legend()
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
