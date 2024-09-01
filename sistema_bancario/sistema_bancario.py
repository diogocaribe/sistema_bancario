from datetime import date, datetime

"""
Unico usuário

Operações:
    depósito
        Valores positivos
    saque
        Limite de 3 saques diários
        Limite no valor do saque de R$ 500,00
        Não havendo saldo, retornar uma msg informando que não há saldo para o saque
    extrato
        Todos os depositos e saques devem aparecer no retorno do extrato
        Ao final do extrato deve aparecer o saldo
        Se tiver em branco retornar 'Não foram realizadas movimentações.'

        -> Adicionar a data e hora

        Formato:
            R$ XXX.XX
    -> Transações:
            10 transaççoes no dia
            Retornar msg apos atingir o limite
            Limite maximo de transações diário

#####################################################
    # Utilizar funções para otimizar o código
        Separar em funções:
            Deposito
                Argumentos (positional only):
                    saldo, valor, extrato
                Retorno:
                    saldo e extrato
            Saque:
                Argumentos (keyword only):
                    saldo, valor, extrato, limite,
                    numero_saque, limite_saque
                Retorno:
                    saldo, extrato
            Extrato:
                Argumentos (positional only e keyword only):
                    posicionais: saldo
                    nomeados: extrato
                Retorno:
                    Imprimir o extrato

        Criar duas funções:
            Criar cliente:
                Armazenar em uma lista (nome,
                data nascimento, cpf, endereço)

                Endereço é uma string com formato: logradouro,
                numero - bairro - vidade/sigla estado.
                Armazenar somente os numeros do CPF. Retirar pontos e traço
                CPF é unique (não cadastrar 2 CPF)

            Criar conta corrente
                Conta é composta por: agencia, numero da conta e usuario
                Número da conta é sequencial iniciando em 1
                Número da Agencia é fixo: '0001'
                Usuário pode ter mais de uma conta, mas uma conta
                pertence a somente um usuário.

                Dica: Para vincular usuário a uma conta, filtre a lista
                de usuários buscando o numero do CPF para cada usuário da lista

            Listar contas

"""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saque = 0
limite_saque = 500
historico_transacao = []
numero_saques = 0
LIMITE_SAQUES = 3


def numero_positivo(num: float) -> bool:
    """Função verifica se o número é positivo.

    Args:
        num (float): _description_

    Returns:
        bool: _description_
    """
    if num > 0:
        return True
    else:
        return False


def deposito(valor: float, saldo: float, extrato: str):
    if not numero_positivo(valor):
        print('Depositos devem ser números positivos')
        return 'Depositos devem ser números positivos'
    if numero_positivo(valor):
        saldo += valor
        historico_transacao.append((datetime.now(), valor))
        return valor, saldo


def saldo(historico_transacao: list):
    return sum(tupla[1] for tupla in historico_transacao)


def saque(extrato: list):
    numero_saques += 1
    if numero_saques > LIMITE_SAQUES:
        print('Sque não permitito. Limite de três saques diários.')

    else:
        valor_saque = float(input('Valor do saque: '))
        if valor_saque > limite_saque:
            print('Saque indisponivel. Valor solicitado maior que o permitido.')
        if valor_saque > saldo:
            print('Saldo indisponivel.')
        else:
            saldo -= valor_saque
            extrato.append(-valor_saque)
    return (saldo, extrato)


def extrato(historico_transacao: list):
    if not historico_transacao:
        print('Não há registro de transações na conta.')
    
    print('Extrato Conta Bancaria')
    [print(f'{v[0].strftime('%H:%M:%S')} R$ {v[1]:.2f}') for v in historico_transacao]

    print(f'Saldo: R$ {saldo(historico_transacao)}')
