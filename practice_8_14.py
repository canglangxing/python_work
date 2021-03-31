def make_car(manufacturer, model, **car_info):
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)