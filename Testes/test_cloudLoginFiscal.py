import Utilitarios.Login as Login

def test_cloudLoginFiscal(set_up):
    page = set_up
    Login.LoginCloudFiscal(page, 'administrador@AcessoFiscalCloud', 'masterkey', '9999', '1')
    Login.SairCloud(page)
    page.close()

