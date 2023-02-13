from models.database.database import db, Column, String, Integer, Numeric, Date, Enum, ForeignKey
from models.reagente import Reagente
from models.many_to_many_relationships.solucao.solucao_usa_reagente import SolucaoUsaReagente
from sqlalchemy.exc import IntegrityError
from datetime import datetime

class Solucao(db.Model):
    """
    Representa a entidade ``solução`` no banco de dados.
    """
    __tablename__ = "solucao"

    id = Column(Integer, primary_key=True, autoincrement=True)

    aula = Column(ForeignKey("aula.id"))
    formula_quimica = Column(ForeignKey('formula_quimica.formula'))
    estado_materia = Column(Enum('Sólido', 'Líquido', 'Gasoso'))
    densidade = Column(Numeric)
    massa = Column(Numeric)
    volume = Column(Numeric)
    concentracao = Column(Numeric)
    local = Column(String(10))
    data_validade = Column(Date)
    deletado_planejado = Column(Enum('Deletado', 'Planejado'))
    
    def __init__(self, formula_quimica:object, estado_materia:str, densidade:float, massa:float, concentracao:float, local:str, data_validade:datetime, volume:float, deletado_planejado:str = None):
        """
        ``id``: int | representa o identificador númerico da solução.
        
        ``nome``: string | representa o nome dado a solução.
        
        ``autor``: string | representa o nome do autor da solução.
        
        ``aula``: objeto da classe ``Aula`` | indica a aula na qual a solução foi criada/registrada.
        
        ``formula_quimica``: objeto da classe ``FormulaQuimica`` | indica a fórmula química da solução.
        
        ``estado_materia``: string | representa o estado da matéria da solução.
        
        ``densidade``: float | representa a densidade da solução, a unidade de medida é kg/m³ (quilograma por metro cúbico).
        
        ``massa``: float | representa a massa total da solução.

        ``concentracao``: float | representa a quantidade de soluto por quantidade de solvente.

        ``deletado_planejado``: string | informa se a solução se encontra em estado de planejamento para uma aula ou se foi deletada.
        
        ``Reagentes``: tuple | contém objetos da classe ``Reagente`` que representam os regentes usados para formar a solução e a massa de reagente que foi usada.
        
        """
        self.formula_quimica = formula_quimica
        self.estado_materia = estado_materia
        self.densidade = densidade
        self.massa = massa
        self.concentracao = concentracao
        self.local = local
        self.data_validade = datetime.strptime(data_validade, '%Y-%m-%d').date()
        self.volume = volume
        self.deletado_planejado = deletado_planejado       
    
    def cadastrar(self, reagentes:tuple[object, float] = None) -> int:
        """
        Realiza o registro da solução no banco de dados e seus relacionamentos com a tabela ``reagente``.
        """
        try:
            # for reagente, massa_utilizada in reagentes:
            #     if reagente.massa < massa_utilizada:
            #         raise ValueError('O valor da massa utilizada deve ser menor ou igual ao disponível no reagente')

            db.session.add(self)
            db.session.commit()
           # id_solucao = [row[0] for row in db.session.execute("select LAST_INSERT_ID()")]
            
            # for reagente in reagentes:
            #     SolucaoUsaReagente(id_solucao[0], reagente[0], reagente[1]).relacionar(db)
            
            # if self.deletado_planejado != 'Planejado':
            #     Reagente.debitar_massa_reagente(db, reagentes)
           
            db.session.commit()
            #return id_solucao
        
        except IntegrityError:
            db.session.rollback()
            #db.session.delete(Solucao.get(id_solucao))
            db.session.commit()
            raise IntegrityError("Erro de integridade")

    @staticmethod
    def listar(tipo_filtro:str, valor_filtro:str):
        if(tipo_filtro == "nome"):
            lista_solucoes = Solucao.query.filter(Solucao.nome.startswith(valor_filtro)).all()
        
        elif(tipo_filtro == "estado-materia"):
            lista_solucoes = Solucao.query.filter_by(estado_materia=valor_filtro).all()
            
        else:
            lista_solucoes = Solucao.query.all()
        
        return lista_solucoes

    def editar(self, nova_formula_quimica:object, novo_estado_materia:str, nova_massa:float, nova_densidade:float, nova_concentracao:float, novo_volume:float, nova_data_validade:str, novo_local:str, novos_reagentes:list = None, nova_aula:object=None):
        #self.aula = nova_aula.id
        self.formula_quimica = nova_formula_quimica
        self.estado_materia = novo_estado_materia
        self.massa = nova_massa
        self.densidade = nova_densidade
        self.concentracao = nova_concentracao
        self.volume = novo_volume
        self.data_validade = datetime.strptime(nova_data_validade, '%Y-%m-%d').date()
        self.local = novo_local

        self.reagentes = novos_reagentes

        try:
            # db.session.query(SolucaoUsaReagente).filter(SolucaoUsaReagente.solucao == self.id).delete()
            # self.id = novo_id
            db.session.add(self)

            # for reagente, massa in self.novos_reagentes:
            #     SolucaoUsaReagente(self, reagente, massa).relacionar(db)
            
            db.session.commit()

        except IntegrityError:
            db.session.rollback()

    def deletar(self):
        """
        Remove o registro da solução e de seus relacionamentos do banco de dados.
        """
        try:
            self.deletado_planejado = 'Deletado'
            db.session.add(self)
            db.session.commit()
        
        except IntegrityError:
            db.session.rollback()
    
    @staticmethod
    def debitar_massa_solucoes(db:object, solucoes:list):
        for solucao, massa_utilizada in solucoes:
            solucao.massa -= massa_utilizada
            db.session.add(solucao)