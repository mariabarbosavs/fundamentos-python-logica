tb = As = ex = media = 0.0

tb = float(input('Digite a nota do trabalho de laboratório: '))
As = float(input('Digite a nota da avaliação semestral: '))
ex = float(input('Digite a nota do exame final: '))

media = ((tb*2) + (As*3) + (ex*5))/10

print(f'A média ponderada do aluno é {media}')

if (media >= 80) and (media <= 100):
    print('Aluno com conceito \'A\'!')
elif (media >=70) and (media < 80):
    print('Aluno com conceito \'B\'!')
elif (media >= 60) and (media < 70):
    print('Aluno com conceito\'C\'!')
elif (media >= 50) and (media < 60):
    print('Aluno com conceito\'D\'!')
elif (media > 0) and (media <50):
    print('Aluno com conceito \'E\'!')


