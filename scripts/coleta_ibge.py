# Coleta da população dos municípios do Rio Grande do Sul
# Fonte: IBGE, Censo Demográfico 2022, tabela 4709 do SIDRA (população residente)
# Os dados do IBGE são públicos e podem ser usados citando a fonte
#
# Essa população serve para comparar os municípios de forma justa,
# por exemplo, calculando as pessoas atingidas a cada 100 mil habitantes.
#
# Como rodar, a partir da pasta principal do projeto:  python scripts/coleta_ibge.py

import requests
import json

# Endereço da API do SIDRA: tabela 4709, todos os municípios do RS (código 43), variável 93 (população), ano 2022
url = "https://apisidra.ibge.gov.br/values/t/4709/n6/in%20n3%2043/v/93/p/2022"

# Pasta e nome do arquivo onde os dados ficam guardados
caminho = "dados/originais/ibge_populacao_rs_2022.json"

try:
    resposta = requests.get(url)

    # O código 200 indica que os dados foram recebidos corretamente
    if resposta.status_code == 200:
        dados = resposta.json()

        municipios = []

        # A primeira linha da resposta é só o cabeçalho, por isso o for começa na segunda (dados[1:])
        for m in dados[1:]:
            municipios.append({
                "codigo_municipio": m.get("D1C"),
                "municipio": m.get("D1N"),
                "populacao_2022": int(m.get("V"))
            })

        # Salva a lista de municípios em JSON, mantendo os acentos
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(municipios, arquivo, ensure_ascii=False, indent=4)

        print("Municipios salvos:", len(municipios))

    else:
        print("Erro:", resposta.status_code)

except:
    print("Erro: não foi possível se comunicar com a API do IBGE.")
