from random import randint


def gerar_cartela():
  cartela = []
  for i in range(16):
    cartela.append(randint(1, 99))

  for index, numeros in enumerate(cartela):
    if index == 4 or index == 8 or index == 12:
      print('\n')
    if numeros < 9:
      print('{}'.format(numeros), end='   ')
    else:
      print('{}'.format(numeros), end='  ')


def verifica_pedra(pedra_atual, cartela):
  numeros_marcados = 0
  for numeros in cartela:
    if pedra_atual == numeros:
      numeros_marcados += 1
  if numeros_marcados == 16:
    print('Você venceu')


def chamar_pedras():
  vitoria = False
  pedras = []
  while vitoria != True:
    pedra_atual = randint(1, 99)
    pedras.append(pedra_atual)
    print('Pedra: {}'.format(pedra_atual))



gerar_cartela()
chamar_pedras()