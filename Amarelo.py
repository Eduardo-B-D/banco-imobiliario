valor_atual = int(input('Insira o valor inicial:'))

while valor_atual > 0:

    print(f'Seu saldo atual é de \033[4;33m{valor_atual}\033[m')
    print('')
    valor = int(input('Digite a operação:'))
    valor_atual += valor
    if valor < 0:
        print(f'\033[31mSubtraiu {int(valor)}\033[m')

    elif valor > 0:
        print(f'\033[32mAdicionou {valor}\033[m')

print('\033[4;31mVocê perdeu!\033[m')