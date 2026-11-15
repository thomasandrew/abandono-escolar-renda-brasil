# Abandono escolar e renda média no Brasil (2013–2023)

**Autor:** Thomas Andrew de Souza Batista  
**Instituição:** Unilasalle Niterói — Sistemas de Informação, 6º período  
**Disciplina:** Análise e Visualização de Dados com Python  
**Palavras-chave:** abandono escolar; renda média; Brasil; Python; dados abertos; FAIR.

## Objetivo
Analisar a evolução temporal do abandono escolar, diferenças entre Ensino Fundamental e Médio e associação descritiva com o indicador de renda média, sem inferir causalidade.

## Fonte
[Kaggle — Taxa de abandono escolar por renda média no Brasil](https://www.kaggle.com/datasets/joaoassaoka/taxa-de-abandono-escolar-por-renda-mdia-brasil). Arquivo recebido: `AbandonoEscolar_RendaMedia_2013_2023.csv`. Verifique termos de uso da fonte antes de republicar os dados.

## Como reproduzir
```bash
git clone URL_DO_SEU_REPOSITORIO
cd NOME_DO_REPOSITORIO
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m src.etl
```

O artigo está em `docs/index.html`. Para publicar: GitHub → Settings → Pages → Deploy from a branch → main → /docs. Substitua o link do GitHub no HTML após criar o repositório.

## Estrutura
- `data/raw/`: arquivo original; `data/processed/`: CSV comprimido tratado.
- `data/data_dictionary.md`: descrição das variáveis.
- `src/etl.py`: ETL reexecutável.
- `notebooks/analise_exploratoria.ipynb`: análise documentada.
- `docs/`: artigo HTML e gráficos.

## FAIR e licenças
Metadados e documentação no README; acesso público após publicação; formatos CSV e CSV.GZ; código MIT. A licença do dataset original não é substituída pela licença do código. Dependências com versões fixas em `requirements.txt`.

## Limitações
O indicador de renda não tem unidade e ajuste inflacionário comprovados na amostra fornecida; correlação temporal não demonstra causalidade. Totais e subgrupos se sobrepõem. Dados faltantes são mantidos.
