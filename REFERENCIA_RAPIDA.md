# Referência rápida do trabalho

## Por onde começo?

- Visão geral e status: [00_LEIA_PRIMEIRO.md](./00_LEIA_PRIMEIRO.md)
- Executar/reexecutar os scripts: [01_GUIA_PASSO_A_PASSO.md](./01_GUIA_PASSO_A_PASSO.md)
- Fórmulas, código e resultados: [02_REFERENCIA_TECNICA.md](./02_REFERENCIA_TECNICA.md)
- Contexto para agentes: [99_CONTEXT_PARA_AGENTES.md](./99_CONTEXT_PARA_AGENTES.md)
- Conceitos estatísticos: [GLOSSARIO_ESTATISTICO.md](./GLOSSARIO_ESTATISTICO.md)

## Fatos atuais

- Fonte original: IPTU 2026 de Porto Alegre, 876.248 registros e 32 colunas.
- População analítica: 876.243 registros, após remover 5 duplicatas exatas.
- Amostra: 1.066 registros, AAS sem reposição, semente 42.
- O pipeline 02–05 foi executado e gerou 4 arquivos intermediários e 9 CSVs em
  `saidas/`.
- Os painéis, o vídeo de até cinco minutos e os links acessíveis continuam
  pendentes conforme o [enunciado](./Enunciado.txt).

## Hipóteses implementadas

| Teste | Hipótese nula |
|-------|---------------|
| H1 — proporção de apartamentos | p = 0,40 |
| H2 — proporção de uso residencial | p = 0,85 |
| H3 — média do valor venal | μ = R$ 400.000 |
| H4 — média da área construída | μ = 100 m² |

O `p = 0,50` aparece somente na fórmula de dimensionamento amostral como
proporção conservadora; não é a hipótese nula de H1.

## Reexecutar o pipeline

Execute na ordem: `scripts/02_preparacao_dados.py` →
`scripts/03_amostragem.py` → `scripts/04_analise_descritiva.py` →
`scripts/05_inferencia_estatistica.py`.

Os resultados e decisões da execução atual estão na seção de inferência de
[02_REFERENCIA_TECNICA.md](./02_REFERENCIA_TECNICA.md).

**Atualizado:** 12/11/2026
