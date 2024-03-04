import string;
import random;

uppercase_letters = list(string.ascii_uppercase)
all_numbers = (0,1,2,3,4,5,6,7,8,9)
competences = ("Idraulica", "Elettronica", "Informatica", "Diagnostica", "Efficienza Energ.", "Termodinamica")
products = ("Caldaia", "Calorifero", "Stufa a pellet", "Impianto a pavimento", "Climatizzatore", "Pompa di calore")

### Parameters for functions in main

client_samples = 1000       # number of clients
richiesta_samples = 2000    # number of requests
tec_samples = 15            # number of employees
max_competences = 2         # max number of competences of an employee

### Change them from here to modify data produced

def main():
    # data_generator_cliente(client_samples)
    # data_generator_competenza()
    # data_generator_richiesta(richiesta_samples)
    # data_generator_tecnico(tec_samples)
    # data_generator_possiede(max_competences)
    pass

def data_generator_cliente(n):
    '''
    #### Description
    Function used to generate pseudo random SQL code to fill the table Cliente.\n
    Takes an integer as the number of sampels created.\n
    Output is stored in cliente_samples.txt.
    '''

    data_file = open('cliente_samples.txt', 'w')
    
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

    data_file = open('richiesta_samples.txt', 'w')

    cliente_file = open('cliente_samples.txt', 'r')
    cliente_rawlist = cliente_file.read().splitlines()[1:]
    cliente_list = []
    for item in cliente_rawlist:
        cliente_list.append(item[1:5])

    tecnico_file = open('tecnico_samples.txt', 'r')
    tecnico_rawlist = tecnico_file.read().splitlines()[1:]
    tecnico_list = []
    for item in tecnico_rawlist:
        tecnico_list.append(item[1:-2])

    input_string = "INSERT INTO Richiesta(nPratica, TipoProblema, SistemaInteressato, Cliente, NumeroDiInterventi) VALUES\n"
    
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
    

#TODO: finire
def data_generator_intervento(n):
    '''
    #### REQUIREMENTS
    Run data_generator_cliente and data_generator_richiesta first.\n
    #### Description
    Function used to generate pseudo random SQL code to fill the table Intervento.\n
    Takes an integer as the number of sampels created.\n
    Output is stored in intervento_samples.txt.
    '''

    data_file = open('data.txt', 'w')
    
    input_string = "INSERT INTO Cliente(ID, Indirizzo, Telefono, PersonaDiRiferimento, NumeroDiRichiesta) VALUES\n"

    for i in range(1, n+1):
        
        ID = "{:04d}".format(i)
        address = f"Via {random.choice(uppercase_letters)}.{random.choice(uppercase_letters)}. {random.randrange(1, 100)}" 
        phone = "333" + "{:07d}".format(i)
        referrer_person = None
        request_num = 0

        input_string += f"({ID}, {address}, {phone}, {referrer_person}, {request_num})"
        
        if i != n: 
            input_string += ",\n"
        else:
            input_string += ";" 
    
    print(input_string)
    data_file.write(input_string)

#TODO: finire
def data_generator_registro_interventi(n):
    '''
    #### REQUIREMENTS
    Run data_generator_intervento and data_generator_tecnico first.\n
    #### Description
    Function used to generate pseudo random SQL code to fill the table RegistroInterventi.\n
    Takes an integer as the number of sampels created.\n
    Output is stored in registrointerventi_samples.txt.
    '''

    data_file = open('data.txt', 'w')
    
    input_string = "INSERT INTO RegistroInterventi(Tecnico, Richiesta, Intervento) VALUES\n"

    for i in range(1, n+1):
        
        ID = "{:04d}".format(i)
        address = f"Via {random.choice(uppercase_letters)}.{random.choice(uppercase_letters)}. {random.randrange(1, 100)}" 
        phone = "333" + "{:07d}".format(i)
        referrer_person = None
        request_num = 0

        input_string += f"({ID}, {address}, {phone}, {referrer_person}, {request_num})"
        
        if i != n: 
            input_string += ",\n"
        else:
            input_string += ";" 
    
    print(input_string)
    data_file.write(input_string)

def data_generator_tecnico(n):
    '''
    #### Description
    Function used to generate pseudo random SQL code to fill the table Tecnico.\n
    Takes an integer as the number of sampels created.
    Output is stored in tecnico_samples.txt.
    '''
    data_file = open('./tecnico_samples.txt', 'w')
    
    input_string = "INSERT INTO Tecnico(CF) VALUES\n"

    for i in range(1, n+1):
         
        input_string += f"({''.join(random.sample(uppercase_letters, 6))}{''.join(map(str, random.sample(all_numbers, 2)))}{random.choice(uppercase_letters)}{''.join(map(str, random.sample(all_numbers, 2)))}{random.choice(uppercase_letters)}{''.join(map(str, random.sample(all_numbers, 3)))}{random.choice(uppercase_letters)})"
        
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
    data_file = open('competenze_samples.txt', 'w')
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
    
    data_file = open('possiede_samples.txt', 'w')
    input_string = "INSERT INTO Possiede(Tecnico, Competenza) VALUES\n"
    
    tecnico_file = open('tecnico_samples.txt', 'r')
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
                input_string += f"({tecnico_list[index][1:-2]}, {pick})"
                previous_picks.append(pick)

                if index != len(tecnico_list)-1:
                    input_string += ",\n"
                else:
                    input_string += ";"
            else: 
                # repeat this cycle of the loop if the new pick is already in previous_picks list 
                j -= 1

    data_file.write(input_string)

main()


# for j in range(competence_n):
#    competence.append(random.choice(fields))