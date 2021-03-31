from random import sample

words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D']
winning_words = sample(words,4)

winning = ''
for winning_word in winning_words:
    winning += winning_word
print(f"As long as the ticket is {winning}, you hit the jackpot.")
print(winning)