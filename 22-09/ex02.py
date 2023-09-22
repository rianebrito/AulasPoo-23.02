insatisfeito = 0
satisfeito = 0
nao_responder = 0

print("Opções de resposta:")
print("1 - insatisfeito")
print("2 - satisfeito")
print("3 - não quero responder")
print("0  - encerrar pesquisa")

resp = int(input("olá! somos a farmácia drogão. digite o numero correspontente a sua resposta  de satisfação"))

while resp != 0:
    if resp == 1:
         insatisfeito +=1

    elif resp == 2:
         satisfeito +=1

    elif resp == 3:
         nao_responder +=1
    
    else:
         print("opção inválida")

    resp = int(input("olá! somos a farmácia drogão. digite o numero correspontente a sua resposta  de satisfação"))

total_respostas = insatisfeito + satisfeito + nao_responder
percentual_insatisfeito = (insatisfeito / total_respostas) * 100
percentual_satisfeito = (satisfeito / total_respostas) * 100
percentual_nao_responder = (nao_responder / total_respostas) * 100

print(f"insatisfeitos: {percentual_insatisfeito}")
print(f"satisfeitos {percentual_satisfeito}")
print(f"não quiseram responder: {nao_responder}")