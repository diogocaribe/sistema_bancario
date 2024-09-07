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
        saldo=conta_info_sacar['saldo'],
        valor_saque=conta_info_sacar['valor_saque'],
        extrato=conta_info_sacar['extrato'],
        qtd_operacao_saque_dia=conta_info_sacar['qtd_operacao_saque_dia'],
        limite_valor_saque_operacao=conta_info_sacar['limite_valor_saque_operacao']
    )

    assert resultado == 800.0


def test_excedeu_valor_saque(conta_info_sacar):
    valor_saque = 600.00
    resultado = sacar(
        saldo=conta_info_sacar['saldo'],
        valor_saque=valor_saque,
        extrato=conta_info_sacar['extrato'],
        qtd_operacao_saque_dia=conta_info_sacar['qtd_operacao_saque_dia'],
        limite_valor_saque_operacao=conta_info_sacar['limite_valor_saque_operacao']
    )

    assert resultado == 'Saque indisponivel. Valor solicitado maior que o permitido.'


def test_excedeu_saldo(conta_info_sacar):
    saldo = 100.00
    resultado = sacar(
        saldo=saldo,
        valor_saque=conta_info_sacar['valor_saque'],
        extrato=conta_info_sacar['extrato'],
        qtd_operacao_saque_dia=conta_info_sacar['qtd_operacao_saque_dia'],
        limite_valor_saque_operacao=conta_info_sacar['limite_valor_saque_operacao']
    )

    assert resultado == 'Saldo indisponível.'


def test_excedeu_num_operacao(conta_info_sacar):
    qtd_operacao_saque_dia=4
    resultado = sacar(
        saldo=conta_info_sacar['saldo'],
        valor_saque=conta_info_sacar['valor_saque'],
        extrato=conta_info_sacar['extrato'],
        qtd_operacao_saque_dia=qtd_operacao_saque_dia,
        limite_valor_saque_operacao=conta_info_sacar['limite_valor_saque_operacao']
    )

    assert resultado == 'Limite de três saques diários.'
