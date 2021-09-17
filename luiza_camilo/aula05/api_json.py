import json
import requests

# API - https://jsonplaceholder.typicode.com/todos

def get_data():
    api = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api)
    #print(response.status_code) # 200 HTTP = ok
    #print(response.content)
    todos = json.loads(response.content)
    return todos


# for todo in todos:
#     print(todo)

"""
{
    "userID": None,
    "id":None
    "title":None
    ""completed": True/False
}
"""
# AVALIAR - UM REGISTRO
def get_one_register():
    one = get_data()
    #print(type(one))
    return one[0]

#print(get_one_register())
 
def get_all_completed_register():
    """Salva apaenas os registros com status True"""
    completed_regs = []
    for register in get_data():
        if register['completed'] == True:
            completed_regs.append(register)

    return(completed_regs)

# for data in get_all_completed_register():
#     print(data)

# save data 
def save_data_to_json():
    """Salva em arquivo fisico"""
    with open('completed.json', 'w') as file:
        json.dump(get_all_completed_register(), file, indent=4)

save_data_to_json()

# HOME WORK - CRIAR FUNCAO PARA COMPLETED == FALSE

