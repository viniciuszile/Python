import sys

while True:
    estado = ""
    cpf_valido = True

    cpf = input("Informe o seu CPF (apenas os números) ou digite 'sair' para encerrar: ").strip()

    if cpf.lower() == 'sair':
        sys.exit()

    if cpf.isdigit():
        if len(cpf) != 11:
            print("CPF com tamanho inválido.")
            print("Lembre-se de informar os 11 dígitos do CPF (12312312312)")
            cpf_valido = False
    else:
        print("CPF inválido. Informe apenas números.")
        cpf_valido = False

    if not cpf_valido:
        continue
    else:
        cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    if cpf[8] == '0':
        estado = "Rio Grande do Sul"
    elif cpf[8] == '1':
        estado = "Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins"
    elif cpf[8] == '2':
        estado = "Pará, Amazonas, Acre, Amapá, Rondônia e Roraima"
    elif cpf[8] == '3':
        estado = "Ceará, Maranhão e Piauí"
    elif cpf[8] == '4':
        estado = "Pernambuco, Rio Grande do Norte, Paraíba e Alagoas"
    elif cpf[8] == '5':
        estado = "Bahia e Sergipe"
    elif cpf[8] == '6':
        estado = "Minas Gerais"
    elif cpf[8] == '7':
        estado = "Rio de Janeiro e Espírito Santo"
    elif cpf[8] == '8':
        estado = "São Paulo"
    elif cpf[8] == '9':
        estado = "Paraná e Santa Catarina"
    else:
        estado = "Estado não identificado"

    print("CPF válido.")
    print("Seu CPF formatado é:", cpf_formatado)
    print("O(s) estado(s) correspondente(s) ao CPF (são):", estado)
    print()
