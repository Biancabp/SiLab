from models.database.database import db, Column, String, Integer, Date, Numeric, ForeignKey
from models.solucao import Solucao

class UsoDiversoSolucao:

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_uso = Column(Date)
    massa = Column(Numeric)
    descricao = Column(String(200))
    solucao = Column(ForeignKey('solucao.id'))

    def __init__(self, data_uso:object, massa:float, descricao:str, solucao:int):
        self.data_uso = data_uso
        self.massa = massa
        self.descricao = descricao
        self.solucao = solucao
    
    def cadastrar(self):
        db.session.add()
        db.session.commit()
    
    @staticmethod
    def listar(solucao:object) -> list:
        lista_uso_diveros_solucao = Solucao.query.filter(Solucao.deletada).all()

        return lista_uso_diveros_solucao

    def editar(self):
        pass

    def deletar(self):
        db.session.delete(self)
        db.session.commit()