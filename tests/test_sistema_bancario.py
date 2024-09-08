from sistema_bancario.sistema_bancario import (
    numero_positivo,
    depositar,
    menu,
    sacar,
    exibir_saldo,
)
from datetime import datetime

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


def test_deposito_numero_positivo():
    assert depositar(valor, _saldo, extrato) == (10, 20)


def test_menu(mocker):
    # Mockar `input`, mas a entrada não afeta o resultado.
    mocker.patch("builtins.input", return_value="")
    result = menu()
    expected_result = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
    """
    assert result == expected_result


def test_depositar(setup_depositar):
    resultado = depositar(
        setup_depositar["valor"], setup_depositar["saldo"], setup_depositar["extrato"]
    )

    assert resultado == (100.00, 600.00)


def test_depositar_num_negativo(setup_depositar):
    valor = -10.00
    resultado = depositar(valor, setup_depositar["saldo"], setup_depositar["extrato"])

    assert resultado == "Não é um valor a ser creditado em conta."


def test_exibir_extrato_sem_transacao(capsys):
    # esperado = None
    # resultado = exibir_extrato(historico_transacao=[])
    # assert resultado == esperado
    return NotImplemented


def test_sacar_sucesso(setup_sacar):
    resultado = sacar(
        saldo=setup_sacar["saldo"],
        valor_saque=setup_sacar["valor_saque"],
        historico_trasacao=setup_sacar["extrato"],
        qtd_operacao_saque_dia=setup_sacar["qtd_operacao_saque_dia"],
        limite_valor_saque_operacao=setup_sacar["limite_valor_saque_operacao"],
    )

    assert resultado == 800.0


def test_excedeu_valor_saque(setup_sacar):
    valor_saque = 600.00
    resultado = sacar(
        saldo=setup_sacar["saldo"],
        valor_saque=valor_saque,
        historico_trasacao=setup_sacar["extrato"],
        qtd_operacao_saque_dia=setup_sacar["qtd_operacao_saque_dia"],
        limite_valor_saque_operacao=setup_sacar["limite_valor_saque_operacao"],
    )

    assert resultado == "Saque indisponivel. Valor solicitado maior que o permitido."


def test_excedeu_saldo(setup_sacar):
    saldo = 100.00
    resultado = sacar(
        saldo=saldo,
        valor_saque=setup_sacar["valor_saque"],
        historico_trasacao=setup_sacar["extrato"],
        qtd_operacao_saque_dia=setup_sacar["qtd_operacao_saque_dia"],
        limite_valor_saque_operacao=setup_sacar["limite_valor_saque_operacao"],
    )

    assert resultado == "Saldo indisponível."


def test_excedeu_num_operacao(setup_sacar):
    qtd_operacao_saque_dia = 4
    resultado = sacar(
        saldo=setup_sacar["saldo"],
        valor_saque=setup_sacar["valor_saque"],
        historico_trasacao=setup_sacar["extrato"],
        qtd_operacao_saque_dia=qtd_operacao_saque_dia,
        limite_valor_saque_operacao=setup_sacar["limite_valor_saque_operacao"],
    )

    assert resultado == "Limite de três saques diários."


def test_exibir_saldo():
    resultado = exibir_saldo(
        historico_transacao=[(datetime(2024, 9, 1, 10, 0, 0), 100.00)]
    )
    esperado = 100
    assert resultado == esperado


def test_exibir_saldo_sem_transacao():
    resultado = exibir_saldo()
    esperado = 0.0
    assert resultado == esperado