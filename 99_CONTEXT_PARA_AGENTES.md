# 99 — CONTEXTO PARA AGENTES DE IA

**Informações estruturadas para agentes IA/LLM processarem**

---

## 🤖 INFORMAÇÕES DE PROJETO

```json
{
  "projeto": {
    "nome": "Análise Estatística IPTU Porto Alegre 2026",
    "disciplina": "IA003 - Estatística",
    "universidade": "PUCRS",
    "semestre": "2024/1",
    "tipo": "Trabalho Final",
    "objetivo": "Análise completa com amostragem e inferência estatística"
  }
}
```

---

## 📊 DADOS — ESPECIFICAÇÃO COMPLETA

### Arquivo Source

```
Nome:           iptu_2026.csv
Caminho:        D:\Pós_IA\Disciplinas\IA003-estatistica\TrabalhoFinal\iptu_2026.csv
Tamanho:        210 MB
Linhas:         876.248 registros
Codificação:    UTF-8
Separador:      ; (ponto-e-vírgula)
Decimal:        , (vírgula)
```

### Variáveis

```
Contínuas:
  - vlr_venal_imovel: valor fiscal do imóvel (R$)
  - mtr_area_construida_total: área construída (m²)
  - vlr_imposto: valor IPTU anual (R$)
  - vlr_aliquota: taxa do imposto (%)

Categóricas:
  - des_finalidade: uso principal (Residencial, Comercial, etc)
  - des_uso: classificação detalhada (Apartamento, Casa, Loja, etc)
  - nme_endloc_bairro_cdl: bairro (98 categorias)
  - num_divisao_fiscal: zona fiscal (5 categorias)

Identificadores:
  - num_sequencial_imovel: ID único do imóvel
  - num_terreno: número do terreno
  - num_quadra: número da quadra
```

### Qualidade de Dados

```
Duplicatas:             5 (removidas em 02)
Linhas vazias:          5 (removidas em 02)
Valores ausentes:
  - des_uso: 24.152 (2,75%)
  - mtr_area_construida_total: 24.057 (2,74%)
Outliers:               Detectados mas mantidos (IQR method)
Assimetria:             Presente (distribuição lognormal típica)
```

---

## 🔄 PIPELINE DE SCRIPTS

### Sequência Obrigatória

```
SCRIPT 01: Exploração (✓ já executado)
    ↓
SCRIPT 02: Preparação de Dados
    ├─ Input:  iptu_2026.csv (876.248)
    ├─ Ações:  Limpeza, tipagem, padronização
    └─ Output: dados_processados/dados_limpos.csv (876.238)
    ↓
SCRIPT 03: Amostragem AAS
    ├─ Input:  dados_processados/dados_limpos.csv
    ├─ Ações:  Cálculo de n, sorteio com seed=42
    └─ Output: dados_processados/amostra.csv (1.066)
    ↓
SCRIPT 04: Análise Descritiva
    ├─ Inputs: dados_limpos.csv + amostra.csv
    ├─ Ações:  Estatísticas + frequências
    └─ Outputs: 8 arquivos CSV em saidas/
    ↓
SCRIPT 05: Inferência Estatística
    ├─ Inputs: dados_limpos.csv + amostra.csv
    ├─ Ações:  4 testes de hipóteses
    └─ Output: saidas/testes_hipoteses.csv
```

### Dependências Entre Scripts

```
02 precisa de:      iptu_2026.csv ✓
03 precisa de:      02 (dados_limpos.csv)
04 precisa de:      02 + 03 (dados_limpos.csv + amostra.csv)
05 precisa de:      02 + 03 (dados_limpos.csv + amostra.csv)
```

---

## 📐 ESTATÍSTICAS CALCULADAS

### Script 02 — Preparação

| Ação | Detalhes |
|------|----------|
| Limpeza | Remoção de duplicatas (5) e linhas vazias (5) |
| Tipagem | Conversão para float64, int64 |
| Consolidação | Padronização de categorias |
| Detecção | Outliers com IQR |
| Rastreabilidade | Coluna `processado_em_02` |

### Script 03 — Amostragem

```
Fórmula: n = [z² × p(1-p) × N] / [E² × (N-1) + z² × p(1-p)]

Parâmetros:
  z = 1,96 (95% confiança)
  p = 0,50 (conservador)
  E = 0,03 (3% margem)
  N = 876.238

Resultado: n ≈ 1.066 registros
Taxa de amostragem: 0,12%
Semente: 42 (reprodutibilidade)
```

### Script 04 — Análise Descritiva

Para cada variável contínua:
- count, mean, std, min, 25%, 50%, 75%, max
- Variância, coeficiente variação
- Skewness, kurtosis

Para cada variável categórica:
- Frequência absoluta
- Percentual
- Ordenação descendente

### Script 05 — Inferência Estatística

Teste H1 — Proporção de Apartamentos
```
H₀: p = 0,50
H₁: p ≠ 0,50
Método: Z-test
α: 0,05
```

Teste H2 — Proporção Residencial
```
H₀: p = 0,70
H₁: p ≠ 0,70
Método: Z-test
α: 0,05
```

Teste H3 — Média Valor Venal
```
H₀: μ = 400.000
H₁: μ ≠ 400.000
Método: t-test (gl = 1.065)
α: 0,05
```

Teste H4 — Média Área Construída
```
H₀: μ = 150
H₁: μ ≠ 150
Método: t-test (gl = 1.065)
α: 0,05
```

---

## 📁 ESTRUTURA DE PASTAS

```
TrabalhoFinal/
├── iptu_2026.csv (210 MB - DADOS ORIGINAIS)
├── requirements.txt (dependências Python)
│
├── scripts/
│   ├── 01_exploracao_dados.py (✓ pronto)
│   ├── 02_preparacao_dados.py (▶ executar)
│   ├── 03_amostragem.py (▶ executar)
│   ├── 04_analise_descritiva.py (▶ executar)
│   └── 05_inferencia_estatistica.py (▶ executar)
│
├── dados_processados/ (SAÍDAS DOS SCRIPTS)
│   ├── dados_limpos.csv (script 02)
│   ├── amostra.csv (script 03)
│   ├── amostra_indices.csv (script 03)
│   └── dados_com_indicador_amostra.csv (script 03)
│
├── saidas/ (RESULTADOS FINAIS)
│   ├── desc_populacao.csv (script 04)
│   ├── desc_amostra.csv (script 04)
│   ├── freq_finalidade_pop.csv (script 04)
│   ├── freq_finalidade_amostra.csv (script 04)
│   ├── freq_uso_pop.csv (script 04)
│   ├── freq_uso_amostra.csv (script 04)
│   ├── freq_bairro_pop.csv (script 04)
│   ├── freq_bairro_amostra.csv (script 04)
│   └── testes_hipoteses.csv (script 05)
│
└── docs/
    ├── 00_LEIA_PRIMEIRO.md (entrada humana)
    ├── 01_GUIA_PASSO_A_PASSO.md (execução humana)
    ├── 02_REFERENCIA_TECNICA.md (detalhes técnicos)
    └── 99_CONTEXT_PARA_AGENTES.md (este arquivo)
```

---

## 🛠️ DEPENDÊNCIAS

```python
# Em requirements.txt
pandas>=1.0.0          # manipulação de dados
numpy>=1.20.0          # computação numérica
scipy>=1.7.0           # testes estatísticos
scikit-learn>=0.24.0   # (opcional, não usado atualmente)
```

### Versão Python
- Mínimo: Python 3.9
- Recomendado: Python 3.10+

### Instalação
```bash
pip install -r requirements.txt
```

---

## ⚙️ CONFIGURAÇÕES CRÍTICAS

### Random Seed
```python
RANDOM_SEED = 42
# Garante reprodutibilidade
# Mesmos resultados em múltiplas execuções
```

### Nível de Significância
```python
ALPHA = 0.05
# 5% de chance de erro tipo I
# 95% de confiança
```

### Parâmetros Amostragem
```python
CONFIANCA = 0.95        # z = 1.96
MARGEM_ERRO = 0.03      # 3%
PROPORCAO = 0.50        # conservadora
POPULACAO = 876238      # N
AMOSTRA_TAMANHO = 1066  # n (calculado)
```

---

## 📊 SAÍDAS ESPERADAS

### Formato Padrão
- **Encoding:** UTF-8
- **Separador:** `;` (ponto-e-vírgula)
- **Decimal:** `,` (vírgula)
- **Índice:** incluído (default pandas)

### Exemplo — desc_populacao.csv

```csv
;vlr_venal_imovel;mtr_area_construida_total;vlr_imposto;vlr_aliquota
count;876238.0;852181.0;876238.0;876238.0
mean;387234.56;145.32;1243.21;0.32
std;892156.43;95.21;2156.43;0.08
min;50000.0;20.0;50.0;0.1
25%;125000.0;80.0;400.0;0.25
50%;158642.0;120.0;625.0;0.3
75%;425000.0;180.0;1200.0;0.35
max;45000000.0;5000.0;125000.0;1.5
```

### Exemplo — testes_hipoteses.csv

```csv
teste;h0;h1;parametro;estatistica;critico;p_valor;rejeita;ic_inf;ic_sup;conclusao
H1;p=0.5;p≠0.5;0.545;2.95;1.96;0.0032;Sim;0.515;0.575;Rejeita H0
H2;p=0.7;p≠0.7;0.682;1.87;1.96;0.0616;Não;0.653;0.711;Não rejeita H0
H3;μ=400000;μ≠400000;387234;1.45;1.96;0.1472;Não;358000;416468;Não rejeita H0
H4;μ=150;μ≠150;145.32;3.21;1.96;0.0013;Sim;142.5;148.1;Rejeita H0
```

---

## 🚀 EXECUÇÃO

### Comando Sequencial Recomendado

```bash
cd D:\Pós_IA\Disciplinas\IA003-estatistica\TrabalhoFinal

# Instalação (primeira vez)
pip install -r requirements.txt

# Execução em sequência
python scripts/02_preparacao_dados.py
python scripts/03_amostragem.py
python scripts/04_analise_descritiva.py
python scripts/05_inferencia_estatistica.py
```

### Tempo Total Esperado
- Script 02: 2-3 minutos
- Script 03: 1-2 minutos
- Script 04: 3-5 minutos
- Script 05: 1-2 minutos
- **Total: 10-15 minutos**

---

## 🔐 CARACTERÍSTICAS DE QUALIDADE

### Validação em Cada Script

| Script | Verificações |
|--------|-------------|
| 02 | Carregamento OK? Duplicatas removidas? Tipos convertidos? |
| 03 | Amostra sorteada? Tamanho correto (1.066)? Sem duplicatas? |
| 04 | Variáveis carregadas? Estatísticas calculadas? Frequências OK? |
| 05 | Testes executados? p-valores calculados? ICs estimados? |

### Rastreabilidade

- Cada script adiciona coluna `processado_em_XX` (rastreabilidade)
- Mensagens verbose permitem acompanhar progresso
- Relatórios de qualidade em console

### Reprodutibilidade

- RANDOM_SEED = 42
- Mesmos resultados sempre
- Ideal para documentação e revisão

---

## 📝 NOTAS IMPORTANTES PARA AGENTES IA

### Ao Processar Este Projeto

1. **Respeitar sequência:** 02 → 03 → 04 → 05
2. **Não modificar seed:** Manter `random_state=42`
3. **Preservar NaNs:** Dados faltantes são informativos
4. **Manter outliers:** Removê-los distorce análise
5. **Verificar tamanhos:** amostra deve ter exatamente 1.066 linhas
6. **Validar tipos:** Numeric cols devem ser float64/int64

### Ao Entender os Resultados

- **p-valor < 0,05:** resultado é estatisticamente significante
- **p-valor ≥ 0,05:** resultado não é significante
- **IC não contém H₀:** rejeita hipótese nula
- **IC contém H₀:** não rejeita hipótese nula

### Ao Sugerir Melhorias

- Manter comentários em Português
- Não remover linhas de validação
- Documentar qualquer mudança
- Testar com dados pequenos primeiro

---

## 🎯 QUESTÕES FREQUENTES PARA IA

**P: Posso carregar dados usando pandas.read_csv()?**  
R: Sim. Parâmetros essenciais:
```python
pd.read_csv('iptu_2026.csv', sep=';', encoding='utf-8', decimal=',')
```

**P: Qual é a variável-alvo principal?**  
R: Não há única variável-alvo. Análise multivariada de:
- vlr_venal_imovel (valor fiscal)
- mtr_area_construida_total (área)
- des_finalidade / des_uso (categorização)

**P: Posso usar outras bibliotecas estatísticas?**  
R: Sim (statsmodels, pingouin). Mas verify com o autor primeiro.

**P: E se os dados estiverem em local diferente?**  
R: Ajustar caminho no início de cada script.

**P: Posso paralelizar execução?**  
R: Não recomendado. Manter sequência 02→03→04→05.

---

## 📖 REFERÊNCIAS ESTATÍSTICAS

### Conceitos Chave

**Amostragem Aleatória Simples (AAS)**
- Sem reposição
- Igual probabilidade para todos
- Base para inferência válida

**Teste de Hipóteses (bilateral, α=0,05)**
- Rejeita H₀ se p < 0,05
- Não rejeita H₀ se p ≥ 0,05

**Intervalo de Confiança 95%**
- Range estimado para parâmetro populacional
- Se repetir amostragem 100 vezes, ~95 ICs conteriam parâmetro verdadeiro

**Z-test vs t-test**
- Z-test: proporções (grande amostra)
- t-test: médias com desvio-padrão desconhecido

---

## 🔗 MAPAS DE FLUXO

### Fluxo de Dados

```
iptu_2026.csv
    ↓ [02]
dados_limpos.csv
    ↓ [03]
amostra.csv
    ↓ [04] ← também usa dados_limpos.csv
    ├→ desc_*.csv
    └→ freq_*.csv
    ↓ [05] ← também usa dados_limpos.csv
    ├→ testes_hipoteses.csv
```

### Fluxo de Decisões (Teste H1)

```
Dados carregados?
  ├─ Não → Erro
  └─ Sim
       ↓
    Calcular proporção apartamentos
       ↓
    Teste Z: (p̂ - p₀) / SE
       ↓
    p-valor < 0,05?
       ├─ Sim → Rejeita H₀
       └─ Não → Não rejeita H₀
```

---

## 🎓 EDUCAÇÃO

Este projeto demonstra:

✅ Limpeza e preparação de dados em larga escala  
✅ Amostragem estatística com cálculo de tamanho  
✅ Análise descritiva (tendência central, dispersão)  
✅ Inferência estatística (testes e intervalos)  
✅ Boas práticas: reprodutibilidade, validação, documentação  

---

**Versão:** 1.0  
**Última atualização:** 2024  
**Público:** Agentes IA/LLM  
**Status:** ✓ Estrutura completa

Para humanos: Leia `00_LEIA_PRIMEIRO.md` ou `01_GUIA_PASSO_A_PASSO.md`
