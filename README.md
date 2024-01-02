# COMP1516_FinalProject
This project ensures that every method and function is named as a verb, has Docstring comments, and follows good indentation and other style guidelines.


## Instruction
Create three Python files named data.py, country.py, main.py, amd test.py with the functionality as follows:
 

### data.py

A given list of tuples. Each tuple contains two elements: the name of a country and the corresponding capital city.


### country.py

**Class Definition (Country):**

Defines a class named Country to represent information about a country.


**Constructor (__init__ method):**

Takes three parameters: country_name, capital_name, and population.
Initializes instance variables country_name, capital_name, and population.
Raises a ValueError if the population is less than 2 million.


**print_details Method:**

Prints information about the country in a specific format.
Returns a string containing the details.
Raises a ValueError if the population is less than 2 million.


**birth Method:**

Simulates a population increase by adding 1 to the current population.
Prints and returns the updated population.


**death Method:**

Simulates a population decrease by subtracting 1 from the current population.
Prints and returns the updated population.


**disaster Method:**

Simulates a population change based on the country's current population.
If the population is 100 million or higher, it subtracts 100 million; otherwise, it sets the population to 0.
Prints and returns the updated population.


### main.py

**Import:**

Imports data about countries and capitals from an external file (countries_and_capitals).
Imports the Country class and the random module.


**Initialization:**

Converts the original tuple data into a list of tuples (list_countries_and_capitals).
Initializes an empty list called all_countries to store instances of the Country class.


**Create Country Objects:**

Iterates over the list of countries and capitals, creating Country objects for each entry.
The Country objects are initialized with a title-cased country name, an uppercase capital name, and a random population ranging from 1 million to 1 billion.


**Print Country Details:**

Iterates over the list of created Country objects and calls the print_details method for each, displaying information about the country's capital, population, and potential errors.


**Population Simulation Loops:**

Three separate loops simulate different population scenarios for each country:

	Birth Loop: Calls the birth() method for each country, simulating population growth.
	Death Loop: Calls the death() method for each country, simulating population decline.
	Disaster Loop: Calls the disaster() method for each country, simulating population changes based on a disaster scenario.


**Exception Handling (ValueError):**

If a ValueError occurs during any population modification operation (e.g., birth, death, disaster), it prints an error message.


### test.py

**First Loop (normal):**

It creates instances of the Country class for each country in the data.
Calls print_details(), birth(), death(), and disaster() methods for each country, displaying information about the country's capital, population changes (birth, death, disaster), and potential errors.


**Second Loop (birth):**

It simulates a scenario where each country experiences a population increase (birth).
Calls birth() and print_details() methods for each country, displaying updated population information.


**Third Loop (death):**

It simulates a scenario where each country experiences a population decrease (death).
Calls death() and print_details() methods for each country, displaying updated population information.


**Fourth Loop (disaster):**

It simulates a scenario where each country experiences a disaster, either reducing the population by 100 million for larger countries or setting it to zero for smaller countries.
Calls disaster() and print_details() methods for each country, displaying updated population information.


Exception Handling (ValueError):

If a ValueError occurs during any population modification operation (e.g., birth, death, disaster), it prints an error message.
