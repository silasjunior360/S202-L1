
from CLI.MotoristaCLI import MotoristaCLI
from DAO.MotoristaDAO import MotoristaDAO
from DAO.PassageiroDAO import PassageiroDAO
from DAO.CorridaDAO import CorridaDAO


from database import Database

db = Database(database="Appp", collection="Motorista")
motorista_dao = MotoristaDAO(db)
passageiro_dao=PassageiroDAO(db)
corrida_dao=CorridaDAO(db)
cli = MotoristaCLI(motorista_dao,passageiro_dao,corrida_dao)
cli.run()

# passageiro=PassageiroDAO(db)
# clii=PassageiroCLI(PassageiroDAO)
# clii.run()

# corrida=CorridaDAO(db)
# cliii=CorridaCLI(CorridaDAO)
# cliii.run()
