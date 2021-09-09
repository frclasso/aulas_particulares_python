import os
import json

file_path = "C:/Users/fabio.classo/Downloads/fabio/aulas_python/aulas_particulares_python/luiza_camilo/aula05"

os.chdir(file_path)


# converter dicionario para json

person = {
    "name": "Jane Doe",
    "salary": 9000,
    "skills": [
        "Python",
        "Django",
        "Flask"
    ],
    "email":"janedoe@email.com",
    "projects": [
        "Python Data Mining",
        "Python Data Data Science",
    ]
}

print(type(person))
# dumps - python object

person_to_json = json.dumps(person, indent=4)
print(person_to_json)
print(type(person_to_json))

# salva
with open("janedoe.json", 'w') as file_write:
    json.dump(person, file_write, indent=4)