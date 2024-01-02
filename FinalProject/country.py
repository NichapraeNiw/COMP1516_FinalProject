# Nattanicha Nilsriphaiwan

from data import countries_and_capitals


class Country:
    """
    This file contains the Country class.
    Define a constructor that takes three parameters:
      - a country name
      - a capital name
      - a population
    In the constructor, assign the parameter values to the instance variables.
    Unless the population is less than 2 million; in that case raise a ValueError with a message in the format of
    (“Population 1057988 is too low”).
    """
    def __init__(self, country_name, capital_name, population):
        self.country_name = country_name
        self.capital_name = capital_name
        self.population = population

    def print_details(self):
        """
        This method prints data in this format: "The capital of Canada (pop. 1234567) is OTTAWA".
        :return: the detail of country with the format
        :raise: ValueError if population lower than 2 million
        """
        detail = f"The capital of {self.country_name} (pop. {self.population}) is {self.capital_name}"
        print(detail)
        if self.population < 2000000:
            raise ValueError(f"Population {self.population} is too low")
        return detail

    def birth(self):
        """
        This method adds 1 to the object’s own self’s population
        :return: population added by one
        """
        birth = self.population + 1
        print(birth)
        return birth

    def death(self):
        """
        This method subtracts 1 from the object’s own self’s population
        :return: population subtracted by one
        """
        death = self.population - 1
        print(death)
        return death

    def disaster(self):
        """
        For countries with a population of 100 million or higher, this method subtracts 100 million from the population.
        For smaller countries, it sets the population to 0.
        :return: amount of population subtracted with 100 million or 0 if population lower than 100 million
        """
        disaster = self.population
        if disaster >= 100000000:
            disaster = disaster - 100000000
        else:
            disaster = 0
        print(disaster)
        return disaster
