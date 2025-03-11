from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def receber_venda():
    data = request.json  # Pega os dados enviados no corpo da requisição

    produto = data.get("produto", "Produto não especificado")
    valor = data.get("valor", "Valor não especificado")
    cliente = data.get("cliente", "Cliente não especificado")

    mensagem = f"Nova venda!\nProduto: {produto}\nValor: {valor}\nCliente: {cliente}"

    # Enviar mensagem para o Telegram
    token = "7791441080:AAHkT4qxRJT51740oiIbS4lYgu8bgGOuuN4"  # Seu token do bot do Telegram
    chat_id = "7017849174"  # Seu chat_id do Telegram
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensagem
    }
    requests.post(url, data=payload)  # Envia a requisição para o Telegram

    return "OK", 200  # Resposta para confirmar que a requisição foi recebida com sucesso

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

