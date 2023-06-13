import csv

nrows = 15000

#pondo os headers em nome de colunas separadas por lista
headers_empresa = ["cnpj","razaosocial_nomeempresarial","naturezajuridica","qualifresponsavel","capitalsocial","porteempresa","entefederativo"]
headers_socios = ["cnpj","identifsocio","nomesocio_razaosocial","cnpj_cpfsocio","qualifsocio","dataentradasocied","pais","reprlegal","nomerepr","qualifreprlegal","faixaetaria"]
headers_estabelecimentos = ["cnpj", "cnpjordem", "cnpjdv", "identifmatriz_filial", "nomefantasia","situcadastral", "datasitucadastral","motivositucadastral","nomecidadeexterior", "pais","datainicioatvd","cnaefiscalprincip","cnaefiscsecund","tipologradouro","logradouro","numero","complemento","bairro","cep","uf","municipio"]
with open('K3241.K03200Y9.D30513.ESTABELE.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    with open("estabelecimentos_file_dest.csv", "w") as out:
        writer = csv.writer(out)
        writer.writerow(headers_estabelecimentos)
        for row in reader:
            writer.writerow(row)
            nrows -= 1
            if nrows == 0:
                break        