people = [
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Cho', 'house': 'Ravenclaw'},
    {'name': 'Draco', 'house': 'Slytherin'}
]

people.sort(key=lambda x: x['name']) # or 'person' instead of 'x'

print(people)
