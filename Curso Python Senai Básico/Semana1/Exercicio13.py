largura = int(input('Digite a largura da parede em metros:'))# recebe o valor de largura
altura = int(input('Digite a altura da parede em metros:'))#recebe o valor de altura
metrosquadrados = altura*largura # calcula o valor de m²
latasdetinta = (metrosquadrados)/(3) # calcula a quantidade de latas de tinta
print ('Você precisará de '+ str(latasdetinta) + ' latas de tinta para pintar sua parede') #exibe o resultado final de quantas latas de tinta o usuário irá precisar para pintar a parede