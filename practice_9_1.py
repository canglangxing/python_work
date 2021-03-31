class Restaurant(object):
    """模拟餐厅信息"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐厅类型"""
        print(f"{self.restaurant_name.title()} is a restaurant specializing in {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

Yi_restaurant = Restaurant('Yi', 'Sichuan cuisine')
print(Yi_restaurant.restaurant_name)
print(Yi_restaurant.cuisine_type)
Yi_restaurant.describe_restaurant()
Yi_restaurant.open_restaurant()