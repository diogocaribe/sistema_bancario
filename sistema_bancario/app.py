from sistema_bancario import (
    deposito,
    saque,
    saldo,
    historico_transacao,
    menu,
    extrato,
)


while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Valor do depósito R$: '))
        deposito(valor, saldo(historico_transacao),
                 extrato(historico_transacao))
        continue

    if opcao == 's':
        saque()

    if opcao == 'e':
        historico_transacao()

    if opcao == 'q':
        break
