"""
Population API for 1960-2021 population datas.

Data Source: The World Bank (https://data.worldbank.org/indicator/SP.POP.TOTL)
"""
import pandas, numpy


class PopulationAPI:

    class DataError(Exception):

        def __init__(self, msg) -> None:
            super().__init__()
            self.msg = msg

        def __str__(self) -> str:
            return self.msg

    def __init__(self, excel_file_name: str = 'population_data.xls') -> None:
        self.file_name = excel_file_name
        self.dataframe = pandas.read_excel(self.file_name)

    def get_population(self, country: str, year: str | int) -> int | None:

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

        data_series = self.dataframe.loc[self.dataframe['Country'] == country.lower(), str(years[0]):str(years[1])].astype(int)
        return data_series.values.flatten().tolist()

x = PopulationAPI()
lst = x.get_population_list('Turkiye', (1960,1970))
print(lst)
