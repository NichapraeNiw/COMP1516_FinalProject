# Nattanicha Nilsriphaiwan

from data import countries_and_capitals
from country import Country


def main():
    try:
        all_countries = []
        for i in range(0, len(countries_and_capitals)):
            all_countries.append([countries_and_capitals[i][0], countries_and_capitals[i][1]])
        # If there are no exceptions:
        # loop through all the countries list and call each object’s print_details().
        print("------------------------------------normal------------------------------------")
        for i in range(0, len(countries_and_capitals)):
            c = Country(countries_and_capitals[i][0], countries_and_capitals[i][1], 100000000)
            print(c.print_details())
            print(c.birth())
            print(c.death())
            print(c.disaster())
        # loop through the list again, calling birth() for each object and calling print_details().
        # note that each country’s population should be 1 higher than the previous loop.
        print("------------------------------------birth------------------------------------")
        for i in range(0, len(countries_and_capitals)):
            if i == 0:
                c = Country(countries_and_capitals[i][0], countries_and_capitals[i][1], 100000000)
                print(c.birth())
                print(c.print_details())
            else:
                c = Country(countries_and_capitals[i][0], countries_and_capitals[i][1], 100000000 + i)
                print(c.birth())
                print(c.print_details())
        # loop through the list again, calling death() for each object and calling print_details().
        # note that each country’s population should be 1 lower than the previous loop.
        print("------------------------------------death------------------------------------")
        for i in range(0, len(countries_and_capitals)):
            if i == 0:
                c = Country(countries_and_capitals[i][0], countries_and_capitals[i][1], 100000000)
                print(c.death())
                print(c.print_details())
            else:
                c = Country(countries_and_capitals[i][0], countries_and_capitals[i][1], 100000000 - i)
                print(c.death())
                print(c.print_details())
        # loop through the list again, calling disaster() for each object and calling print_details().
        # note that each country’s population should be 100 million lower than the previous loop (for big countries).
        # or country’s population should be zero(for countries that previously had populations of 100 million or lower).
        print("------------------------------------disaster------------------------------------")
        for i in range(0, len(countries_and_capitals)):
            if i == 0:
                c = Country(countries_and_capitals[i][0], countries_and_capitals[i][1], 100000000)
                print(c.disaster())
                print(c.print_details())
            else:
                c = Country(countries_and_capitals[i][0], countries_and_capitals[i][1], 100000000 - i)
                print(c.disaster())
                print(c.print_details())

        print()

    except ValueError as e:
        print("oops")
        print(e)


if __name__ == '__main__':
    main()
