nome = input('Digite o seu nome:')
idade = int(input('Digite sua idade:'))
peso = float(input('Digite o seu peso em KG:'))
altura = float(input('Digite a sua altura em m:'))
anos = 2023-idade
imc = (peso)/(altura*altura)
print('Seu nome é ' + str(nome) + ' e tem ' + str(len(nome)) + ' caracteres, você tem '+ str(idade) + ' anos e nasceu no ano de ' + str(anos) + ' . Você mede '+ str(altura)+ 'M e pesa ' + str(peso) + 'KG e seu IMC é: ' + str(imc) )