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
            Depositar
                Argumentos (positional only):
                    saldo, valor, extrato
                Retorno:
                    saldo e extrato
            Sacar:
                Argumentos (keyword only):
                    saldo, valor, extrato, limite,
                    numero_saque, limite_saque
                Retorno:
                    saldo, extrato
            Visualizar historico (extrato):
                Argumentos (positional only e keyword only):
                    posicionais: saldo
                    nomeados: extrato
                Retorno:
                    Imprimir o extrato

        Criar duas funções:
            Criar usuário (cliente do banco):
                Armazenar em uma lista (nome,
                data nascimento, cpf, endereço)

                Endereço é uma string com formato: logradouro,
                numero - bairro - vidade/sigla estado.
                Armazenar somente os numeros do CPF. Retirar pontos e traço
                CPF é unique (não cadastrar 2 CPF)

            Criar conta corrente:
                Conta é composta por: agencia, numero da conta e usuario
                Número da conta é sequencial iniciando em 1
                Número da Agencia é fixo: '0001'
                Usuário pode ter mais de uma conta, mas uma conta
                pertence a somente um usuário.

                Dica: Para vincular usuário a uma conta, filtre a lista
                de usuários buscando o numero do CPF para cada usuário da lista

            Listar contas

"""


sacar = 0
limite_saque = 500
historico_trasacao = []
numero_saques = 0
LIMITE_SAQUES = 3


def menu(escolha=None):
    print('\n Escolha a opção desejada:')
    menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    """
    return menu


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


def depositar(valor: float, saldo: float, historico_transacao: list = historico_trasacao):
    """Função para depositar dinheiro na conta

    Args:
        Todos devem ser positional only
        valor (float): Valor financeiro para ser depositado em conta
        saldo (float): Valor financeiro existente em conta
        extrato (str): Histórico de transações na conta

    Returns:
        _type_: _description_
    """

    if numero_positivo(valor):
        saldo += valor
        historico_transacao.append((datetime.now(), valor))
        return valor, saldo
    else:
        return 'Não é um valor a ser creditado em conta.'


def exibir_extrato(historico_transacao: list = historico_trasacao) -> None:
    txt_cabecalho = '============ Extrato Conta Bancária ============'
    len_cabecalho = len(txt_cabecalho)
    rodape = '=' * len_cabecalho

    cabecalho = print(f'\n{rodape}\n{txt_cabecalho}\n{rodape}')

    if not historico_transacao:
        cabecalho
        print('\n    Não há registro de transações na conta')
        print('\n')
        print(rodape)
        print('\n ')

    if historico_transacao:
        cabecalho
        for v in historico_transacao:
            data_hora = v[0].strftime('%d/%m/%Y %H:%M:%S')
            valor_ = f'R$: {v[1]:.2f}'
            valor = f'{valor_:>28}'
            print(f'{data_hora} {valor}')
        print(rodape)

        saldo = f'Saldo: R$ {exibir_saldo(historico_transacao)}'
        print(f'{saldo:>48}')
        print(rodape)


def sacar(
    saldo: float,
    valor_saque: float,
    qtd_operacao_saque_dia: int,
    limite_valor_saque_operacao: float,
    historico_trasacao: list = historico_trasacao,
) -> str:
    """Função para realizar saque em conta bancária
        Requisitos:
        Limite de 3 saques diários
        Limite no valor do saque de R$ 500,00
        Não havendo saldo, retornar uma msg informando que não há saldo para o saque

    Args (keyword only - chave valor):
        saldo (float): Montante financeira do cliente disponivel para
                    operações de saque, pagamentos.
        valor_saque (float): Financeiro solicitado para sacar.
        extratohistorico_transacao (str): Impressão do hitorico de transações na conta.
        qtd_operacao_saque_dia (int): Número de operações de saque por dia
        limite_valor_saque_operacao (float): Valor máximo para sacar no dia.

    Returns:
        str: Extrato impresso.
    """

    excedeu_saldo = valor_saque > saldo
    excedeu_qtd_operacao_saque_dia = qtd_operacao_saque_dia > LIMITE_SAQUES
    excedeu_valor_saque = valor_saque > limite_valor_saque_operacao

    if excedeu_valor_saque:
        print('Saque indisponivel. Valor solicitado maior que o permitido.')
        return 'Saque indisponivel. Valor solicitado maior que o permitido.'

    elif excedeu_saldo:
        print('Saldo indisponivel.')
        return 'Saldo indisponível.'

    elif excedeu_qtd_operacao_saque_dia:
        print('Limite de três saques diários.')
        return 'Limite de três saques diários.'

    else:
        saldo -= valor_saque
        historico_trasacao.append((datetime.now(), -valor_saque))
        qtd_operacao_saque_dia += 1

    # print(exibir_extrato(extrato))
    return saldo


def exibir_saldo(historico_transacao: list = historico_trasacao):
    if historico_transacao:
        return sum(tupla[1] for tupla in historico_transacao)
    else:
        return 0.0


def criar_usuario(usuario: str):
    return NotImplemented


def criar_conta_corrente(usuario: str):
    return NotImplemented
