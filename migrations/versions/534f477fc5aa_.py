"""empty message

Revision ID: 534f477fc5aa
Revises: 9ebd25fef5d6
Create Date: 2023-01-27 09:03:28.009042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '534f477fc5aa'
down_revision = '9ebd25fef5d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo_equipamento',
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('nome')
    )
    op.create_table('equipamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('localizacao', sa.String(length=100), nullable=False),
    sa.Column('qtd', sa.SmallInteger(), nullable=False),
    sa.Column('volume', sa.SmallInteger(), nullable=False),
    sa.Column('tamanho', sa.SmallInteger(), nullable=False),
    sa.Column('tipo_equipamento', sa.String(length=100), nullable=False),
    sa.Column('lugar', sa.String(length=100), nullable=False),
    sa.Column('danificado', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['tipo_equipamento'], ['tipo_equipamento.nome'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('solucao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('autor', sa.String(length=100), nullable=True),
    sa.Column('aula', sa.Integer(), nullable=True),
    sa.Column('formula_quimica', sa.String(length=30), nullable=True),
    sa.Column('estado_materia', sa.Enum('Sólido', 'Líquido', 'Gasoso'), nullable=True),
    sa.Column('densidade', sa.Numeric(), nullable=True),
    sa.Column('massa', sa.Numeric(), nullable=True),
    sa.Column('concentracao', sa.Numeric(), nullable=True),
    sa.Column('deletado_planejado', sa.Enum('Deletado', 'Planejado'), nullable=True),
    sa.ForeignKeyConstraint(['aula'], ['aula.id'], ),
    sa.ForeignKeyConstraint(['formula_quimica'], ['formula_quimica.formula'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('solucao_usa_reagente',
    sa.Column('solucao', sa.Integer(), nullable=False),
    sa.Column('reagente', sa.Integer(), nullable=False),
    sa.Column('massa', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['reagente'], ['reagente.id'], ),
    sa.ForeignKeyConstraint(['solucao'], ['solucao.id'], ),
    sa.PrimaryKeyConstraint('solucao', 'reagente')
    )
    op.drop_table('curso')
    op.drop_constraint(None, 'turma', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'turma', 'curso', ['curso'], ['nome_curso'])
    op.create_table('curso',
    sa.Column('nome_curso', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('nome_curso')
    )
    op.drop_table('solucao_usa_reagente')
    op.drop_table('solucao')
    op.drop_table('equipamento')
    op.drop_table('tipo_equipamento')
    # ### end Alembic commands ###
