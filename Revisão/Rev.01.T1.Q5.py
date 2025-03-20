def calcular_custo_final(custo_de_fabrica):
    # Definir as constantes das taxas
    percentagem_distribuidor = 0.28
    impostos = 0.45
    
    # Calcular o valor da percentagem do distribuidor
    valor_distribuidor = percentagem_distribuidor * custo_de_fabrica
    
    # Calcular o valor dos impostos
    valor_impostos = impostos * custo_de_fabrica
    
    # Calcular o custo final ao consumidor
    custo_final = custo_de_fabrica + valor_distribuidor + valor_impostos
    
    # Retornar o custo final ao consumidor
    return custo_final

# Exemplo de uso da função
custo_fabrica = float(input())
custo_final_consumidor = calcular_custo_final(custo_fabrica)
print(f"R$ {custo_final_consumidor:.2f}")
