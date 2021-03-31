class Restaurant(object):
    """模拟餐厅信息"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐厅类型"""
        print(f"{self.restaurant_name.title()} is a restaurant specializing in {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

    def served_people(self):
        print(f"{self.number_served} people have dined in this restaurant.")

    def set_number_served(self, served_number):
        self.number_served = served_number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


# Yi_restaurant = Restaurant('Yi', 'Sichuan cuisine')
# Yi_restaurant.describe_restaurant()
# Yi_restaurant.open_restaurant()
# Yi_restaurant.set_number_served(15)
# Yi_restaurant.increment_number_served(10)
# Yi_restaurant.served_people()