from flask import Flask, request, jsonify
from barcode import Code128 # Classe responsável por gerar tags de código de barras
from barcode.writer import ImageWriter # Importa a classe usada para salvar a tag como imagem
app = Flask(__name__) # Cria uma instância do aplicativo Flask

# Define uma rota para o endpoint '/create_tag', onde solicitações POST são esperadas
@app.route('/create_tag', methods=["POST"])
def create_tag():
    body = request.json # Extrai os dados JSON da solicitação
    product_code = body.get('product_code') # Obtém o código do produto do body da solicitação http

    # Cria uma tag de código de barras com o código do produto,  usando imagem como saída
    tag = Code128(product_code, writer=ImageWriter())

    # Define o caminho do arquivo para salvar a tag de código de barras
    path_from_tag = f'{tag}'

    # Salva a tag de código de barras como uma imagem no caminho especificado
    tag.save(path_from_tag)
    # Retorna uma resposta JSON com o caminho do arquivo da tag de código de barras
    return jsonify({ "tag_path": path_from_tag })

if __name__ == '__main__':
    # Inicia o servidor Flask na porta 3000
    app.run(host='0.0.0.0', port=3000)
