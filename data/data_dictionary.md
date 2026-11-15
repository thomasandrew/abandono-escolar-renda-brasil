# Dicionário de dados

Fonte: dataset Kaggle **Taxa de abandono escolar por renda média no Brasil** (2013–2023). Os nomes e interpretações abaixo foram inferidos da estrutura fornecida; unidades monetárias, deflator e metodologia original da renda devem ser confirmados na fonte.

| Variável | Tipo | Descrição |
|---|---|---|
| Ano | inteiro | Ano de referência (2013–2023) |
| Unidade_Geografica | texto | Brasil, região ou unidade federativa |
| Regiao | texto | Região geográfica ou agregação Brasil |
| Localizacao | categoria | Total, Rural ou Urbana |
| Dependencia_Administrativa | categoria | Total, Pública, Privada, Municipal, Federal ou Estadual |
| Grupo_de_Abandono | categoria | Etapa ou ano escolar |
| Taxa_Abandono | decimal | Taxa de abandono em percentual; pode estar ausente |
| Renda_Media | inteiro | Indicador de renda média fornecido pelo dataset; unidade e metodologia não verificadas |

**Granularidade:** uma linha por combinação de ano, unidade geográfica, localização, dependência administrativa e grupo escolar. Há agregações sobrepostas (Brasil/regiões/estados e totais/subgrupos); não se deve calcular médias simples de todas as linhas para representar o país.

**Ausências:** preservadas como nulos, não substituídas por zero.

**Licenciamento:** MIT cobre somente o código deste repositório. O dataset de terceiros mantém sua licença original, a ser verificada no Kaggle antes de redistribuição ou atribuição de CC BY.
