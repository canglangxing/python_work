with open('learning_python.txt') as file_object:
    contents = file_object.read()
    new_cintents = contents.replace('python', 'C')
    print(new_cintents)