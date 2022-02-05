DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    """LIST COMPREHENSION"""
    #all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    #all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    #for worker in all_platzi_workers:
        #print(worker)
    
    """THE CHALLENGE IS TO DO THE THINGS THAT ARE ABOVE WITH FUNCTIONS"""

    """Crear las listas all_python_devs y all_platzi_workers usando filter y map 
    Crear la lista old_people y adults con list COMPREHENSION"""

    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))

    all_python_devs = list(filter(lambda worker : worker["language"] == "python",DATA))
    all_python_devs = list(map(lambda worker: worker["name"],all_python_devs))
    
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    
    #old_people = [{**worker, **{'old':worker["age"] > 70}} for worker in DATA]
    old_people = [{**worker, **{'old':worker["age"] > 70}} for worker in DATA]
    print(old_people)

    """FUNCIONES COMPLEJAS"""
    

    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"],adults))
    #Quiero ponerle una llave extra al diccionario DATA de arriba
    #Que sea True or false para >70    
    old_people = list(map(lambda worker: worker | {"old":worker["age"] > 70}, DATA))  
    #print(old_people)

if __name__ == '__main__':
    run()