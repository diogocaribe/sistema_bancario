import pytest


@pytest.fixture
def conta_info_sacar():
    return {
        'saldo_inicial': 1000.0,
        'valor_saque': 200.0,
        'extrato': [],
        'numero_saque': 1,
        'limite_valor_saque_diario': 1000.0,
        'limite_valor_saque_operacao': 500.0,
    }
