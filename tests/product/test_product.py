from inventory_report.inventory.product import Product
from datetime import date


def test_cria_produto():
    today = date.today()
    product = Product(
        12,
        'ventilador',
        'Mondial',
        today,
        today,
        '123456',
        'em local ventilado',
    )

    assert product.id == 12
    assert product.nome_do_produto == 'ventilador'
    assert product.nome_da_empresa == 'Mondial'
    assert product.data_de_fabricacao == str(today)
    assert product.data_de_validade == str(today)
    assert product.numero_de_serie == '123456'
    assert product.instrucoes_de_armazenamento == 'em local ventilado'
