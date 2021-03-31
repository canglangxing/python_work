filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} dose not exist.")
else:
    words = content.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
