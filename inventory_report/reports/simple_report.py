from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, invetory):
        today = str(date.today())

        date_fabric = min(
            [
                item["data_de_fabricacao"]
                for item in invetory
            ]
        )
        date_valid = min(
            [
                item["data_de_validade"]
                for item in invetory
                if item["data_de_validade"] >= today
            ]
        )
        firm_name = max(
            item["nome_da_empresa"]
            for item in invetory
        )

        return(
            f"Data de fabricação mais antiga: {date_fabric}\n"
            f"Data de validade mais próxima: {date_valid}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{firm_name}\n"
        )
