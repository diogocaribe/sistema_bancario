from sistema_bancario import (
    depositar,
    sacar,
    exibir_saldo,
    menu,
    exibir_extrato
)


while True:
    opcao = input(menu())

    if opcao == 'd':
        valor = float(input('\n Valor do depósito R$: '))
        depositar(
            valor,
            exibir_saldo())
        continue

    if opcao == 's':
        valor = float(input('\n Valor do depósito R$: '))
        sacar(saldo=exibir_saldo(),
              valor_saque=valor,
              qtd_operacao_saque_dia=1,
              limite_valor_saque_operacao=500.0)

    if opcao == 'e':
        exibir_extrato()

    if opcao == 'q':
        break
