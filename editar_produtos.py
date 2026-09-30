produtos = ["Arroz", "Feijão", "Café", "Açúcar"]

produtos[1] = "Pão"
produtos.remove("Café")
if "Leite" in produtos:
    produtos.remove("Leite")
else:
    print("Produto não encontrado.")