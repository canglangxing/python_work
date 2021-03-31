def city_country(city, country):
    full_city = f'"{city}, {country}"'
    return full_city.title()

famous_city = city_country('santiago', 'chile')
print(famous_city)

famous_city = city_country('berlin', 'germany')
print(famous_city)

famous_city = city_country('florence', 'italy')
print(famous_city)