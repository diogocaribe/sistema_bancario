import pytest
from datetime import datetime

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
    extrato = [
        (datetime(2024, 9, 1, 10, 0, 0), 100.00),
        (datetime(2024, 9, 2, 15, 30, 0), 10.00)
    ]
    return {
        'valor': 100.0,
        'saldo': 500.0,
        'extrato': extrato
    }
