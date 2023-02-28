# PopulationAPI  [![Owner](https://img.shields.io/badge/owner-enescnby-blue)](https://github.com/enescnby)


Population API for 1960-2020 population datas.

Data Source: The World Bank (https://data.worldbank.org/indicator/SP.POP.TOTL)

## METHODS
1\) **list_countries**( ) -> list :
    
    Returns the list of countries that exist in data frame.
    
    Example Calling Statement:
    
      --> api = PopulationAPI()
      --> country_list = api.list_countries()
      # country_list = ["aruba", "africa eastern and southern", ... , "zimbabwe"]
      

2\) **get_population**( country: str, year: int \| str ) -> int :

    Returns the population of the given country in the given year.
    
    Example Calling Statement:
        
        --> api = PopulationAPI()
        --> population = api.get_population("Turkiye", 1980) or api.get_population("Turkiye", "1980")
    
    Possible Errors:

        - Data Error: When the user gives the year that does not exist in data frame or can not fetching, DataError occurs.
        
        - Name Error: When the user gives the invalid country name, NameErroe occurs.
        
        - ValueError: When the user gives to year parameter the other than integer, ValueError occurs.

3\) **get_population_list**( country: str, year: tuple \| list) -> list : 

    Returns the populations list of the given country between the given years.
    
    Exampe Calling Statement:
    
      --> api = PopulationAPI()
      --> pop_list = api.get_population_list("Turkiye", (1960, 1963))
      # pop_list = [Population of Turkiye in 1960, Population of Turkiye in 1962, Population of Turkiye in 1963]
      
    Possible Errors:
    
        - DataError: When the user gives the year that does not exist in data frame or can not fetching, DataError occurs.

        ! WARNING ! If the user gives the invalid country name, no error occur. Function returns the empty list.

4\) **get_percentage**( country: str, years: tuple | list) -> float :

    Returns the percentage of increase or decrease in population in the given country between the given years.
    If the population has increased, percentage is negative.
    If the population has decreased, percentage is positive.
    
    Example Calling Statemet:
    
      --> api = PopulationAPI()
      --> perc = api.get_percentage( "Turkiye", (1960,1961) )

    Possible Errors:
    
      - DataError: When the user gives the year or the country name that does not exist in data frame, DataError occurs.
      
      

> ***This project is under development.***
