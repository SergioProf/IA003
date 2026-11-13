# SUMÁRIO EXECUTIVO — Preparação do Ambiente

> **Registro histórico da exploração inicial (07/11/2026).** As contagens de
> ausências e estatísticas desta seção descrevem a fonte original, antes da
> remoção das 5 duplicatas. O pipeline 02–05 foi executado desde então; consulte
> [00_LEIA_PRIMEIRO.md](./00_LEIA_PRIMEIRO.md) e
> [02_REFERENCIA_TECNICA.md](./02_REFERENCIA_TECNICA.md) para o estado atual.
> Os três painéis e o vídeo exigidos no enunciado continuam pendentes.

## Status inicial: ambiente preparado

**Data do registro:** 7 de novembro de 2026
**Hora:** ~15:45 (Brasília)  
**Prazo Final:** 15 de novembro de 2026 (8 dias úteis)

---

## 1. Validação da Base de Dados

### ✅ Dataset Confirmado
- **Arquivo:** `iptu_2026.csv`
- **Tamanho:** 210.53 MB
- **Total de registros:** 876.248 imóveis
- **Número de colunas:** 32 variáveis
- **Período:** 2026 (exercício completo)
- **Encoding:** UTF-8, separador `;` (ponto-e-vírgula)

### ✅ Estrutura de Dados Validada

#### Variáveis Quantitativas Principais
| Variável | Descrição | N Válido | Tipo |
|----------|-----------|----------|------|
| `vlr_venal_imovel` | Valor Venal do Imóvel (R$) | 876.205 | float |
| `mtr_area_construida_total` | Área Construída Total (m²) | 852.191 | float |
| `vlr_imposto` | IPTU (R$) | 876.205 | float |
| `vlr_aliquota` | Alíquota (%) | 876.205 | float |

#### Variáveis Qualitativas Principais
| Variável | Descrição | Valores Únicos | Ausências |
|----------|-----------|----------------|-----------|
| `des_finalidade` | Tipo de finalidade | N/A | 0 |
| `des_uso` | Classificação de uso | N/A | 24.152 (2.76%) |
| `nme_endloc_bairro_cdl` | Bairro | N/A | 507 (0.06%) |
| `num_divisao_fiscal` | Divisão Fiscal | 3 | 0 |

### ⚠️ Dados Faltantes Identificados

| Campo | Ausências | % |
|-------|-----------|---|
| `nivel` (Nível do imóvel) | 794.604 | 90.68% |
| `complemento` | 764.494 | 87.25% |
| `pavimento` | 402.407 | 45.92% |
| `num_endloc_unidade` (Unidade) | 164.022 | 18.72% |
| `des_endloc_tipo_unidade` (Tipo unidade) | 159.971 | 18.26% |
| `des_zona` (Zona) | 123.805 | 14.13% |
| `des_uso` (Uso) | 24.152 | **2.76%** ✓ Relevante |
| `mtr_area_construida_total` (Área) | 24.057 | **2.75%** ✓ Relevante |

**Nota:** As ausências altas em `nivel`, `complemento` e `pavimento` não afetam significativamente as análises planejadas.

### ⚠️ Anomalias Detectadas

1. **Duplicatas:** 5 linhas duplicadas encontradas (0.0006%) — negligenciável
2. **Valores Extremos:** Detectadas em valor venal e área construída (esperado em dados de leilão/cadastro)
3. **Formato de Decimais:** Utiliza vírgula (`,`) como separador decimal — validado

---

## 2. População e Unidade Amostral

### ✅ População Definida

- **N da fonte original:** 876.248 registros
- **N analítico após remover 5 duplicatas:** 876.243 registros
- **Definição:** Todos os imóveis registrados no cadastro IPTU de Porto Alegre no exercício 2026
- **Unidade Amostral:** Registro individual de imóvel

### ✅ Contexto

Porto Alegre, capital do Rio Grande do Sul, com população de ~1,4 milhão. O IPTU (Imposto sobre Propriedade Predial e Territorial Urbana) incide sobre imóveis urbanos. Os dados incluem:
- Imóveis residenciais, comerciais, industriais, mistos e de utilidade pública
- Valores de mercado, áreas, localizações e tributos
- Dados de 2026 com periodicidade anual

---

## 3. Dimensionamento da Amostra

### ✅ Cálculo Realizado

#### Parâmetros Adotados
- **Nível de confiança:** 95% (z = 1,96)
- **Margem de erro:** 3 pontos percentuais
- **Proporção (p):** 0,50 (conservador)
- **Fator de correção:** População finita (N analítico = 876.243)

#### Fórmula Aplicada
```
n = [z² × p × (1-p) × N] / [E² × (N-1) + z² × p × (1-p)]
N = 876.243
n ≈ 1.065,81 → arredondado para cima: 1.066 registros
```

### ✅ Tamanho Amostral

**n = 1.066 registros** (aproximadamente 0,12% da população analítica)

Essa amostra permite:
- Estimar proporções com margem de erro de 3%
- Estimar médias com precisão adequada (dado N amostral grande)
- Comparar resultados com população completa

---

## 4. Estrutura de Trabalho Preparada

### ✅ Pasta de Projeto

```
TrabalhoFinal/
├── 📄 00_LEIA_PRIMEIRO.md          ← Entrada para humanos
├── 📄 01_GUIA_PASSO_A_PASSO.md     ← Execução
├── 📄 02_REFERENCIA_TECNICA.md     ← Código e resultados
├── 📄 99_CONTEXT_PARA_AGENTES.md   ← Contexto para agentes
├── 📄 Enunciado.txt                ← Tarefa original
├── 📄 fonteDosDados.txt            ← Fonte IPTU
├── 📄 dicionario-de-dados.pdf      ← Dicionário
├── 📄 requirements.txt             ← Dependências
├── 📄 roadmap.md                   ← Estado e pendências
├── 📊 iptu_2026.csv                ← Dataset original
│
├── 📁 scripts/                     ← Scripts Python
│   ├── 01_exploracao_dados.py
│   ├── 02_preparacao_dados.py
│   ├── 03_amostragem.py
│   ├── 04_analise_descritiva.py
│   └── 05_inferencia_estatistica.py
│
├── 📁 dados_processados/           ← 4 CSVs intermediários
└── 📁 saidas/                      ← 9 CSVs de resultados
```

### Scripts e artefatos no estado atual

| # | Script | Status | Função |
|----|--------|--------|--------|
| 1 | `01_exploracao_dados.py` | ✅ Executado | Validação inicial da fonte |
| 2 | `02_preparacao_dados.py` | ✅ Executado | Limpeza e tratamento |
| 3 | `03_amostragem.py` | ✅ Executado | Seleção AAS, semente 42 |
| 4 | `04_analise_descritiva.py` | ✅ Executado | Comparação descritiva |
| 5 | `05_inferencia_estatistica.py` | ✅ Executado | Intervalos e testes |

O status dos artefatos é baseado nos arquivos presentes no repositório, não
substitui uma nova execução após alterações futuras nos scripts.

### ✅ Dependências Python

Preparado arquivo `requirements.txt` com:
- pandas, numpy, scipy
- scikit-learn (para amostragem)
- matplotlib, seaborn, plotly (visualização)
- streamlit (painéis interativos)

---

## 5. Próximas Etapas

### Sequência de execução e entrega

```
Etapa A: Exploração ✅ [CONCLUÍDO]
  └─> 01_exploracao_dados.py

Etapa B: Preparação ✅ [EXECUTADA]
  └─> 02_preparacao_dados.py
      - Validar e converter tipos
      - Tratar valores monetários
      - Confirmar valores faltantes

Etapa C: Amostragem ✅ [EXECUTADA]
  └─> 03_amostragem.py
      - Gerar AAS (n ≈ 1.066)
      - Salvar índices
      - Documentar semente

Etapa D: Descritivas ✅ [EXECUTADA]
  └─> 04_analise_descritiva.py
      - Estatísticas população
      - Gráficos exploratórios
      - Repetir com amostra

Etapa E: Inferência ✅ [EXECUTADA]
  └─> 05_inferencia_estatistica.py
      - Intervalos de confiança (proporção)
      - Intervalos de confiança (média)
      - Testes de hipóteses
      - Comparar com população

Etapa F: Painéis ⬜ [PENDENTE]
  └─> Implementar os 3 painéis interativos exigidos no enunciado
      - Painel 1: População
      - Painel 2: Amostra
      - Painel 3: Inferência + Comparação

Etapa G: Vídeo e links ⬜ [PENDENTE]
  └─> Gravação e edição
      - YouTube (max 5 min)
      - Links públicos
```

### Cronograma Estimado

| Data | Tarefa | Tempo | Status |
|------|--------|-------|--------|
| 07/11 (hoje) | Análise inicial + ambiente | 2h | ✅ |
| 07-08/11 | Etapas B (Prep. dados) | 1h | ⬜ |
| 08/11 | Etapa C (Amostragem) | 0.5h | ⬜ |
| 08-09/11 | Etapa D (Descritivas) | 1.5h | ⬜ |
| 09/11 | Etapa E (Inferência) | 1h | ⬜ |
| 09-10/11 | Etapa F (Painéis) | 2h | ⬜ |
| 10-14/11 | Etapa G (Vídeo) | 1.5h | ⬜ |
| **15/11** | **ENTREGA** | — | ⬜ |

**Total:** ~9 horas de trabalho (factível em 8 dias)

---

## 6. Hipóteses codificadas no script 05

Os valores abaixo correspondem à implementação atual e ainda precisam de
justificativa substantiva na apresentação final; não representam aprovação
externa das hipóteses.

### Hipótese 1: Proporção — Finalidade "Apartamento"

- **Variável:** `des_finalidade`
- **Evento:** Apartamento
- **H₀:** p = 0,40
- **H₁:** p ≠ 0,40 (bilateral)
- **α:** 0,05

### Hipótese 2: Proporção — Uso Residencial

- **Variável:** `des_uso` (válidos: 852.091 após remover duplicatas)
- **Evento:** Residencial
- **H₀:** p = 0,85
- **H₁:** p ≠ 0,85 (bilateral)
- **α:** 0,05

### Hipótese 3: Média — Valor Venal do Imóvel

- **Variável:** `vlr_venal_imovel` (válidos: 876.200 após remover duplicatas)
- **H₀:** μ = R$ 400.000
- **H₁:** μ ≠ R$ 400.000 (bilateral)
- **α:** 0,05
- **Nota:** Distribuição assimétrica; validar pressupostos

### Hipótese 4: Média — Área Construída

- **Variável:** `mtr_area_construida_total` (válidos: 852.186 após remover duplicatas)
- **H₀:** μ = 100 m²
- **H₁:** μ ≠ 100 m² (bilateral)
- **α:** 0,05
- **Nota:** Outliers presentes; analisar distribuição

---

## 7. Checklist de Validação ✅

### Dados
- [x] Dataset carregado (876.248 registros originais)
- [x] População analítica definida (876.243 após remoção de 5 duplicatas)
- [x] Separador e encoding validados
- [x] Ausências documentadas
- [x] Duplicatas identificadas (5 linhas)
- [x] Tipos de dados confirmados

### Amostragem
- [x] Tamanho calculado (n = 1.066)
- [x] Semente de aleatoriedade fixada (42)
- [x] Índices salvos
- [x] Método AAS documentado

### Análise
- [x] Descritivas população e amostra
- [x] Intervalos de confiança e testes de hipóteses implementados
- [x] Comparação população vs. amostra

### Painéis
- [ ] Painel 1 (População)
- [ ] Painel 2 (Amostra)
- [ ] Painel 3 (Inferência)
- [ ] Links acessíveis

### Vídeo
- [ ] Roteiro escrito
- [ ] Gravado
- [ ] Link publicado e acessível

---

## 8. Recursos e Documentação

### Arquivos atuais
- [00_LEIA_PRIMEIRO.md](./00_LEIA_PRIMEIRO.md) — status e visão geral
- [01_GUIA_PASSO_A_PASSO.md](./01_GUIA_PASSO_A_PASSO.md) — execução
- [02_REFERENCIA_TECNICA.md](./02_REFERENCIA_TECNICA.md) — detalhes do pipeline
- [99_CONTEXT_PARA_AGENTES.md](./99_CONTEXT_PARA_AGENTES.md) — contexto para IA
- [Enunciado.txt](./Enunciado.txt) — tarefa completa
- [dicionario-de-dados.pdf](./dicionario-de-dados.pdf) — descrição das variáveis

### Referências Externas
- [IPTU — Dados Abertos Porto Alegre](https://dadosabertos.poa.br/dataset/iptu)
- [Scipy.stats — Testes estatísticos](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Streamlit — Framework de dashboards](https://docs.streamlit.io)
- [Plotly — Gráficos interativos](https://plotly.com/python)

---

## 9. Instruções para Próxima Sessão

### Antes da entrega

1. Reexecutar os scripts 02–05 na ordem indicada em
   [01_GUIA_PASSO_A_PASSO.md](./01_GUIA_PASSO_A_PASSO.md), para regenerar os
   CSVs com o código atual.
2. Construir e testar os três painéis interativos exigidos.
3. Gravar o vídeo de até cinco minutos e disponibilizar os links de entrega.

### Pontos de Atenção

- ⚠️ **Decimais:** o CSV usa ponto-e-vírgula entre colunas e vírgula decimal
- ⚠️ **Distribuição:** Valor venal é altamente assimétrico — examinar distribuição
- ⚠️ **Ausências:** `des_uso` (2.76%) e `mtr_area_construida_total` (2.75%) afetam tamanho válido
- ⚠️ **Independência:** Múltiplas unidades podem estar no mesmo lote — documentar

---

## 10. Conclusão

Os scripts de preparação, amostragem, análise descritiva e inferência estão
implementados, e os CSVs foram regenerados após os ajustes nos scripts 02–03.
Painéis, vídeo e links continuam pendentes.

---

**Preparado por:** Copilot SDK + Análise Manual  
**Data:** 7 de novembro de 2026  
**Tempo total de preparação:** ~2 horas

🎯 **Status:** Scripts implementados; reexecução dos scripts 02–05 necessária
