def save_to_file(content, file):
    with open(file, 'w') as file:
        file.write(content)

def read_file(file):
    with open(file, 'r') as file:
        return file.read()
