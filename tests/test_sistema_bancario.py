from sistema_bancario.sistema_bancario import numero_positivo, depositar, exibir_saldo, menu, sacar

_saldo = 10
extrato = [10]
valor = 10


def test_numero_positivo_positivo():
    assert numero_positivo(10) is True


def test_numero_positivo_zero():
    assert numero_positivo(0) is False


def test_numero_positivo_negativo():
    assert numero_positivo(-5) is False


def test_numero_positivo_float_positivo():
    assert numero_positivo(3.14) is True


def test_numero_positivo_float_negativo():
    assert numero_positivo(-1.23) is False


def test_deposito_numero_negativo():
    assert depositar(valor, _saldo, extrato) == 'Depositos devem ser números positivos'


def test_deposito_numero_positivo():
    assert depositar(valor, _saldo, extrato) == (10, 20)


def test_saldo_unica_transacao():
    assert _saldo == exibir_saldo(extrato)


def test_menu(mocker):
    # Mockar `input`, mas a entrada não afeta o resultado.
    mocker.patch('builtins.input', return_value='')
    result = menu()
    expected_result = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    """
    assert result == expected_result


def test_sacar_sucesso(conta_info_sacar):

    resultado = sacar(
        saldo=['saldo_inicial'],
        valor_saque=['valor_saque'],
        extrato=['extrato'],
        qtd_saque_dia=['numero_saque'],
        limite_saque_dia=['limite_valor_saque_diario'],
        limite_saque_operacao=['limite_valor_saque_operacao'],
    )

    assert resultado == 800.0


def test_limite_saques_diarios():
    saldo_inicial = 1000.0
    valor_saque = 200.0
    extrato = []
    numero_saque = 3
    limite_valor_saque_diario = 1000.0
    limite_valor_saque_operacao = 500.0

    resultado = sacar(
        saldo=saldo_inicial,
        valor_saque=valor_saque,
        extrato=extrato,
        numero_saques=numero_saques,
        limite_saque_dia=limite_valor_saque_diario,
        limite_saque_operacao=limite_valor_saque_operacao,
    )

    assert resultado == 'Saque não permitido. Limite de três saques diários.'


def test_valor_saque_excede_limite():
    saldo_inicial = 1000.0
    valor_saque = 600.0
    extrato = []
    numero_saques = 1
    limite_valor_saque_diario = 1000.0
    limite_valor_saque_operacao = 500.0

    resultado = sacar(
        saldo=saldo_inicial,
        valor_saque=valor_saque,
        extrato=extrato,
        numero_saques=numero_saques,
        limite_saque_dia=limite_valor_saque_diario,
        limite_saque_operacao=limite_valor_saque_operacao,
    )

    assert resultado == 'Saque indisponível. Valor solicitado maior que o permitido.'


def test_saldo_insuficiente():
    saldo_inicial = 100.0
    valor_saque = 200.0
    extrato = []
    numero_saques = 1
    limite_valor_saque_diario = 1000.0
    limite_valor_saque_operacao = 500.0

    resultado = sacar(
        saldo=saldo_inicial,
        valor_saque=valor_saque,
        extrato=extrato,
        numero_saques=numero_saques,
        limite_saque_dia=limite_valor_saque_diario,
        limite_saque_operacao=limite_valor_saque_operacao,
    )

    assert resultado == 'Saldo indisponível.'
