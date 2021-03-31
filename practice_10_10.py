with open('little_women.txt', encoding = 'utf-8') as f:
    content = f.read()
    times = content.lower().count('the ')
    print(times)