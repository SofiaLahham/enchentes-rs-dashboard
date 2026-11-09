# Enchentes no RS: dashboard interativo

Dashboard interativo sobre as enchentes no Rio Grande do Sul. Mostra, bairro a bairro,
quais áreas de Porto Alegre e quantas pessoas são afetadas conforme o nível do Guaíba
sobe, e compara os municípios do RS atingidos na enchente de maio de 2024.

## O problema
Em maio de 2024, o Guaíba chegou a 5,35 m, a maior marca da história.
A ferramenta atual que mostra a simulação de alagamento é lenta e instável,
o que dificulta o acesso da defesa civil, da imprensa e dos moradores.

## O que o dashboard responde
- **Simulação (Porto Alegre):** se o rio chegar a X metros, quais bairros e quantas pessoas são afetados?
- **Contexto (Porto Alegre e RS):** que escolas e unidades de saúde ficam alagadas, com que
  frequência o Guaíba chega a esses níveis e quais municípios do RS foram mais atingidos em 2024.

## Dados
| Fonte | Conteúdo | Recorte | Coleta |
|---|---|---|---|
| INCT SiMAI | Simulação de alagamento por bairro (3 m a 10 m) | Porto Alegre | Arquivo JSON |
| UFRGS (Zenodo) | Pessoas, escolas e unidades de saúde atingidas por município | Região do Guaíba (RS), maio/2024 | API |
| ANA | Nível do Guaíba na estação do Cais Mauá | Porto Alegre, 2014–2025 | API |
| IBGE (SIDRA) | População por município | RS, Censo 2022 | API |

## Tecnologias
Python · pandas · requests · plotly

## Dashboard
Em construção.

## Como rodar
Em construção.

## Equipe
- Sofia
- Bernardo
