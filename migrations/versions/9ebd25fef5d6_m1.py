"""m1

Revision ID: 9ebd25fef5d6
Revises: 
Create Date: 2022-12-21 00:38:26.015197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ebd25fef5d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curso',
    sa.Column('nome_curso', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('nome_curso')
    )
    op.create_table('formula_quimica',
    sa.Column('formula', sa.String(length=30), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('formula')
    )
    op.create_table('usuario',
    sa.Column('matricula', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=300), nullable=False),
    sa.Column('senha', sa.String(length=64), nullable=False),
    sa.Column('tipo_usuario', sa.Enum('Professor', 'Tutor'), nullable=False),
    sa.PrimaryKeyConstraint('matricula')
    )
    op.create_table('reagente',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('estado_materia', sa.Enum('Sólido, Líquido, Gasoso'), nullable=False),
    sa.Column('densidade', sa.Numeric(), nullable=False),
    sa.Column('massa', sa.Numeric(), nullable=True),
    sa.Column('volume', sa.Numeric(), nullable=True),
    sa.Column('data_validade', sa.Date(), nullable=True),
    sa.Column('formula_quimica', sa.String(length=30), nullable=False),
    sa.Column('deletado', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['formula_quimica'], ['formula_quimica.formula'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('turma',
    sa.Column('cod', sa.String(length=10), nullable=False),
    sa.Column('ano', sa.SmallInteger(), nullable=True),
    sa.Column('turno', sa.Enum('Matutino', 'Vespertino', 'Noturno'), nullable=True),
    sa.Column('curso', sa.String(length=100), nullable=True),
    sa.Column('qtd_alunos', sa.SmallInteger(), nullable=True),
    sa.ForeignKeyConstraint(['curso'], ['curso.nome_curso'], ),
    sa.PrimaryKeyConstraint('cod')
    )
    op.create_table('aula',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('turma', sa.String(length=10), nullable=True),
    sa.Column('data_aula', sa.Date(), nullable=True),
    sa.Column('roteiro', sa.String(length=500), nullable=True),
    sa.Column('professor', sa.Integer(), nullable=True),
    sa.Column('planejada_efetivada', sa.Enum('Planejada', 'Efetivada'), nullable=True),
    sa.Column('deletada', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['professor'], ['usuario.matricula'], ),
    sa.ForeignKeyConstraint(['turma'], ['turma.cod'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aula')
    op.drop_table('turma')
    op.drop_table('reagente')
    op.drop_table('usuario')
    op.drop_table('formula_quimica')
    op.drop_table('curso')
    # ### end Alembic commands ###
