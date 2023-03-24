from inventory_report.reports.colored_report import ColoredReport

# from inventory_report.inventory.inventory import Inventory


class MockInventory:
    @staticmethod
    def generate(fake_parameter):
        return (
            "Data de fabricação mais antiga: 2020-09-06\n"
            "Data de validade mais próxima: 2023-09-17\n"
            "Empresa com mais produtos: Target Corporation"
        )


line1 = (
    "\x1b[32mData de fabricação mais antiga:\x1b[0m "
    "\x1b[36m2020-09-06\x1b[0m\n"
)
line2 = (
    "\x1b[32mData de validade mais próxima:\x1b[0m "
    "\x1b[36m2023-09-17\x1b[0m\n"
)
line3 = (
    "\x1b[32mEmpresa com mais produtos:\x1b[0m "
    "\x1b[31mTarget Corporation\x1b[0m"
)


output = f"{line1}" f"{line2}" f"{line3}"


def test_decorar_relatorio():
    assert ColoredReport(MockInventory).generate("aaa") == output
