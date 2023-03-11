class NfpaRRSimulaFeriasObjects:

    def __init__(self, page):
        self.page = page

    @property
    def empresa(self):
        return self.page.get_by_role("textbox", name="Empresa *")

    @property
    def contrato(self):
        return self.page.get_by_label("Contrato do Empregado  *")

    @property
    def dataInicial(self):
        return self.page.locator("#formFieldPDATAINICIALFERIASnfpaRRSimulaFerias").get_by_role("textbox", name="Data")

    @property
    def dataPgto(self):
        return self.page.locator("#formFieldPDATAPGTOnfpaRRSimulaFerias").get_by_role("textbox", name="Data")

    @property
    def diasFerias(self):
        return self.page.get_by_label("Dias de Férias  *")

    @property
    def diasAbono(self):
        return self.page.get_by_label("Dias Abono  *")

    @property
    def diasPremio(self):
        return self.page.get_by_label("Dias Prêmio  *")

    @property
    def abonoInicioFerias(self):
        return self.page.get_by_role("combobox", name="Abono é no Início das Férias *")

    @property
    def pagaAdt13(self):
        return self.page.get_by_role("combobox", name="Paga Adiantamento de 13º *")

    @property
    def descontarAdt(self):
        return self.page.get_by_role("combobox", name="Descontar Adiantamentos *")

    @property
    def calcularDescSindicato(self):
        return self.page.get_by_role("combobox", name="Calcular Descontos Sindicais *")

    @property
    def botaoExecutar(self):
        return self.page.get_by_role("button", name="o EXECUTAR")