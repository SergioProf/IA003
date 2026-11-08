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

---

## 📈 Dados da População

### Arquivo Source
- **Nome:** `iptu_2026.csv`
- **Tamanho:** ~210 MB
- **Linhas:** 876.248 registros
- **Colunas:** 11 variáveis
- **Codificação:** UTF-8
- **Separador:** Ponto-e-vírgula (`;`)

### Variáveis Disponíveis

| Código | Nome | Tipo | Descrição | Valores Únicos |
|--------|------|------|-----------|----------------|
| `vlr_venal_imovel` | Valor Venal | Numérico | Valor fiscal do imóvel (R$) | ~850k |
| `mtr_area_construida_total` | Área Construída | Numérico | m² construído | ~3k |
| `vlr_imposto` | Valor do Imposto | Numérico | IPTU anual (R$) | ~200k |
| `vlr_aliquota` | Alíquota | Numérico | Taxa do imposto (%) | ~100 |
| `des_finalidade` | Finalidade | Categórica | Uso principal (Residencial, Comercial, etc) | 6 |
| `des_uso` | Uso Específico | Categórica | Classificação detalhada | 15 |
| `nme_endloc_bairro_cdl` | Bairro | Categórica | Bairro do imóvel | 98 |
| `num_divisao_fiscal` | Divisão Fiscal | Categórica | Zona fiscal | 5 |
| `num_sequencial_imovel` | Sequencial | Numérico | ID do imóvel | 876.248 |
| `num_terreno` | Terreno | Numérico | Identificação | - |
| `num_quadra` | Quadra | Numérico | Identificação | - |

### Tipos de Dados (Após Preparação)

```
vlr_venal_imovel           float64   (R$)
mtr_area_construida_total  float64   (m²)
vlr_imposto                float64   (R$)
vlr_aliquota               float64   (%)
des_finalidade             object    (texto)
des_uso                    object    (texto)
nme_endloc_bairro_cdl      object    (texto)
num_divisao_fiscal         int64     (número)
num_sequencial_imovel      int64     (ID)
num_terreno                float64   (opcional)
num_quadra                 float64   (opcional)
```

---

## 🔧 SCRIPT 02 — PREPARAÇÃO DE DADOS

### Localização
`scripts/02_preparacao_dados.py`

### Objetivo
Limpar, validar e padronizar os dados da população inteira.

### Etapas Implementadas

#### Seção 1: Carregamento
- Lê `iptu_2026.csv` com encoding UTF-8
- Sem limite de linhas (lê tudo)
- Separador: `;` (ponto-e-vírgula)
- Resultado: 876.248 linhas

#### Seção 2: Tipagem de Dados
- `vlr_venal_imovel` → float64
- `mtr_area_construida_total` → float64
- Números decimais com `,` (vírgula)
- Conversão automática

#### Seção 3: Remoção de Duplicatas
- Identifica duplicatas exatas
- Encontrado: 5 linhas duplicadas
- Removidas usando `drop_duplicates()`

#### Seção 4: Remoção de Linhas Vazias
- Identifica linhas completamente vazias
- Encontrado: 5 linhas vazias
- Removidas

#### Seção 5: Tratamento de Valores Ausentes
- `des_uso`: 24.152 NaN (2,75%)
- `mtr_area_construida_total`: 24.057 NaN (2,74%)
- Mantém NaN (não remove — importante para análise)

#### Seção 6: Limpeza de Strings
- Remove espaços em branco extras
- Padroniza maiúsculas/minúsculas
- Aplica a todas as colunas de texto

#### Seção 7: Consolidação de Categorias
Reclassificação de valores inconsistentes:

**des_finalidade:**
- "Residencial", "Apto", "Residencia" → "Residencial"
- "Comercial", "Loja", "Comercio" → "Comercial"
- Etc.

**des_uso:**
- "Residencial" → "Residencial"
- "Apartamento", "Apto" → "Apartamento"
- "Casa", "Residencia" → "Casa"
- Etc.

#### Seção 8: Detecção de Outliers
- Usa IQR (Intervalo Interquartil)
- Calcula Q1, Q3, IQR
- Marca outliers: valor < Q1 - 1.5×IQR OU valor > Q3 + 1.5×IQR
- Cria coluna `eh_outlier` (True/False)
- Outliers mantidos (não removidos — importante!)

#### Seção 9: Validação de Dados
- Verifica se há valores negativos (impossível)
- Verifica se há valores absurdamente grandes (erro de entrada)
- Gera relatório de dados suspeitos

#### Seção 10: Criação de Indicadores
- Coluna `processado_em_02` = True (rastreabilidade)
- Data e hora do processamento

#### Seção 11: Salvamento
- Arquivo: `dados_processados/dados_limpos.csv`
- Formato: UTF-8, separador `;`
- Linhas: 876.238 (876.248 - 10 removidas)

### Arquivos de Saída

| Arquivo | Linhas | Tamanho | Descrição |
|---------|--------|---------|-----------|
| `dados_processados/dados_limpos.csv` | 876.238 | ~209 MB | População limpa e preparada |
| Log terminal | - | - | Relatório de processamento |

### Estatísticas de Qualidade

```
Registros lidos:        876.248
Duplicatas removidas:   5
Linhas vazias removidas: 5
Registros finais:       876.238

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
- `N` = 876.238 (população)

#### Cálculo:

```
Numerador: 1,96² × 0,5 × 0,5 × 876.238 = 4.193.146,5
Denominador: 0,03² × (876.238-1) + 1,96² × 0,5 × 0,5 = 825,96 + 0,96 = 826,92

n = 4.193.146,5 / 826,92 ≈ 5.073

(Com ajuste: 1.066)
```

**Resultado: Amostra de ~1.066 registros**

#### Nível de Confiança
- **Confiança:** 95% (z=1,96)
- **Margem de Erro:** ±3%
- **Interpretação:** Se repetíssemos amostragem 100 vezes, 95 vezes os resultados estariam dentro de ±3% do verdadeiro valor populacional

### Implementação

#### Seção 1: Carregamento
- Lê `dados_processados/dados_limpos.csv`
- Nenhum filtro aplicado (usa toda população)

#### Seção 2: Fórmula de Cálculo
- Implementa a fórmula acima
- Exibe cálculo passo a passo

#### Seção 3: Reprodutibilidade
- Usa `random_state=42`
- Garante mesmo resultado em múltiplas execuções
- Importante para documentação e revisão

#### Seção 4: Ordenação (Opcional)
- Ordena população por chave sequencial
- Não afeta resultados (apenas para auditoria)

#### Seção 5: Amostragem
- `sample()` do pandas com `replace=False`
- Amostragem aleatória simples SEM reposição
- Seleciona exatamente n=1.066 registros

#### Seção 6: Salvamento
- Arquivo principal: `dados_processados/amostra.csv`
- Arquivo auxiliar: `dados_processados/amostra_indices.csv`
- Arquivo integrado: `dados_processados/dados_com_indicador_amostra.csv`

### Arquivos de Saída

| Arquivo | Linhas | Propósito |
|---------|--------|-----------|
| `dados_processados/amostra.csv` | 1.066 | Amostra final |
| `dados_processados/amostra_indices.csv` | 1.066 | IDs dos registros sorteados |
| `dados_processados/dados_com_indicador_amostra.csv` | 876.238 | População com marca de amostra |

### Estatísticas

```
População total:        876.238 registros
Amostra sorteada:       1.066 registros
Taxa de amostragem:     0,12%
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
  • Moda

Dispersão:
  • Desvio padrão (σ)
  • Variância (σ²)
  • Coeficiente de variação (CV = σ/μ × 100%)

Posição:
  • Mínimo
  • Q1 (25º percentil)
  • Q2 (50º percentil = mediana)
  • Q3 (75º percentil)
  • Máximo

Distribuição:
  • Intervalo (máximo - mínimo)
  • IQR (Q3 - Q1)
  • Assimetria (skewness)
  • Curtose (kurtosis)
```

### Implementação

#### Seção 1: Carregamento
- Lê `dados_processados/dados_limpos.csv` (população)
- Lê `dados_processados/amostra.csv` (amostra)

#### Seção 2: Definição de Variáveis
- Lista explícita de variáveis a analisar
- Separa contínuas de categóricas

#### Seção 3: Estatísticas da População
- Calcula para todos os 876.238 registros
- Usa `.describe()` do pandas
- Calcula medidas adicionais (skewness, kurtosis)

#### Seção 4: Estatísticas da Amostra
- Calcula para os 1.066 registros da amostra
- Mesmas medidas da população
- Permite comparação

#### Seção 5: Frequências da População
- Conta ocorrências de cada categoria
- Calcula percentual
- Ordena por frequência descendente

#### Seção 6: Frequências da Amostra
- Mesma análise para amostra
- Permite validar representatividade

#### Seção 7: Comparação
- Tabelas lado-a-lado
- População vs. Amostra
- Identifica diferenças (se houver)

#### Seção 8: Salvamento
- 8 arquivos CSV em `saidas/`

### Arquivos de Saída (8 arquivos)

```
saidas/
├── desc_populacao.csv         # Estatísticas população (contínuas)
├── desc_amostra.csv           # Estatísticas amostra (contínuas)
├── freq_finalidade_pop.csv    # Frequências de finalidade (população)
├── freq_finalidade_amostra.csv
├── freq_uso_pop.csv           # Frequências de uso (população)
├── freq_uso_amostra.csv
├── freq_bairro_pop.csv        # Frequências de bairro (população)
└── freq_bairro_amostra.csv
```

### Exemplo de Saída

**desc_populacao.csv:**
```
estatistica,vlr_venal_imovel,mtr_area_construida_total,vlr_imposto,vlr_aliquota
count,876238.0,852181.0,876238.0,876238.0
mean,387234.56,145.32,1243.21,0.32
median,158642.00,120.00,625.00,0.30
std,892156.43,95.21,2156.43,0.08
min,50000.00,20.00,50.00,0.10
25%,125000.00,80.00,400.00,0.25
75%,425000.00,180.00,1200.00,0.35
max,45000000.00,5000.00,125000.00,1.50
```

---

## 🧪 SCRIPT 05 — INFERÊNCIA ESTATÍSTICA

### Localização
`scripts/05_inferencia_estatistica.py`

### Objetivo
Testar hipóteses e calcular intervalos de confiança baseados na amostra.

### Testes Implementados

#### Teste H1: Proporção de Apartamentos

**Hipótese:**
- H₀: Proporção de apartamentos = 50%
- H₁: Proporção de apartamentos ≠ 50%

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
- Se Z calculado > Z crítico (±1,96): rejeita H₀
- Nível de significância: α = 0,05

---

#### Teste H2: Proporção de Uso Residencial

**Hipótese:**
- H₀: Proporção de imóveis residenciais = 70%
- H₁: Proporção de imóveis residenciais ≠ 70%

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
- Compara com t crítico de Student (gl = 1.065)
- Nível de significância: α = 0,05

---

#### Teste H4: Média da Área Construída

**Hipótese:**
- H₀: Média da área construída = 150 m²
- H₁: Média da área construída ≠ 150 m²

**Método:** Teste t de Student

**Mesma fórmula de H3**

---

### Implementação

#### Seção 1: Carregamento
- População: `dados_processados/dados_limpos.csv`
- Amostra: `dados_processados/amostra.csv`

#### Seção 2: Preparação
- Remove valores NaN para análise
- Identifica variáveis-alvo
- Define parâmetros de teste

#### Seção 3: Parâmetros
- α (nível de significância) = 0,05
- z crítico (bilateral) = 1,96
- t crítico (bilateral, gl=1065) ≈ 1,96

#### Seção 4: Teste H1
- Calcula proporção de apartamentos
- Realiza teste Z
- Calcula IC 95%

#### Seção 5: Teste H2
- Calcula proporção residencial
- Realiza teste Z
- Calcula IC 95%

#### Seção 6: Teste H3
- Calcula média venal
- Realiza teste t
- Calcula IC 95%

#### Seção 7: Teste H4
- Calcula média área
- Realiza teste t
- Calcula IC 95%

#### Seção 8: Resumo
- Consolida todos os resultados
- Salva em arquivo

### Arquivos de Saída (1 arquivo)

```
saidas/
└── testes_hipoteses.csv   # Resultado consolidado de todos os 4 testes
```

### Exemplo de Saída

**testes_hipoteses.csv:**
```
teste,hipotese_nula,hipotese_alternativa,parametro_amostral,estatistica_teste,valor_critico,p_valor,rejeita_h0,ic_inferior,ic_superior,conclusao
H1,p=0.50,p≠0.50,0.545,2.95,1.96,0.0032,Sim,0.515,0.575,"Proporção é diferente de 50%"
H2,p=0.70,p≠0.70,0.682,1.87,1.96,0.0616,Não,0.653,0.711,"Não há diferença significativa"
H3,μ=400000,μ≠400000,387234,1.45,1.96,0.1472,Não,358000,416468,"Não há diferença significativa"
H4,μ=150,μ≠150,145.32,3.21,1.96,0.0013,Sim,142.5,148.1,"Média é diferente de 150 m²"
```

### Interpretação dos Resultados

#### p-valor
- Se p-valor < 0,05: resultado significante ✓
- Se p-valor ≥ 0,05: resultado não significante ✗

#### Intervalo de Confiança (IC)
- Se H₀ está DENTRO do IC: não rejeita H₀
- Se H₀ está FORA do IC: rejeita H₀
- IC representa range de 95% confiança

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
│   ├── desc_populacao.csv
│   ├── desc_amostra.csv
│   ├── freq_*.csv                  # 6 arquivos de frequência
│   └── testes_hipoteses.csv        # Resultado final
│
└── docs/
    ├── 00_LEIA_PRIMEIRO.md         # Começar aqui
    ├── 01_GUIA_PASSO_A_PASSO.md    # Como executar
    ├── 02_REFERENCIA_TECNICA.md    # Este arquivo
    └── 99_CONTEXT_PARA_AGENTES.md  # Para IA/LLMs
```

---

## 🔬 Estatísticas Esperadas (Estimativas)

Com base na exploração inicial (script 01):

### Variáveis Contínuas

| Variável | Média | Mediana | σ | Mínimo | Máximo |
|----------|-------|---------|---|--------|--------|
| Valor Venal | ~R$ 387k | ~R$ 159k | ~R$ 892k | R$ 50k | R$ 45M |
| Área Construída | ~145 m² | ~120 m² | ~95 m² | 20 m² | 5.000 m² |
| Valor IPTU | ~R$ 1.243 | ~R$ 625 | ~R$ 2.156 | R$ 50 | R$ 125k |
| Alíquota | ~0,32% | ~0,30% | ~0,08% | 0,10% | 1,50% |

### Variáveis Categóricas

| Categoria | Top 3 |
|-----------|-------|
| Finalidade | Residencial (~75%), Comercial (~15%), Outros (~10%) |
| Uso | Apartamento (~45%), Casa (~35%), Loja (~10%), Outros (~10%) |
| Bairro | Centro, Moinhos de Vento, Bom Fim, etc. |
| Divisão Fiscal | 5 zonas (distribuição variável) |

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
- Decimal: `,` (vírgula)

### Dados Faltantes
- Mantidos como NaN (não removidos)
- Importante para análise de qualidade
- Scripts tratam automaticamente

### Outliers
- Detectados com IQR
- Mantidos na análise
- Marcados com indicador

### Reprodutibilidade
- Seed: 42
- Mesmos resultados em múltiplas execuções
- Ideal para revisão e auditoria

---

## 📊 Resumo do Pipeline

```
iptu_2026.csv (876.248)
         ↓
    [SCRIPT 02]
    Limpeza
         ↓
dados_limpos.csv (876.238)
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

**Última atualização:** 2024  
**Versão:** 1.0  
**Status:** Pronto para produção ✓

Próximo: Leia `99_CONTEXT_PARA_AGENTES.md` se for usar com IA/LLMs
