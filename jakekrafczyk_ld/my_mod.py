import pandas as pd


def set_display(columns, rows):
    """"
    This function sets the maximum number of columns
    and rows that display when printing a function.

    """
    pd.set_option('display.max_columns', columns)
    pd.set_option('display.max_rows', rows)


def list_to_column(DataFrame, list, column_name):
    """"
    This allows you to take a list and convert it into
    a column in the designated pandas DataFrame.

    """
    DataFrame[column_name] = list
    return DataFrame


class Food():
    def __init__(self, name, color, macro, price_range):
        self.name = name
        self.color = color
        self.macro = macro
        self.price_range = price_range

    def eat(self):
        print("I am eating ", self.name)

    @property
    def describe(self):
        return f"{self.price_range} {self.macro}"


class Meat(Food):  # Meat class inherits from the Food class
    def __init__(self, name, color, macro, price_range):
        super().__init__(name, color, macro, price_range)

    def cost(self):
        print("This meat is ", self.price_range)


if __name__ == "__main__":

    meal = Meat("Chicken", "White", "Protein", "Cheap")
    meal.eat()
    meal.describe
    print(meal.name, " is my favorite ", meal.macro)
