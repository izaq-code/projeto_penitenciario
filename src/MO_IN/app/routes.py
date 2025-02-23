from flask import Blueprint, render_template, request, jsonify, Response, send_from_directory
from app.model_handler import predict_outcomes
import pandas as pd  # IMPORTAÇÃO DO PANDAS AQUI
import os

main = Blueprint('main', __name__)

# Página inicial com o formulário de upload
@main.route('/')
def index():
    return render_template('index.html')

# Rota de previsão
@main.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado"}), 400

    if file and file.filename.endswith('.xlsx'):
        try:
            # Usando o pandas corretamente para ler o arquivo Excel
            data = pd.read_excel(file)  # Aqui estamos utilizando o pandas para ler o arquivo

            # Realiza as previsões com a função 'predict_outcomes'
            predictions = predict_outcomes(data)

            # Envia os resultados para a página de resultados
            return render_template('resultados.html', predictions=predictions)
        except Exception as e:
            return jsonify({"error": f"Erro ao processar o arquivo: {str(e)}"}), 500
    else:
        return jsonify({"error": "O arquivo enviado não é um arquivo Excel válido"}), 400

# Rota para servir qualquer arquivo CSS da pasta static/
@main.route('/static/<filename>')
def serve_css(filename):
    # Ajuste o caminho para garantir que estamos procurando na pasta 'static'
    css_path = os.path.join('static', filename)
    
    if not os.path.exists(css_path):
        return jsonify({"error": f"Arquivo {filename} não encontrado"}), 404
    
    with open(css_path, 'r') as css_file:  # Abra o arquivo CSS
        css_content = css_file.read()  # Leia o conteúdo
    return Response(css_content, mimetype='text/css')  # Retorna o conteúdo CSS com o tipo correto
