from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate_company_product_list(list_of_dicts):
        companies = Counter(
            [dict["nome_da_empresa"] for dict in list_of_dicts]
        )
        report = [
            f"- {company}: {companies[company]}" for company in companies
        ]
        return "\n".join(report)

    @staticmethod
    def generate(list_of_dicts):
        return (
            f"{SimpleReport.generate(list_of_dicts)}\n"
            f"Produtos estocados por empresa:\n"
            f"{CompleteReport.generate_company_product_list(list_of_dicts)}\n"
        )
