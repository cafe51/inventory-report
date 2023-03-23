from datetime import datetime, date
from collections import Counter


class SimpleReport:
    @staticmethod
    def string_to_date(date):
        return datetime.strptime(str(date), "%Y-%m-%d").date()

    @staticmethod
    def oldest_fab(list_of_dicts):
        fab = [
            SimpleReport.string_to_date(dict["data_de_fabricacao"])
            for dict in list_of_dicts
        ]
        oldest_date = min(fab)
        return str(oldest_date)

    @staticmethod
    def nearest_due(list_of_dicts):
        today = date.today()
        fab_list = []
        for dict in list_of_dicts:
            if SimpleReport.string_to_date(dict["data_de_validade"]) > today:
                fab_list.append(
                    SimpleReport.string_to_date(dict["data_de_validade"])
                )
        nearest_date = min(fab_list)
        return nearest_date
        # return f'todas = {fab_list} e a menor é = {str(nearest_date)}'

    @staticmethod
    def top_prod_company(list_of_dicts):
        companies = Counter(
            [dict["nome_da_empresa"] for dict in list_of_dicts]
        )
        max_total_product = max(companies.values())
        company_with_max_quantity_of_products = ""

        for company in companies:
            if companies[company] == max_total_product:
                company_with_max_quantity_of_products = company

        return company_with_max_quantity_of_products

    @staticmethod
    def generate(list_of_dicts):
        oldest_fab = SimpleReport.oldest_fab(list_of_dicts)
        nearest_due = SimpleReport.nearest_due(list_of_dicts)
        top_prod_company = SimpleReport.top_prod_company(list_of_dicts)
        return (
            f"Data de fabricação mais antiga: {oldest_fab}\n"
            f"Data de validade mais próxima: {nearest_due}\n"
            f"Empresa com mais produtos: {top_prod_company}"
        )
