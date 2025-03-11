from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])  # Alterado de GET para POST
def receber_venda():
    # Extrair dados do JSON enviado na requisição
    dados = request.get_json()
    
    if not dados:
        return "Nenhum dado recebido", 400  # Retorna erro caso o JSON esteja vazio
    
    produto = dados.get("product", "Produto não especificado")
    valor = dados.get("amount", "Valor não especificado")
    cliente = dados.get("customer", "Cliente não especificado")
    transaction_id = dados.get("transaction_id", "ID de transação não especificado")

    mensagem = f"Nova venda!\nProduto: {produto}\nValor: {valor}\nCliente: {cliente}\nID Transação: {transaction_id}"

    # Enviar mensagem para o Telegram
    token = "7791441080:AAHkT4qxRJT51740oiIbS4lYgu8bgGOuuN4"  # Seu token do bot do Telegram
    chat_id = "7017849174"  # Seu chat_id do Telegram
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensagem
    }
    response = requests.post(url, json=payload)  # Envia a requisição para o Telegram com JSON

    if response.status_code != 200:
        return f"Erro ao enviar mensagem para o Telegram: {response.text}", 500

    return "OK", 200  # Resposta para confirmar que a requisição foi recebida com sucesso

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
