csv_file = open('csv_data.csv', 'r')
lines = csv_file.readlines()
csv_file.close()

lines = [line.strip() for line in lines[1:]]   # ignore the first inside  line line comprehension
for line in lines:
    person_data = line.split(',')
    name = person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree = person_data[3]
    print(f'{name.title()} is {age} studying {degree.capitalize()} at {university.title()}')