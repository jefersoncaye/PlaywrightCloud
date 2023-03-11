from playwright.sync_api import expect

class AcoesPersonalizadas:

    def __init__(self, page):
        self.page = page

    def navegar(self, url):
        self.page.on("console", print(f'navegando para a pagina: {url}'))
        self.page.goto(url)

    def click(self, elemento, localClicado = ''):
        if localClicado == '':
            localClicado = elemento
        self.page.on("console", print(f'clicando em/no: {localClicado}'))
        elemento.click()

    def dblclick(self, elemento, localClicado = ''):
        if localClicado == '':
            localClicado = elemento
        self.page.on("console", print(f'clicando duas vezes em/no: {localClicado}'))
        elemento.dblclick()

    def press(self, elemento, tecla):
        self.page.on("console", print(f'pressionando a tecla: {tecla}'))
        elemento.press(tecla)

    def type(self, elemento, valor, campo=''):
        self.page.on("console", print(f'escrevendo: {valor} no campo: {campo}'))
        elemento.type(valor)

    def fill(self, elemento, valor, campo=''):
        self.page.on("console", print(f'colando texto: {valor} no campo: {campo}'))
        elemento.fill(valor)

    def selectOption(self, elemento, valor, campo=''):
        self.page.on("console", print(f'Selecionando Opção: "{valor}" no campo: {campo}'))
        elemento.select_option(label=valor)

    def expectHaveText(self, elemento, valorEsperado, nomeObjetoAValidar = ''):
        if nomeObjetoAValidar == '':
            nomeObjetoAValidar = elemento
        self.page.on("console", print(f'Validando se o elemento: {nomeObjetoAValidar} possui o texto: \n"{valorEsperado}"\n'))
        expect(elemento).to_have_text(valorEsperado)

    def expectContainsText(self, elemento, valorEsperado, nomeObjetoAValidar = ''):
        if nomeObjetoAValidar == '':
            nomeObjetoAValidar = elemento
        self.page.on("console", print(f'Validando se o elemento: {nomeObjetoAValidar} possui o texto: \n"{valorEsperado}"\n'))
        expect(elemento).to_contain_text(valorEsperado)



