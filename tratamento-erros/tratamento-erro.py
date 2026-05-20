text = 'texto invalido'

try:
    """Tratamentos de erros e exceções: Tentativa de converção de uma variável do tipo string para int"""
    print(int(text))
except:
    print("Houve um erro na conversão!")
finally:
    print("Tentativa de conversão finalizada!")

    

divisor = 0

try:
    """Tratamento de erro para divisões com número = 0"""
    resultado = 20//divisor 
except ZeroDivisionError: 
    print('Erro: Não é possivel dividir um número por 0.')
finally:
    if (divisor > 0):
        print(f'Divisão concluida! Resultado: {resultado}')
    else:
        print('Tentativa finalizada!')
