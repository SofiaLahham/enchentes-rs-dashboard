# Coleta do nível do Guaíba medido na estação do Cais Mauá, em Porto Alegre
# Fonte: Agência Nacional de Águas e Saneamento Básico (ANA), serviço de dados hidrometeorológicos
# Estação: Cais Mauá C6, código 87450004, a régua oficial do nível do Guaíba em Porto Alegre
# Os dados da ANA são públicos e podem ser usados citando a fonte
#
# A estação mede o nível do rio a cada 15 minutos. Os dados são pedidos um ano por vez,
# de 2014 (quando a estação começou a medir) até 2025.
#
# Como rodar, a partir da pasta principal do projeto:  python scripts/coleta_ana.py

import requests
import json
import time
from bs4 import BeautifulSoup

# Pasta e nome do arquivo onde os dados ficam guardados
caminho = "dados/originais/ana_nivel_cais_maua.json"

medicoes = []   # lista onde todas as medições são guardadas

for ano in range(2014, 2026):
    # Endereço do serviço da ANA, pedindo as medições da estação do primeiro ao último dia do ano
    url = "https://telemetriaws1.ana.gov.br/ServiceANA.asmx/DadosHidrometeorologicos?codEstacao=87450004&DataInicio=01/01/" + str(ano) + "&DataFim=31/12/" + str(ano)

    # O servidor da ANA às vezes falha, então cada ano é tentado até 3 vezes
    for tentativa in range(3):
        try:
            resposta = requests.get(url)

            # O código 200 indica que os dados foram recebidos corretamente
            if resposta.status_code == 200:
                # A resposta vem em XML, que é lido com o BeautifulSoup
                soup = BeautifulSoup(resposta.text, "html.parser")
                registros = soup.find_all("dadoshidrometereologicos")   # cada registro é uma medição

                quantidade_no_ano = 0
                for registro in registros:
                    nivel = registro.find("nivel").get_text().strip()

                    # Guarda só as medições que têm o nível preenchido
                    if nivel != "":
                        medicoes.append({
                            "data_hora": registro.find("datahora").get_text().strip(),
                            "nivel_cm": float(nivel)
                        })
                        quantidade_no_ano = quantidade_no_ano + 1

                print("Ano", ano, "- medicoes coletadas:", quantidade_no_ano)
                break   # deu certo, então não precisa tentar de novo

            else:
                print("Ano", ano, "- erro:", resposta.status_code, "- tentando de novo")

        except:
            print("Ano", ano, "- erro: não foi possível se comunicar com a ANA - tentando de novo")

        time.sleep(5)   # espera 5 segundos antes de tentar de novo

    # Espera 1 segundo entre um ano e outro, para não sobrecarregar o servidor da ANA
    time.sleep(1)

# Salva todas as medições em JSON
# Sem o indent, porque são muitas medições e o arquivo ficaria muito grande
with open(caminho, "w", encoding="utf-8") as arquivo:
    json.dump(medicoes, arquivo, ensure_ascii=False)

print("Total de medicoes salvas:", len(medicoes))
