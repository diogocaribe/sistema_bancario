import pytest


@pytest.fixture
def setup_sacar():
    return {
        'saldo': 1000.0,
        'valor_saque': 200.0,
        'extrato': [],
        'qtd_operacao_saque_dia': 1,
        'limite_valor_saque_operacao': 500.0,
    }

@pytest.fixture
def setup_depositar():
    return {
        'valor': 100.0,
        'saldo': 500.0,
        'historico_transacao': [400.00, 100.00]
    }
