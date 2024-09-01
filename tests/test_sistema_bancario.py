from sistema_bancario.sistema_bancario import numero_positivo, deposito, saldo

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
    assert deposito(valor, _saldo, extrato) == 'Depositos devem ser números positivos'


def test_deposito_numero_positivo():
    assert deposito(valor, _saldo, extrato) == (10, 20)


def test_saldo_unica_transacao():
    assert _saldo == saldo(extrato)
