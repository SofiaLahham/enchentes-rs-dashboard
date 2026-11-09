# Coleta da tabela de municípios atingidos pela enchente de maio de 2024
# Fonte: Banco de dados das cheias na Região Hidrográfica do Lago Guaíba (UFRGS), publicado no Zenodo
# Licença: CC BY 4.0, que permite o uso citando a fonte
#
# A tabela traz, para cada um dos 139 municípios da região do Guaíba, as pessoas, os domicílios,
# as escolas e as unidades de saúde atingidas pela mancha de inundação observada em 6 de maio de 2024.
#
# Como rodar, a partir da pasta principal do projeto:  python scripts/coleta_ufrgs.py

import requests

# Endereço do arquivo na API do Zenodo
url = "https://zenodo.org/api/records/11185049/files/analise_ada_rhguaiba_municipios_10052024.csv/content"

# Pasta e nome do arquivo onde os dados ficam guardados
caminho = "dados/originais/ufrgs_municipios_2024.csv"

try:
    resposta = requests.get(url)

    # O código 200 indica que o arquivo foi recebido corretamente
    if resposta.status_code == 200:
        resposta.encoding = "utf-8"   # garante que os acentos dos nomes dos municípios sejam lidos corretamente

        # Salva o arquivo do jeito que veio, sem nenhuma alteração
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(resposta.text)

        print("Arquivo da UFRGS salvo em:", caminho)

    else:
        print("Erro:", resposta.status_code)

except:
    print("Erro: não foi possível se comunicar com o Zenodo.")
