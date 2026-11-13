# 02 — REFERÊNCIA TÉCNICA

**Detalhes completos de implementação e dados**

---

## 📊 Visão Geral do Projeto

### Objetivo
Análise estatística completa de dados de IPTU (Imposto Predial Territorial Urbano) de Porto Alegre para o ano de 2026.

### Metodologia
1. Exploração inicial (script 01 — já executado)
2. **Preparação de dados** (script 02)
3. **Amostragem aleatória simples** (script 03)
4. **Análise descritiva** (script 04)
5. **Inferência estatística** (script 05)
6. **Painéis interativos** (`app.py`, Streamlit + Plotly)

### Execução dos painéis

Na raiz do projeto, após executar os scripts 02 e 03:

```bash
python -m streamlit run app.py
```

O aplicativo lê `dados_processados/dados_com_indicador_amostra.csv` quando
disponível; caso contrário, usa `dados_painel/dados_painel.csv.gz`, gerado por
`python scripts/06_exportar_dados_painel.py` para o deploy. O arquivo reduzido
contém somente as oito variáveis analisadas e a coluna `em_amostra`; deve ser
regenerado após mudanças nos dados ou na amostra. As três opções
da navegação lateral apresentam população, amostra e inferência/comparação.
Os parâmetros populacionais e as estimativas amostrais são calculados a partir
dos registros; o painel não depende dos CSVs de resumo em `saidas/`.

---

## 📈 Dados da População

### Arquivo Source
- **Nome:** `iptu_2026.csv`
- **Tamanho:** ~210 MB
- **Registros de dados:** 876.248
- **Colunas originais:** 32
- **Codificação:** UTF-8
- **Separador:** Ponto-e-vírgula (`;`)
- **População analítica atual:** 876.243 registros, após remoção de 5 duplicatas exatas
- **Colunas após preparação:** 34 (32 originais + 2 auxiliares)

### Variáveis Usadas nas Análises

| Código | Nome | Tipo | Descrição | Valores Únicos |
|--------|------|------|-----------|----------------|
| `vlr_venal_imovel` | Valor Venal | Numérico | Valor fiscal do imóvel (R$) | ~850k |
| `mtr_area_construida_total` | Área Construída | Numérico | m² construído | ~3k |
| `vlr_imposto` | Valor do Imposto | Numérico | IPTU anual (R$) | ~200k |
| `vlr_aliquota` | Alíquota | Numérico | Taxa do imposto (%) | ~100 |
| `des_finalidade` | Finalidade | Categórica | Finalidade registrada para o imóvel | variável |
| `des_uso` | Uso | Categórica | Classificação de uso | variável |
| `nme_endloc_bairro_cdl` | Bairro | Categórica | Bairro do imóvel | variável |
| `num_divisao_fiscal` | Divisão Fiscal | Categórica | Divisão fiscal | 3 |

As demais colunas da fonte estão no cabeçalho de `iptu_2026.csv` e no
dicionário oficial. A preparação adiciona `indice_original` e
`num_campos_vazios`; não cria um identificador chamado `num_sequencial_imovel`.

As quatro primeiras variáveis da tabela são tratadas como quantitativas; as
quatro últimas são usadas como categorias nas análises.

---

## 🔧 SCRIPT 02 — PREPARAÇÃO DE DADOS

### Localização
`scripts/02_preparacao_dados.py`

### Objetivo
Limpar, validar e padronizar os dados da população inteira.

### Etapas Implementadas

#### Seção 1: Carregamento e estado inicial
- Lê `iptu_2026.csv` em UTF-8, separado por `;`.
- A fonte atual contém 876.248 registros e 32 colunas.

#### Seção 2: Remoção de linhas completamente vazias
- Verifica linhas em que todas as colunas estão ausentes.
- Não há linhas totalmente vazias no arquivo atual.

#### Seção 3: Remoção de duplicatas
- Remove 5 linhas duplicadas exatas com `drop_duplicates()`.

#### Seção 4: Tipagem e limpeza dos valores
- Converte as variáveis quantitativas usadas na análise para `float`.
- Troca vírgula decimal por ponto antes da conversão.
- Valores não convertíveis tornam-se `NaN` e são contabilizados.
- Remove espaços externos e padroniza os textos das variáveis categóricas usadas.

#### Seção 5: Tratamento de valores negativos
- Converte valores negativos nas medidas monetárias e de área para `NaN`, sem remover a linha.

#### Seção 6: Consolidação de categorias
- Padroniza rótulos de `des_finalidade` por correspondência de texto. Em
  `des_uso`, preserva as categorias originais, inclusive a distinção entre
  "Exclusivamente Residencial" e "Não Exclusivamente Residencial".
- As correspondências exatas estão nos dicionários `mapa_finalidade` e `mapa_uso` do script.

#### Seção 7: Identificação de outliers
- Usa IQR: valores abaixo de Q1 - 1,5×IQR ou acima de Q3 + 1,5×IQR são quantificados no terminal.
- Mantém os valores extremos; o script não cria uma coluna `eh_outlier`.

#### Seção 8: Variáveis auxiliares
- Cria `indice_original` para rastrear a posição após a limpeza.
- Cria `num_campos_vazios` para contar ausências por registro.

#### Ausências na população processada atual
- `des_uso`: 24.152
- `mtr_area_construida_total`: 24.057
- `vlr_venal_imovel`: 43
- `nme_endloc_bairro_cdl`: 507
- As ausências são mantidas para que cada análise use os casos válidos da variável.

#### Seção 9: Resumo e salvamento
- Salva `dados_processados/dados_limpos.csv` em UTF-8, separado por `;`.
- O arquivo atual contém 876.243 registros e 34 colunas (32 originais + 2 auxiliares).

### Arquivos de Saída

| Arquivo | Linhas | Tamanho | Descrição |
|---------|--------|---------|-----------|
| `dados_processados/dados_limpos.csv` | 876.243 | ~209 MB | População limpa e preparada |
| Log terminal | - | - | Relatório de processamento |

### Estatísticas de Qualidade

```
Registros lidos:        876.248
Duplicatas removidas:   5
Linhas vazias removidas: 0
Registros finais:       876.243

Percentual mantido: 99,99%
```

---

## 🎲 SCRIPT 03 — AMOSTRAGEM

### Localização
`scripts/03_amostragem.py`

### Objetivo
Selecionar uma amostra aleatória simples (AAS) representativa da população.

### Metodologia

#### Cálculo do Tamanho da Amostra

Fórmula (com correção de população finita):

```
n = [z² × p(1-p) × N] / [E² × (N-1) + z² × p(1-p)]
```

Onde:
- `z` = 1,96 (valor crítico para 95% de confiança)
- `p` = 0,50 (proporção conservadora)
- `E` = 0,03 (margem de erro de 3%)
- `N` = 876.243 (registros da população processada atual)

**Importante:** `p = 0,50` é usado somente no dimensionamento da amostra
porque maximiza a variância de uma proporção quando ela é desconhecida. Não é
a hipótese nula do teste de apartamentos; no teste H1, o script usa
`H₀: p = 0,40`.

#### Cálculo:

```
Numerador: 1,96² × 0,5 × 0,5 × 876.243 ≈ 841.543,78
Denominador: 0,03² × (876.243-1) + 1,96² × 0,5 × 0,5 ≈ 789,58

n ≈ 841.543,78 / 789,58 ≈ 1.065,81
Arredondando para cima: 1.066 registros
```

**Resultado: Amostra de ~1.066 registros**

#### Nível de Confiança
- **Confiança:** 95% (z=1,96)
- **Margem de Erro:** ±3%
- A margem de erro de 3 pontos percentuais se refere ao dimensionamento de proporções sob as premissas da fórmula, não é uma garantia para qualquer média ou variável.

### Implementação

#### Seção 1: Carregamento
- Lê `dados_processados/dados_limpos.csv`
- Nenhum filtro aplicado (usa toda população)

#### Seção 2: Fórmula de Cálculo
- Implementa a fórmula acima
- Exibe cálculo passo a passo

#### Seção 3: Reprodutibilidade
- Inicializa o gerador NumPy com `np.random.seed(42)`.
- Garante mesmo resultado em múltiplas execuções
- Importante para documentação e revisão

#### Seção 4: Amostragem
- Usa `numpy.random.choice` com `replace=False`.
- Amostragem aleatória simples SEM reposição
- Seleciona exatamente n=1.066 registros

#### Seção 5: Salvamento
- Arquivo principal: `dados_processados/amostra.csv`
- Arquivo auxiliar: `dados_processados/amostra_indices.csv`
- Arquivo integrado: `dados_processados/dados_com_indicador_amostra.csv`

### Arquivos de Saída

| Arquivo | Linhas | Propósito |
|---------|--------|-----------|
| `dados_processados/amostra.csv` | 1.066 | Amostra final |
| `dados_processados/amostra_indices.csv` | 1.066 | Índices de linha sorteados |
| `dados_processados/dados_com_indicador_amostra.csv` | 876.243 | População com marca de amostra |

### Estatísticas

```
População total:        876.243 registros
Amostra sorteada:       1.066 registros
Taxa de amostragem:     0,1217%
Método:                 AAS (sem reposição)
Semente aleatória:      42
```

---

## 📊 SCRIPT 04 — ANÁLISE DESCRITIVA

### Localização
`scripts/04_analise_descritiva.py`

### Objetivo
Calcular estatísticas descritivas (média, mediana, desvio padrão, etc) para variáveis contínuas e frequências para variáveis categóricas.

### Variáveis Analisadas

#### Contínuas (Estatísticas)
1. `vlr_venal_imovel` — Valor venal (R$)
2. `mtr_area_construida_total` — Área construída (m²)
3. `vlr_imposto` — Valor do imposto (R$)
4. `vlr_aliquota` — Alíquota (%)

#### Categóricas (Frequências)
1. `des_finalidade` — Finalidade do imóvel
2. `des_uso` — Uso específico
3. `nme_endloc_bairro_cdl` — Bairro
4. `num_divisao_fiscal` — Divisão fiscal

### Estatísticas Calculadas (Variáveis Contínuas)

Para cada variável contínua:

```
Tendência Central:
  • Média (μ)
  • Mediana

Dispersão:
  • Desvio padrão (σ)
  • Coeficiente de variação (CV = σ/μ × 100%)

Posição:
  • Mínimo
  • Q1 (25º percentil)
  • Q2 (50º percentil = mediana)
  • Q3 (75º percentil)
  • Máximo

Distribuição:
  • Intervalo (máximo - mínimo)
```

O script também apresenta Q1 e Q3 separadamente. Não calcula moda, variância,
assimetria ou curtose.

### Implementação

#### Seção 1: Carregamento
- Lê `dados_processados/dados_com_indicador_amostra.csv`
- Separa a população e a amostra pela coluna `em_amostra`

#### Seção 2: Definição de Variáveis
- Lista explícita de variáveis a analisar
- Separa contínuas de categóricas

#### Seção 3: Estatísticas da População
- Calcula as medidas para os 876.243 registros processados atuais
- Compara os resultados com os casos válidos da amostra

#### Seção 4: Estatísticas da Amostra
- Calcula as mesmas medidas para os 1.066 registros sorteados

#### Frequências e comparação
- Conta frequências e calcula percentuais para as quatro variáveis categóricas.
- Cada arquivo compara população e amostra lado a lado; as ausências aparecem como categoria.

### Arquivos de Saída (8 arquivos)

```
saidas/
├── desc_vlr_venal_imovel.csv
├── desc_mtr_area_construida_total.csv
├── desc_vlr_imposto.csv
├── desc_vlr_aliquota.csv
├── freq_des_finalidade.csv
├── freq_des_uso.csv
├── freq_nme_endloc_bairro_cdl.csv
└── freq_num_divisao_fiscal.csv
```

Cada arquivo `desc_*.csv` contém as linhas `Media`, `Mediana`,
`Desvio-Padrao`, `Minimo`, `Q1`, `Q3`, `Maximo`, `Amplitude` e `CV`, com as
colunas `Estatística`, `População`, `Amostra` e `Diferença (%)`. Cada arquivo
`freq_*.csv` compara categoria, frequência e percentual dos dois grupos.

O script grava esses arquivos como CSV separado por vírgula e sem índice.

---

## 🧪 SCRIPT 05 — INFERÊNCIA ESTATÍSTICA

### Localização
`scripts/05_inferencia_estatistica.py`

### Objetivo
Testar hipóteses e calcular intervalos de confiança baseados na amostra.

### Testes Implementados

#### Teste H1: Proporção de Apartamentos

**Hipótese:**
- H₀: Proporção de apartamentos = 40%
- H₁: Proporção de apartamentos ≠ 40%

**Método:** Teste Z para proporções

**Fórmula:**
```
Z = (p̂ - p₀) / √[p₀(1-p₀)/n]

Onde:
  p̂ = proporção na amostra
  p₀ = proporção sob H₀
  n = tamanho da amostra
```

**Interpretação:**
- Para o teste bilateral, rejeita-se H₀ se |Z| > 1,96 (equivalentemente, se o valor-p < 0,05).
- Nível de significância: α = 0,05

---

#### Teste H2: Proporção de Uso Exclusivamente Residencial

**Hipótese:**
- H₀: Proporção de imóveis de uso exclusivamente residencial = 85%
- H₁: Proporção de imóveis de uso exclusivamente residencial ≠ 85%

O denominador considera apenas os registros com `des_uso` preenchido. A
categoria "Não Exclusivamente Residencial" não é contada no evento e não deve
ser interpretada automaticamente como comercial.

**Método:** Teste Z para proporções

**Mesma fórmula de H1**

---

#### Teste H3: Média do Valor Venal

**Hipótese:**
- H₀: Média do valor venal = R$ 400.000
- H₁: Média do valor venal ≠ R$ 400.000

**Método:** Teste t de Student

**Fórmula:**
```
t = (x̄ - μ₀) / (s / √n)

Onde:
  x̄ = média amostral
  μ₀ = média sob H₀
  s = desvio padrão amostral
  n = tamanho da amostra
  gl = n - 1 (graus de liberdade)
```

**Interpretação:**
- Compara com o valor crítico da distribuição t de Student, usando `n - 1` graus de liberdade da amostra válida.
- Nível de significância: α = 0,05

---

#### Teste H4: Média da Área Construída

**Hipótese:**
- H₀: Média da área construída = 100 m²
- H₁: Média da área construída ≠ 100 m²

**Método:** Teste t de Student

**Mesma fórmula de H3**

---

### Implementação

#### Seção 1: Carregamento
- Lê `dados_processados/dados_com_indicador_amostra.csv`
- Usa a coluna `em_amostra` para separar população e amostra

#### Seção 2: Preparação
- Remove ausências variável a variável para calcular estatísticas
- Identifica variáveis-alvo
- Define parâmetros de teste

#### Seção 3: Parâmetros
- α (nível de significância) = 0,05
- z crítico (bilateral) = 1,96
- O valor crítico t é calculado pela distribuição t, com `n - 1` graus de liberdade para cada variável

#### Seções 3–6: Testes H1–H4
- Calcula proporção de apartamentos
- Realiza teste Z
- Calcula proporção de uso exclusivamente residencial
- Realiza teste Z
- Calcula média venal
- Realiza teste t
- Calcula média área
- Realiza teste t
- Calcula intervalo de confiança de 95% para cada parâmetro

#### Seção 8: Resumo
- Consolida todos os resultados
- Salva em arquivo

### Arquivos de Saída (1 arquivo)

```
saidas/
└── testes_hipoteses.csv   # Resultado consolidado de todos os 4 testes
```

### Formato da Saída

**`saidas/testes_hipoteses.csv`** contém:
```
Hipótese,Estatística,Valor-p,Decisão
"H1: p_Apartamento = 0,40",0.7252,0.468313,Não rejeitar H₀
"H2: p_Exclusivamente_Residencial = 0,85",-0.2262,0.821027,Não rejeitar H₀
"H3: μ_Valor = 400k",-3.2121,0.001357,Rejeitar H₀
"H4: μ_Área = 100",0.9040,0.366187,Não rejeitar H₀
```

A tabela contém somente estatística, valor-p e decisão; os
intervalos de confiança e conclusões detalhadas são exibidos no terminal.

### Resultados da execução mais recente

| Hipótese | n válido na amostra | Estatística | Valor-p | Decisão (α = 0,05) |
|----------|---------------------:|------------:|--------:|--------------------|
| H1: apartamentos, p₀ = 0,40 | 1.066 | z = 0,7252 | 0,468313 | Não rejeitar H₀ |
| H2: uso exclusivamente residencial, p₀ = 0,85 | 1.036 | z = -0,2262 | 0,821027 | Não rejeitar H₀ |
| H3: valor venal, μ₀ = R$ 400.000 | 1.066 | t = -3,2121 | 0,001357 | Rejeitar H₀ |
| H4: área construída, μ₀ = 100 m² | 1.036 | t = 0,9040 | 0,366187 | Não rejeitar H₀ |

Em H2, a proporção populacional é 84,58% (720.727 de 852.091 valores
válidos) e a amostral é 84,75% (878 de 1.036), com IC de 95% de 82,56% a
86,94%. Os denominadores variam por hipótese porque os testes usam casos
válidos para cada variável.

### Interpretação dos Resultados

#### p-valor
- Se p-valor < 0,05: resultado significante ✓
- Se p-valor ≥ 0,05: resultado não significante ✗

#### Intervalo de Confiança (IC)
- Nos testes t, o IC e o teste usam o mesmo erro padrão e distribuição; a inclusão do valor hipotético tende a corresponder à decisão do teste, salvo arredondamento.
- Para proporções, o teste Z usa erro padrão calculado sob H₀, enquanto o IC usa a proporção observada. Por isso, decisões baseadas no IC de Wald podem não coincidir exatamente com as do teste; use o valor-p para a decisão formal.
- O IC de 95% descreve uma faixa estimada para o parâmetro populacional.

#### Conclusão
- **Rejeita H₀:** evidência suficiente contra a hipótese nula
- **Não rejeita H₀:** evidência insuficiente contra a hipótese nula

---

## 📂 Estrutura de Pastas

```
TrabalhoFinal/
├── iptu_2026.csv                    # Dados originais (210 MB)
├── requirements.txt                 # Dependências Python
│
├── scripts/
│   ├── 01_exploracao_dados.py      # Exploração (já executado)
│   ├── 02_preparacao_dados.py      # Limpeza de dados
│   ├── 03_amostragem.py            # Amostragem AAS
│   ├── 04_analise_descritiva.py    # Análise descritiva
│   └── 05_inferencia_estatistica.py # Testes de hipóteses
│
├── dados_processados/
│   ├── dados_limpos.csv            # População limpa
│   ├── amostra.csv                 # Amostra (1.066 registros)
│   ├── amostra_indices.csv         # Índices sorteados
│   └── dados_com_indicador_amostra.csv
│
├── saidas/
│   ├── desc_<variável>.csv         # 4 comparações quantitativas
│   ├── freq_<variável>.csv         # 4 comparações categóricas
│   └── testes_hipoteses.csv        # 4 testes resumidos
│
├── 00_LEIA_PRIMEIRO.md             # Entrada para humanos
├── 01_GUIA_PASSO_A_PASSO.md        # Como executar
├── 02_REFERENCIA_TECNICA.md        # Detalhes técnicos
└── 99_CONTEXT_PARA_AGENTES.md      # Contexto para IA/LLMs
```

Os resultados observados devem ser consultados nos CSVs gerados; valores
preenchidos como previsões ou exemplos não são resultados do pipeline.

---

## 🛠️ Dependências e Versões

```
Python:     3.9+
pandas:     1.x ou 2.x
numpy:      1.20+
scipy:      1.7+
scikit-learn: 0.24+ (opcional, não usado no pipeline atual)
```

### Instalação
```bash
pip install -r requirements.txt
```

---

## ⚙️ Detalhes Técnicos Importantes

### Codificação
- Arquivo: UTF-8
- Separador: `;` (ponto-e-vírgula)
- Decimal na fonte: `,` (vírgula); script 02 normaliza para ponto nas variáveis quantitativas.

Os CSVs dos scripts 02 e 03 usam `;`; os CSVs dos scripts 04 e 05 usam a vírgula
separadora padrão do pandas. Os scripts 02–05 gravam sem índice; os arquivos
produzidos pelo script 01 usam o padrão do pandas, que inclui índice em
`01_descritivas_populacao.csv`.

### Dados Faltantes
- Mantidos como NaN (não removidos)
- Importante para análise de qualidade
- Cada cálculo usa os casos válidos da variável analisada

### Outliers
- Identificados e quantificados no terminal pelo critério IQR
- Mantidos na análise
- Não recebem coluna indicadora específica

### Reprodutibilidade
- Seed: 42
- Mesmos resultados em múltiplas execuções
- Ideal para revisão e auditoria

---

## 📊 Resumo do Pipeline

```
iptu_2026.csv (876.248 registros, 32 colunas)
         ↓
    [SCRIPT 02]
    Remove 5 duplicatas
         ↓
dados_limpos.csv (876.243 registros, 34 colunas)
         ↓
    [SCRIPT 03]
    Amostragem AAS
         ↓
amostra.csv (1.066)
         ↓
    [SCRIPT 04]
    Descritivas
         ├→ desc_*.csv
         └→ freq_*.csv
         ↓
    [SCRIPT 05]
    Testes
         ↓
testes_hipoteses.csv ✓
```

---

## 🎓 Conceitos Estatísticos

### Amostragem Aleatória Simples (AAS)
- Cada elemento tem probabilidade igual de ser selecionado
- Sem reposição (cada registro escolhido uma única vez)
- Base para inferência estatística válida

### Nível de Confiança
- 95% significa que em 100 repetições, 95 teriam resultado similar
- Complemento: 5% de risco de erro (α)

### Intervalo de Confiança
- Range estimado para parâmetro populacional
- Ex: IC = [0,50 ; 0,60] para proporção = "95% confiança valor real entre 50% e 60%"

### Teste de Hipóteses
- H₀ (nula): afirmação a testar (geralmente "sem efeito")
- H₁ (alternativa): o oposto de H₀
- Decisão baseada em p-valor e nível de significância

### p-valor
- Probabilidade de obter resultado tão extremo quanto observado, se H₀ fosse verdadeira
- p < 0,05: resultado é raro (rejeita H₀)
- p ≥ 0,05: resultado é comum (não rejeita H₀)

---

## 📝 Convenções de Código

Todos os scripts seguem:

1. **Português:** comentários e mensagens em português
2. **Modular:** código organizado em seções numeradas
3. **Verboso:** muitos `print()` para acompanhamento
4. **Validação:** verificações em cada etapa
5. **Rastreabilidade:** colunas indicadoras de processamento

---

## 🔐 Boas Práticas

✅ Sempre executar na ordem: 02 → 03 → 04 → 05

✅ Validar arquivos de saída após cada script

✅ Manter cópia backup dos `dados_processados/`

✅ Documentar qualquer modificação aos scripts

✅ Reproduzir análise com seed=42 (padrão)

---

**Última atualização:** 12/11/2026
**Versão:** 1.0  
**Status:** Pronto para produção ✓

Próximo: Leia `99_CONTEXT_PARA_AGENTES.md` se for usar com IA/LLMs
