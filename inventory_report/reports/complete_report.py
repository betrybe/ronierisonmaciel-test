from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def get_companies_stock(cls, inventory):
        companies = [company["nome_da_empresa"] for company in inventory]
        companies_set = {
            company: companies.count(company) for company in companies
        }
        stock = []
        for company in companies_set.keys():
            stock.append({
                "nome_da_empresa": company,
                "quantidade": companies_set[company]
            })
        return stock

    @classmethod
    def generate(cls, invetory):
        report = (
            f"{super().generate(invetory)}"
            f"\nProdutos estocados por empresa: \n"
        )
        for company in cls.get_companies_stock(invetory):
            stk = list(company.values())
            report += f"- {stk[0]}: {stk[1]}\n"
        return report
