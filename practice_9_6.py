class Restaurant:
    """模拟餐厅信息"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐厅类型"""
        print(f"{self.restaurant_name.title()} is a restaurant specializing in {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

class IceCreamStand(Restaurant):
    """docstring for ClassName"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['milk', 'chocolate', 'strawbarry']

    def display_ice_cream(self):
        print("There are many flavors of ice cream:")
        for flavor in self.flavors:
            print(flavor)


Zhongxugao = IceCreamStand('Zhongxugao', 'Ice cream')
Zhongxugao.display_ice_cream()