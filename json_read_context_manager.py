import json

with  open('json_data.json', 'r') as file:
    
    file_contents = json.load(file) #dictionary

print(file_contents['friends'][0])

cars = [
    {
        'make': 'Ford', 'model': 'Fiesta'
    },
    {
        'make': 'Ford', 'model': 'Focus'
    }
]

with open('json_cars.json', 'w') as file:
    json.dump(cars, file)
