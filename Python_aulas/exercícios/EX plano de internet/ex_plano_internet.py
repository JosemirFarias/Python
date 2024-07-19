def solicitar_consumo_dados():
   
    while True:
        try:
            consumo = float(input("Digite o consumo médio mensal de dados em GB: "))
            return consumo
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def recomendar_plano(consumo):
   
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB."
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB."
    else:
        return "Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB."


try:
    consumo_mensal = solicitar_consumo_dados()
    recomendacao = recomendar_plano(consumo_mensal)
    print(recomendacao)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
