import json

file = open('json_data.json', 'r')
file_contents = json.load(file) #dictionary
file.close()

print(file_contents['friends'][0])

cars = [
    {
        'make': 'Ford', 'model': 'Fiesta'
    },
    {
        'make': 'Ford', 'model': 'Focus'
    }
]

file = open('json_cars.json', 'w')
json.dump(cars, file)
file.close()