# Perfil de Consumo - Sabesp
imovel = input("Digite o tipo de imovel: ")
consumo = float(input("Digite o consumo de água em metros cúbicos (m³): "))


# Regras de negócio


if imovel == "comercial":
    print("tarifa comercial aplicada, consulte o plano corporativo")


elif imovel == "casa" or imovel == "apartamento":
    if consumo <= 10:
        print("Consumo economico - excelente controle de água.")
    elif consumo <= 25:
        print("Consumo moderado - dentro dos padrões residencial")
    else:
        print("Consumo excessivo - adotote medidas de economia e verifique por vazamentos.")
