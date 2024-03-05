import string
import random
import datetime
import aux

uppercase_letters = list(string.ascii_uppercase)
all_numbers = (0,1,2,3,4,5,6,7,8,9)
competences = ("Idraulica", "Elettronica", "Informatica", "Diagnostica", "Efficienza Energ.", "Termodinamica")
products = ("Caldaia", "Calorifero", "Stufa a pellet", "Impianto a pavimento", "Climatizzatore", "Pompa di calore")

def data_generator_cliente(n):
    '''
    #### Description
    Function used to generate pseudo random SQL code to fill the table Cliente.\n
    Takes an integer as the number of sampels created.\n
    Output is stored in cliente_samples.txt.
    '''

    data_file = open('output/cliente_samples.txt', 'w')
    input_string = "INSERT INTO Cliente(ID, Indirizzo, Tel, PersonaDiRiferimento, NumeroDiRichieste) VALUES\n"

    for i in range(1, n+1):
        
        ID = "{:04d}".format(i)
        address = f"'Via {random.choice(uppercase_letters)}.{random.choice(uppercase_letters)}. {random.randrange(1, 100)}'" 
        phone = "333" + "".join(map(str, random.sample(all_numbers, 7)))
        referrer_person = 'Null'
        request_count = 0

        input_string += f"({ID}, {address}, {phone}, {referrer_person}, {request_count})"
        
        if i != n: 
            input_string += ",\n"
        else:
            input_string += ";" 
    
    data_file.write(input_string)

def data_generator_richiesta(n):
    '''
    #### REQUIREMENTS
    Run data_generator_cliente and data_generator_competenza first.\n
    #### Description
    Function used to generate pseudo random SQL code to fill the table Richiesta.\n
    Takes an integer as the number of sampels created.\n
    Output is stored in richiesta_samples.txt.
    '''

    # competences is the set of possible values for the attribute "TipoProblema" because of integrity constraint
    global competences
    # competences is the set of possible values for the attribute "SistemaInteressato"
    global products

    data_file = open('output/richiesta_samples.txt', 'w')
    input_string = "INSERT INTO Richiesta(nPratica, TipoProblema, SistemaInteressato, Cliente, NumeroDiInterventi) VALUES\n"

    # read data for the foreign keys
    cliente_file = open('output/cliente_samples.txt', 'r')
    cliente_rawlist = cliente_file.read().splitlines()[1:]
    cliente_list = []
    for item in cliente_rawlist:
        cliente_list.append(item[1:5])

    tecnico_file = open('output/tecnico_samples.txt', 'r')
    tecnico_rawlist = tecnico_file.read().splitlines()[1:]
    tecnico_list = []
    for item in tecnico_rawlist:
        tecnico_list.append(item[1:-2])
    
    for i in range(0, n):
        
        request_num = "{:04d}".format(i)
        problem_type = f"'{random.choice(competences)}'" 
        involved_system = f"'{random.choice(products)}'"
        client = f"{random.choice(cliente_list)}"
        intervention_count = 0

        input_string += f"({request_num}, {problem_type}, {involved_system}, {client}, {intervention_count})"
        
        if i != n-1: 
            input_string += ",\n"
        else:
            input_string += ";" 
    
    data_file.write(input_string)
    
def data_generator_intervento(n):
    '''
    #### REQUIREMENTS
    Run data_generator_cliente and data_generator_richiesta first.\n
    #### Description
    Function used to generate pseudo random SQL code to fill the table Intervento.\n
    Takes an integer as the number of sampels created.\n
    Output is stored in intervento_samples.txt.
    '''

    data_file = open('output/intervento_samples.txt', 'w')
    input_string = "INSERT INTO Intervento(Richiesta, nIntervento, Data, Durata, TelCliente) VALUES\n"

    # read data for the foreign keys
    richiesta_file = open('output/richiesta_samples.txt', 'r')
    richiesta_rawlist = richiesta_file.read().splitlines()[1:]
    richiesta_list = []
    for item in richiesta_rawlist:
        richiesta_list.append(item[1:5])

    
    for request in richiesta_list:

        rand_intervention_amount = random.randrange(1, n + 1)
        
        # 1st loop is used to ensure that the date randomly generated are sorted from the oldest to the newest
        interventions_date = []
        for i in range(0, rand_intervention_amount):
            interventions_date.append(aux.random_date('01/01/2019', '01/01/2022', "%d/%m/%Y"))
        interventions_date.sort()

        # 2nd loop is used to randomize the amount of intervention for each request (min 1, max n)
        for i in range(0, rand_intervention_amount):
            
            # generates hours and minutes to format the time interval of the intervention duration
            h = "{:02d}".format(random.randrange(0, 3))
            if h == "00":
                m = random.randrange(15, 60, 15)
            else:
                m = "{:02d}".format(random.randrange(00, 60, 30))
            
            intervention_num = "{:04d}".format(i+1)
            data = interventions_date[0]
            interventions_date.pop(0)
            duration = f"00:{h}:{m}"
            phone = 'Null'

            input_string += f"({request}, {intervention_num}, DATE '{data}', '{duration}', {phone})"
            if i != rand_intervention_amount-1 :
                input_string += ",\n"

        if richiesta_list.index(request) != len(richiesta_list)-1: 
            input_string += ",\n"
        else:
            input_string += ";" 

    data_file.write(input_string)

#TODO: finire
def data_generator_registro_interventi():
    '''
    #### REQUIREMENTS
    Run data_generator_intervento and data_generator_tecnico first.\n
    #### Description
    Function used to generate pseudo random SQL code to fill the table RegistroInterventi.\n
    Takes an integer as the number of sampels created.\n
    Output is stored in registrointerventi_samples.txt.
    '''

    data_file = open('output/registro_interventi.txt', 'w')
    input_string = "INSERT INTO RegistroInterventi(Tecnico, Richiesta, Intervento) VALUES\n"

    # read data for the foreign keys
    possiede_file = open('output/possiede_samples.txt', 'r')
    possiede_rawlist = possiede_file.read().splitlines()[1:]
    
    intervento_file = open('output/intervento_samples.txt', 'r')
    intervento_rawlist = intervento_file.read().splitlines()[1:]
    intervento_list = [] # contains tuples, first element is request_id, second element is intervention_id
    for item in intervento_rawlist:
        intervento_list.append((item[1:5], item[7:11]))

    richiesta_file = open('output/richiesta_samples.txt', 'r')
    richiesta_rawlist = richiesta_file.read().splitlines()[1:]

    for item in intervento_list:
        
        issue_type = ''
        employee = ''

        # find the issue_type from request_id
        for line in richiesta_rawlist:
            if item[0] in line:
                issue_type = line[8:].split("'")[0]

        # find an employee which has the competences for the issue_type
        # in order to distribute equally the jobs to each employee, each employee is picked randomly and if he has competences, it is confirmed and the loop is stopped.
        # that's why the while True loop
        while True:
            random_line = random.choice(possiede_rawlist)
            if issue_type in random_line:
                employee = random_line[2:18]
                break

        input_string += f"('{employee}', {item[0]}, {item[1]})"
        
        if intervento_list.index(item) != len(intervento_list) - 1: 
            input_string += ",\n"
        else:
            input_string += ";" 
    
    data_file.write(input_string)
    
        
def data_generator_tecnico(n):
    '''
    #### Description
    Function used to generate pseudo random SQL code to fill the table Tecnico.\n
    Takes an integer as the number of sampels created.
    Output is stored in tecnico_samples.txt.
    '''
    
    data_file = open('output/tecnico_samples.txt', 'w')
    input_string = "INSERT INTO Tecnico(CF) VALUES\n"

    for i in range(1, n+1):
         
        input_string += f"('{''.join(random.sample(uppercase_letters, 6))}{''.join(map(str, random.sample(all_numbers, 2)))}{random.choice(uppercase_letters)}{''.join(map(str, random.sample(all_numbers, 2)))}{random.choice(uppercase_letters)}{''.join(map(str, random.sample(all_numbers, 3)))}{random.choice(uppercase_letters)}')"
        
        if i != n: 
            input_string += ",\n"
        else:
            input_string += ";" 
    
    data_file.write(input_string)
    
def data_generator_competenza():
    '''
    #### Description
    Function used to generate SQL code to fill the table Competenza.\n
    The samples added to the table are defined in the global variable 'competences' at the beginning of the file.
    Takes an integer as the number of sampels created.
    Output is stored in tecnico_samples.txt.
    '''

    global competences

    data_file = open('output/competenze_samples.txt', 'w')
    input_string = "INSERT INTO Competenza(Campo) VALUES\n"

    for item in competences:

        input_string += f"('{item}')"

        if competences.index(item) != len(competences)-1: 
            input_string += ",\n"
        else:
            input_string += ";" 

    data_file.write(input_string)


def data_generator_possiede(n):
    '''
    #### REQUIREMENTS
    Run data_generator_tecnico and data_generator_competenza first.\n
    #### Description
    Function used to generate pseudo random SQL code to fill the table Possiede.\n
    Takes an integer as the number of sampels created.\n
    Output is stored in possiede_samples.txt.
    '''

    global competences
    
    data_file = open('output/possiede_samples.txt', 'w')
    input_string = "INSERT INTO Possiede(Tecnico, Competenza) VALUES\n"
    
    # read data for the foreign keys
    tecnico_file = open('output/tecnico_samples.txt', 'r')
    tecnico_list = tecnico_file.read().splitlines()

    for index in range(1, len(tecnico_list)):
        
        # rand n is the random number of competences that an employee must have
        rand_n = random.randrange(1, n + 1)
        # random picks are stored in this list to avoid duplicated in the same row
        previous_picks = []                          

        for j in range(0, rand_n):
            pick = random.choice(competences)
            # check if the new pick is already in the list mentioned above
            if pick not in previous_picks:
                input_string += f"({tecnico_list[index][1:-2]}, '{pick}')"
                previous_picks.append(pick)

                if index != len(tecnico_list)-1:
                    input_string += ",\n"
                else:
                    input_string += ";"
            else: 
                # repeat this cycle of the loop if the new pick is already in previous_picks list 
                j -= 1

    data_file.write(input_string)