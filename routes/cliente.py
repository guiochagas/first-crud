from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint("cliente", __name__)

@cliente_route.route("/") # Listar todos os clientes
def lista_clientes():
    return render_template("lista_clientes.html", clientes=CLIENTES)


@cliente_route.route("/", methods=["POST"]) # Inserir os dados do cliente.
def inserir_cliente():
    return {"ok": "ok"}


@cliente_route.route("/new") # Formulário para cadastrar um cliente.
def form_cliente():
    return render_template("form_cliente.html")


@cliente_route.route("/<int:cliente_id>") # Exibir detalhes do cliente.
def detalhe_cliente(cliente_id):
    return render_template("detalhe_cliente.html")


@cliente_route.route("/<int:cliente_id>/edit") # Formulário para editar um cliente.
def form_edit_cliente(cliente_id):
    return render_template("form_edit_cliente.html")


@cliente_route.route("/<int:cliente_id>/update", methods=["PUT"]) # Atualizar informações de um cliente.
def atualizar_cliente(cliente_id):
    pass


@cliente_route.route("/<int:cliente_id>/delete", methods=["DELETE"]) # Deletar um cliente.
def deletar_cliente(cliente_id):
    pass