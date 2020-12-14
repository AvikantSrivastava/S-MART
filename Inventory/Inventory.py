import datetime


class Inventory():
    def __init__(self, id):
        self.id = id

    def sell(self, item_name, quantity):
        pass

    def get_Sales(self, date):
        pass

    def get_Profit(self, date):
        pass


if __name__ == '__main__':
    inventory_id = 'abcd'
    inventory = Inventory(inventory_id)

    # To get net profit of Day X by subtracting Sales from Day X-1
    todaysDate = datetime.date()
    todays_profit = inventory.get_Profit(todaysDate)

    # To get Sales by providing the Date as a parameter.
    todaysDate = datetime.date()
    todays_sales_data = inventory.get_Sales(todaysDate)

    # To sell and Item and update in inventory.
    inventory.sell('shampoo', 15)
    inventory.sell('beer', 26)
    inventory.sell('chips', 47)

    

