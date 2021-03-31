from random import sample

words = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D']
word = sample(words,4)

my_ticket = []
times = 0
while my_ticket != word:
    my_ticket = sample(words,4)
    times +=1

print(times)