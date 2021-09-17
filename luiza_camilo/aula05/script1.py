import json

# dois casos:  strings ou dicionarios

# string
person = '{"name": "Bob","languages":["English", "Franch"]}'

print(type(person))
print(person)
print()
person_as_dict = json.loads(person) # LOADS() ESPERA UMA STRING
print()
print(type(person_as_dict))
print(person_as_dict["languages"])
print()

# converter json
# dumps() -- espera um objeto do tipo Python
print(json.dumps(person_as_dict, indent=4, sort_keys=True))
