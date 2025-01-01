def write_file(file_name, file_content):
    text1 = f"{file_name}.txt"
    with open(text1, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    text1 = f"{file_name}.txt"
    with open(text1, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    text1 = f"{file_name}.txt"
    with open(text1, 'r') as file:
        return file.read()
    
# Example usage
write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")
content = read_file(file_name="logfile")
print(content)
