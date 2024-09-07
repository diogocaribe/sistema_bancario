from sistema_bancario import (
    depositar,
    sacar,
    exibir_saldo,
    historico_transacao,
    menu,
    exibir_extrato,
)


while True:
    opcao = input(menu())

    if opcao == "d":
        valor = float(input("\n Valor do depósito R$: "))
        depositar(
            valor, exibir_saldo(historico_transacao),
            exibir_extrato(historico_transacao),
        )
        continue

    if opcao == "s":
        sacar()

    if opcao == "e":
        exibir_extrato()

    if opcao == "q":
        break
