def show_message(messages):
    for message in messages:
        print(message)
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)

messages = ['today is sunny day', 'today is sunday', 'today is a good day']
sent_messages = []

print(messages)
print(sent_messages)
show_message(messages)
send_messages(messages, sent_messages)
print(messages)
print(sent_messages)