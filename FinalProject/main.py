# Nattanicha Nilsriphaiwan

from data import countries_and_capitals
from country import Country
import random


def main():
    try:
        list_countries_and_capitals = list(countries_and_capitals)
        all_countries = []
        for i in range(0, len(countries_and_capitals)):
            all_countries.append(Country(list_countries_and_capitals[i][0].title(),
                                         list_countries_and_capitals[i][1].upper(),
                                         random.randint(1000000, 1000000000)))
        # print detail
        for country in all_countries:
            country.print_details()

        # loop through the list again, calling birth() for each object and calling print_details()
        for country in all_countries:
            country.birth()
            country.print_details()

        # loop through the list again, calling death() for each object and calling print_details()
        for country in all_countries:
            country.death()
            country.print_details()
        # loop through the list again, calling disaster() for each object and calling print_details()
        for country in all_countries:
            country.disaster()
            country.print_details()
    except ValueError as e:
        print("oops")
        print(e)


if __name__ == '__main__':
    main()
