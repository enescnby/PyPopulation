"""
Population API for 1960-2021 population datas.

Data Source: The World Bank (https://data.worldbank.org/indicator/SP.POP.TOTL)
"""

import pandas

class PopulationAPI:

    def __init__(self, excel_file_name: str = 'population_data.xls') -> None:
        self.file_name = excel_file_name
        self.dataframe = pandas.read_excel(self.file_name)

    def get_population(self, country: str, year: str | int) -> int | None:
        year = str(year)
        try:
            data_series = self.dataframe.loc[self.dataframe['Country'] == country.lower(), year]
        except KeyError:
            print("There is no data in " + year)
            return None
        try:
            data = int(data_series)
        except ValueError:
            print("There is no data in " + country + " in " + year + " or can not fetching." )
            return None
        except TypeError:
            print("Invalid country name.")
            return None
        return data
