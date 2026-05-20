idade = 15
altura = 1.75

resultado = (idade >= 18) and (altura>=1.70)
msg = "pode participar do evento? " + str(resultado)
print(msg)

"""programa de disparo de alarme"""

porta = 'a' 
janela = 'f'
alarme = (porta == "a") or (janela == "a")
msg = 'Alarme disparado? ' + str(alarme)
print(msg)

tem_dinheiro = True
tem_dinheiro = not (tem_dinheiro)

msg = ('tem dinheiro?' + str(tem_dinheiro))
print(msg)