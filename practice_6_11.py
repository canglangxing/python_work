cities = {
    'beijing': {
        'country': 'china',
        'population': 21536000,
        'fact': 'it is a city with a long history',
    },
    'paris': {
        'country': 'france',
        'population': 2240000,
        'fact': 'people think of it as a romantic city,'
    },
    'los angeles': {
    'country':'american',
    'population': 4086700,
    'fact': 'it is one of the most prosperous cities',
    },

}

for city, info in cities.items():
    print(f"\n{city.title()} is a city of {info['country'].title()}.")
    print(f"It has a population of {info['population']}.")
    print(info['fact'].title())