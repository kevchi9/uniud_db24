import functions as f

### Parameters for functions in main

client_samples = 1000       # number of clients
richiesta_samples = 2000    # number of requests
tec_samples = 15            # number of employees
max_competences = 2         # max number of competences of an employee
max_interventions = 3       # max numebr of interventions for each request

### Change them from above to modify data produced

def main():
    # f.data_generator_cliente(client_samples)
    # f.data_generator_competenza()
    # f.data_generator_richiesta(richiesta_samples)
    # f.data_generator_tecnico(tec_samples)
    # f.data_generator_possiede(max_competences)
    # f.data_generator_intervento(max_interventions)
    f.data_generator_registro_interventi()
    
main()