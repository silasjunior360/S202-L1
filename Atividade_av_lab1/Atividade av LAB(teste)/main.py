
from CLI.MotoristaCLI import MotoristaCLI
from DAO.MotoristaDAO import MotoristaDAO
from CLI.PassageiroCLI import PassageiroCLI
from DAO.PassageiroDAO import PassageiroDAO
from CLI.CorridaCLI import CorridaCLI
from DAO.CorridaDAO import CorridaDAO


from database import Database

db = Database(database="App", collection="Motorista")
motorista_dao = MotoristaDAO(db)
cli = MotoristaCLI(motorista_dao)
cli.run()

# passageiro=PassageiroDAO(db)
# clii=PassageiroCLI(PassageiroDAO)
# clii.run()

# corrida=CorridaDAO(db)
# cliii=CorridaCLI(CorridaDAO)
# cliii.run()
