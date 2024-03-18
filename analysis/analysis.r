library("RPostgreSQL")

dsn_database = "basi24"
dsn_server = "localhost"
dsn_port = "5432"
dsn_uid = "postgres"
dsn_pswd = "postgres"

# tryCatch({
#     drv <- dbDriver("PostgreSQL")
#     print("Connecting to Database...")
#     connec <- dbConnect(drv,
#                 dbname = dsn_database,
#                 host = dsn_server,
#                 port = dsn_port,
#                 user = dsn_uid,
#                 password = dsn_pswd)
#     print("Database Connected!")
# },
# error = function(cond) {
#     print("Unable to connect to Database")
# })

# cliente_df <- dbGetQuery(connec, "SELECT * FROM progetto_basi.Cliente")
# richiesta_df <- dbGetQuery(connec, "SELECT * FROM Richiesta")
# reg_inter_df <- dbGetQuery(connec, "SELECT * FROM RegistroInterventi")
# possiede_df <- dbGetQuery(connec, "SELECT * FROM Possiede")

distribuzione_lavori_mesi_df <- dbGetQuery(connec, 
            "SELECT EXTRACT(month FROM data) as mese, 
            count(*) as n_interventi
            FROM progetto_basi.intervento 
            GROUP BY mese
            ORDER BY mese;")

#test_df <- as.numeric(raw_df)
test_df <- lapply(distribuzione_lavori_mesi_df, as.numeric)

print(test_df)
plot(test_df$mese, test_df$n_interventi, "o")
# hist(test_df[c('count')])

# barplot(test_df[c('count')])