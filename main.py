import csv


#pondo os headers em nome de colunas separadas por lista
headers_empresa = ["cnpj","razaosocial_nomeempresarial","naturezajuridica","qualifresponsavel","capitalsocial","porteempresa","entefederativo"]
headers_socios = ["cnpj","identifsocio","nomesocio_razaosocial","cnpj_cpfsocio","qualifsocio","dataentradasocied","pais","reprlegal","nomerepr","qualifreprlegal","faixaetaria"]
headers_estabelecimentos = ["cnpj", "cnpjordem", "cnpjdv", "identifmatriz_filial", "nomefantasia","situcadastral", "datasitucadastral","motivositucadastral","nomecidadeexterior", "pais","datainicioatvd","cnaefiscalprincip","cnaefiscsecund","tipologradouro","logradouro","numero","complemento","bairro","cep","uf","municipio"]

nrows = 100000
src = "K3241.K03200Y9.D30513.SOCIO.csv"
dst = "socios_file_dest.csv"
headers = headers_socios

print(f"Gerando CSV de {dst.split('_')[0].upper()} com {nrows} linhas a partir do arquivo {src.split('.')[-2]}")

with open(src, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    with open(dst, "w") as out:
        writer = csv.writer(out)
        writer.writerow(headers)
        for row in reader:
            writer.writerow(row)
            nrows -= 1
            if nrows == 0:
                break        