#import file_operation
from util.file_operation import save_to_file, read_file
#from util2.say_hello import say_hello

file_name = 'names.txt'

save_to_file('Rolf', file_name)


content = read_file(file_name)
print(content)

