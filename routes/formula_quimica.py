from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models.formula_quimica import FormulaQuimica

formula_quimica_blueprint = Blueprint('formula_quimica', __name__)

@formula_quimica_blueprint.route('/formulas_quimica')
@login_required
def formulas_quimica():
    formulas = FormulaQuimica.query.all()
    return render_template('formulas.html', formulas=formulas)

@formula_quimica_blueprint.route('/formulas_quimica/cadastrar', methods=['POST'])
@login_required
def cadastrar_formula_quimica():
    formula_quimica, nome = request.form.get('formula-quimica'), request.form.get('nome')
    FormulaQuimica(formula_quimica, nome).cadastrar()
    formulas = FormulaQuimica.query.all()
    return render_template('formulas.html', formulas=formulas)

@formula_quimica_blueprint.route('/formulas_quimica/editar', methods=['POST'])
@login_required
def editar_formula_quimica():
    id_formula_quimica = request.form.get('id-formula')
    formula_quimica = FormulaQuimica.query.get(id_formula_quimica)

    nova_formula = request.form.get('nova-formula-quimica')
    novo_nome = request.form.get('nome')
    formula_quimica.editar(nova_formula, novo_nome)

    formulas = FormulaQuimica.query.all()
    return render_template('formulas.html', formulas=formulas)

@formula_quimica_blueprint.route('/formulas_quimica/deletar')
@login_required
def deletar_formula_quimica():
    id_formula_quimica = request.form.get('formula-quimica')
    formula_quimica = FormulaQuimica.query.get(id_formula_quimica)
    formula_quimica.deletar()
    return render_template('formulas.html')