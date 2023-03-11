import Utilitarios.Login as Login
from Testes.nFpaFerias.Utilitarios .simularFerias import simularFerias


def test_nFpaRelatorioSimulacaoFerias(set_up):
    page = set_up
    Login.LoginCloudFolha(page, 'administrador@CloudnFpaRelatorioSimulacaoFerias', 'masterkey', '1', '62',
                          '011900', '122100', '0001 - Indústria e Comércio de Confecções Flor Azul Ltda')
    simularFerias(page=page, empresa='1', contrato='151', dataInicial='01062020', dataPgto='28052020', diasFerias='15',
                  diasAbono='0', diasPremio='0', abonoInicioFerias='Não', pagaAdt13='Não', descontaAdt='Não',
                  calcularDescSindicato='Não')
    Login.SairCloud(page)
    page.close()
