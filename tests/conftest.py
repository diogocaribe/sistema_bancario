import pytest


@pytest.fixture
def conta_info_sacar():
    return {
        'saldo': 1000.0,
        'valor_saque': 200.0,
        'extrato': [],
        'qtd_operacao_saque_dia': 1,
        'limite_valor_saque_operacao': 500.0,
    }
