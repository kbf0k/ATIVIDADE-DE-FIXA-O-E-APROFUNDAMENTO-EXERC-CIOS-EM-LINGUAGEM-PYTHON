# Kaique Bernardes Ferreira, João Pedro da Cunha Machado, Gabriel Moreira Gonçalves
while True:
    try:
        temperatura = float(input('DIGITE A TEMPERATURA: '))
        escolha = int(input('[1] Celsius\n[2] Fahrenheit\n[3] Kelvin\n:'))
        match escolha:
            case 1:
                def celsius():
                    print(f'{temperatura}ºC')
                celsius()
                break
            case 2:
                def fahrenheit():
                    print(f'{(temperatura*9/5)+32} Fahrenheit')
                fahrenheit()
                break
            case 3:
                def kelvin():
                    print(f'{temperatura + 273.15} Kelvin')
                kelvin()
                break
            case _:
               escolha = int(input('[1] Celsius\n[2] Fahrenheit\n[3] Kelvin\n:'))
    except ValueError:
        print('RESPOSTA INVÁLIDA')