nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')                     #entrada de valores
print('ola, {} vc tem {} anos'.format(nome, idade))     #saida de valores

valor1 = int(input('informe um valor: '))
valor2 = int(input('informe outro valor: '))

valor = (valor1 + valor2) #o valor foi definido como int então é possivel realizar a soma

print('int valor final: ',valor)

valor1 = input('Informe um valor: ')
valor2 = input('Informe um valor: ')

valor = (valor1 + valor2) #o valor não foi definido como int então ele junta as variaveis
print('sem o int valor final: ',valor)

