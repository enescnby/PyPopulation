"""
Population API for 1960-2020 population datas.

Data Source: The World Bank (https://data.worldbank.org/indicator/SP.POP.TOTL)
"""
import pandas

class PopulationAPI:

    """
    Population API for 1960-2020 population datas.

    Data Source: The World Bank (https://data.worldbank.org/indicator/SP.POP.TOTL)
    """

    class DataError(Exception):

        def __init__(self, msg) -> None:
            super().__init__()
            self.msg = msg

        def __str__(self) -> str:
            return self.msg

    def __init__(self, excel_file_name: str = 'population_data.xls') -> None:
        self.file_name = excel_file_name
        self.dataframe = pandas.read_excel(self.file_name)

    def list_countries(self) -> list:
        """
        Returns the list of countries.
        """

        return list(self.dataframe.loc[:, 'Country'])

    def get_population(self, country: str, year: str | int) -> int | None:
        """
        Returns the population of given country in given year.\n
        If the given country or the given year does not exist in data frame, DataError occurs.\n
        Example of calling:\n
            x = PopulationAPI( )\n
            x.get_population( "Turkiye", 1980 )
        """
        try:
            int(year)
        except ValueError:
            raise ValueError("The year must be an integer.")
        year = str(year)

        try:
            data_series = self.dataframe.loc[self.dataframe['Country'] == country.lower(
            ), year]
        except KeyError:
            raise PopulationAPI.DataError("There is no data in " + year)

        try:
            data = int(data_series)
        except ValueError:
            raise PopulationAPI.DataError(
                "There is no data in " + country + " in " + year + " or can not fetching.")
        except TypeError:
            raise NameError("Invalid country name.")
        return data

    def get_population_list(self, country: str, years: tuple | list) -> list:
        """
        Returns the list of populations the given country between the given years.\n
        If the given country does not exist in data frame, returns empty list.\n
        If one of the given years does not exist in data frame, DataError occurs.\n
        Example of calling:\n
            x = PopulationAPI( )\n
            x.get_population_list( "Turkiye", (1960, 1980) )
        """
        try:
            data_series = self.dataframe.loc[self.dataframe['Country'] == country.lower(), str(years[0]):str(years[1])].astype(int)
        except KeyError:
            raise PopulationAPI.DataError("There is no data in given year.")
        return data_series.values.flatten().tolist()
