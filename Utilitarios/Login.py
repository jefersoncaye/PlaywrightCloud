import os
import time
import psutil as ps
from playwright.sync_api import expect
from Utilitarios.acoesPersonalizadas import AcoesPersonalizadas
from PageObjects.login import LoginObjects

def IniciarNHtml(caminhoExe):
    for proc in ps.process_iter():
        info = proc.as_dict(attrs=['pid', 'name'])
        if info['name'] == 'nHttp.exe':
            print("nHttp.exe aberto, Fechando..")
            os.system('taskkill /im nHttp.exe')
    print(f"Abrindo {caminhoExe}")
    os.startfile(caminhoExe)

def FecharNHtml():
    for proc in ps.process_iter():
        info = proc.as_dict(attrs=['pid', 'name'])
        if info['name'] == 'nHttp.exe':
            print("Fechando nHttp.exe")
            os.system('taskkill /im nHttp.exe')


def SairCloud(page):
    ap = AcoesPersonalizadas(page)
    loginObjects = LoginObjects(page)
    ap.click(loginObjects.fotoUsuario, 'Foto Usuario')
    ap.click(loginObjects.botaoSair, 'Sair')
    expect(loginObjects.botaoEntrar).to_be_enabled()
    FecharNHtml()

def LoginCloudFiscal(page,usuario, senha, empresa, filial):
    ap = AcoesPersonalizadas(page)
    loginObjects = LoginObjects(page)
    IniciarNHtml('D:\\workspace\\Tributario\\nHttp.exe')
    print(f'\nFazendo Login conexao: {usuario}, senha: {senha}')
    ap.navegar("http://localhost:8080/home/Inicio")
    while page.is_visible('[class="cookies-title"]',timeout = 5000):
        ap.click(loginObjects.botaoPermitir, 'Permitir Cookies ')
    ap.fill(loginObjects.usuario,usuario)
    ap.fill(loginObjects.senha, senha)
    ap.click(loginObjects.botaoEntrar, "Entrar")
    page.wait_for_load_state()
    ap.click(loginObjects.botaoAcessarFiscal, 'Fiscal')
    page.wait_for_load_state()
    ap.fill(loginObjects.empresa, empresa)
    ap.press(loginObjects.empresa, "Enter")
    time.sleep(1)
    ap.fill(loginObjects.filial,filial)
    ap.press(loginObjects.filial, "Enter")
    ap.click(loginObjects.botaoSelecionar, 'Selecionar')
    ap.expectContainsText(loginObjects.cabecalhoDadosEmpresa,'9999 - Empresa Padrão Questor Sistemas - SC')


def LoginCloudFolha(page,usuario, senha, empresa, periodoCalculo, dataInicial, dataFinal,
                    descicaoEmpresa='9999 - Empresa Padrão Questor Sistemas - SC'):
    ap = AcoesPersonalizadas(page)
    loginObjects = LoginObjects(page)
    IniciarNHtml('D:\\workspace\\Tributario\\nHttp.exe')
    print(f'\nFazendo Login conexao: {usuario}, senha: {senha}')
    ap.navegar("http://localhost:8080/home/Inicio")
    while page.is_visible('[class="cookies-title"]',timeout = 5000):
        ap.click(loginObjects.botaoPermitir, 'Permitir Cookies ')
    ap.fill(loginObjects.usuario,usuario, 'Usuario')
    ap.fill(loginObjects.senha, senha, 'Senha')
    ap.click(loginObjects.botaoEntrar, "Entrar")
    page.wait_for_load_state()
    ap.click(loginObjects.botaoAcessarFolha, 'Folha')
    page.wait_for_load_state()
    ap.dblclick(loginObjects.empresa, 'Empresa')
    ap.fill(loginObjects.empresa, empresa, 'Empresa')
    ap.press(loginObjects.empresa, "Enter")
    time.sleep(1)
    ap.fill(loginObjects.periodoCalculo,periodoCalculo, 'Periodo de Calculo')
    ap.press(loginObjects.periodoCalculo, "Enter")
    ap.type(loginObjects.dataInicial, dataInicial, 'Data Inicial')
    ap.type(loginObjects.dataFinal, dataFinal, 'Data Final')
    ap.click(loginObjects.botaoSelecionar, 'Selecionar')
    ap.expectContainsText(loginObjects.cabecalhoDadosEmpresa, descicaoEmpresa)
