import Utilitarios.Login as Login

def test_cloudLoginFolha(set_up):
    page = set_up
    Login.LoginCloudFolha(page, 'administrador@AcessoFolhaCloud', 'masterkey', '9999', '1', '011900', '122100')
    Login.SairCloud(page)
    page.close()

