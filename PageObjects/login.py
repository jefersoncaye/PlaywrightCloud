"""
Mapeamento da Tela http://localhost:8080/home/Inicio

Não adicionar eventos, apenas mapeamento
"""

class LoginObjects:

    def __init__(self, page):
        self.page = page

    @property
    def usuario(self):
        return self.page.get_by_placeholder("Usuário@Conexão")

    @property
    def senha(self):
        return self.page.get_by_placeholder("Senha")

    @property
    def botaoEntrar(self):
        return self.page.get_by_role("button", name="ENTRAR")

    @property
    def botaoAcessarFiscal(self):
        return self.page.get_by_role("link", name="Fiscal")

    @property
    def botaoAcessarFolha(self):
        return self.page.get_by_role("link", name="Folha de Pagamento")

    @property
    def empresa(self):
        return self.page.get_by_label("Empresa  *")

    @property
    def filial(self):
        return self.page.get_by_label("Filial  *")

    @property
    def periodoCalculo(self):
        return self.page.get_by_label("Período de Cálculo  *")

    @property
    def dataInicial(self):
        return self.page.get_by_role("textbox", name="Informe a competência inicial para filtro do movimento")

    @property
    def dataFinal(self):
        return self.page.get_by_role("textbox", name="Informe a competência final para filtro do movimento")

    @property
    def botaoSelecionar(self):
        return self.page.get_by_role("button", name="Selecionar")

    @property
    def cabecalhoDadosEmpresa(self):
        return self.page.locator('xpath=//*[@id="SelecaoEmpresaList"]/span[1]')

    @property
    def fotoUsuario(self):
        return self.page.locator(".symbol-label").first

    @property
    def botaoSair(self):
        return self.page.get_by_role("link", name=" Sair")

    @property
    def botaoPermitir(self):
        return self.page.get_by_role("button", name="Permitir")
