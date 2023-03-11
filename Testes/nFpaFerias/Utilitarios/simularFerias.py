from Utilitarios.acoesPersonalizadas import AcoesPersonalizadas
from PageObjects.nFpaFerias.nfpaRRSimulaFerias import NfpaRRSimulaFeriasObjects

def simularFerias(page, empresa='', contrato='', dataInicial='', dataPgto='', diasFerias='', diasAbono='', diasPremio='',
                  abonoInicioFerias='', pagaAdt13='', descontaAdt='', calcularDescSindicato=''):
    ap = AcoesPersonalizadas(page)
    nfpaRRSimulaFeriasObjects = NfpaRRSimulaFeriasObjects(page)
    ap.navegar('http://localhost:8080/npmnFpa/Relatorio?Scope={Class:%22nfpaRRSimulaFerias%22}')
    ap.fill(nfpaRRSimulaFeriasObjects.empresa, empresa, 'Empresa')
    ap.fill(nfpaRRSimulaFeriasObjects.contrato, contrato, 'Contrato')
    ap.type(nfpaRRSimulaFeriasObjects.dataInicial, dataInicial, 'Data Inicial')
    ap.type(nfpaRRSimulaFeriasObjects.dataPgto, dataPgto, 'Data Pagamento')
    ap.fill(nfpaRRSimulaFeriasObjects.diasFerias, diasFerias, 'Dias Ferias')
    ap.fill(nfpaRRSimulaFeriasObjects.diasAbono, diasAbono, 'Dias Abono')
    ap.fill(nfpaRRSimulaFeriasObjects.diasPremio, diasPremio, 'Dias Premio')
    ap.selectOption(nfpaRRSimulaFeriasObjects.abonoInicioFerias, abonoInicioFerias, 'Abono é no Inicio Ferias')
    ap.selectOption(nfpaRRSimulaFeriasObjects.pagaAdt13, pagaAdt13, 'Paga Adiantamento de 13°')
    ap.selectOption(nfpaRRSimulaFeriasObjects.descontarAdt, descontaAdt, 'Descontar Adiantamentos')
    ap.selectOption(nfpaRRSimulaFeriasObjects.calcularDescSindicato, calcularDescSindicato, 'Calcular Descontos Sindicais')
    ap.click(nfpaRRSimulaFeriasObjects.botaoExecutar, 'Executar')
