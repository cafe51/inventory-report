from inventory_report.inventory.product import Product


def test_relatorio_produto():
    output = (
        "O produto Farinha fabricado "
        "em 2021-02-18 por Farinini com validade até 2023-09-17 "
        "precisa ser armazenado ao abrigo de luz."
    )
    farinha = Product(
        1,
        "Farinha",
        "Farinini",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402",
        "ao abrigo de luz",
    )

    assert output == farinha.__repr__()
