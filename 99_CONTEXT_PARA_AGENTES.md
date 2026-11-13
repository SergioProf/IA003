# 99 — CONTEXTO PARA AGENTES DE IA

**Informações estruturadas para agentes IA/LLM processarem**

> Estado verificado dos arquivos locais em 12/11/2026. Para leitura humana,
> comece por `00_LEIA_PRIMEIRO.md`; este arquivo não substitui o enunciado.
> Os scripts 02–05 foram executados após os ajustes recentes; os CSVs locais
> correspondem ao código atual.

---

## 🤖 INFORMAÇÕES DE PROJETO

```json
{
  "projeto": {
    "nome": "Análise Estatística IPTU Porto Alegre 2026",
    "disciplina": "IA003 - Estatística",
    "universidade": "PUCRS",
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
Registros:      876.248 (fonte original)
Colunas:        32 (fonte original)
População após limpeza: 876.243 registros (5 duplicatas removidas)
Colunas após preparação: 34 (inclui 2 auxiliares)
Codificação:    UTF-8
Separador:      ; (ponto-e-vírgula)
Decimal:        , (vírgula)
Conversão:      substitui a vírgula decimal por ponto antes de converter para float
Falhas:         valores não numéricos viram NaN e são contabilizados no terminal
```

### Variáveis

```
Quantitativas usadas nas análises:
  - vlr_venal_imovel: valor fiscal do imóvel (R$)
  - mtr_area_construida_total: área construída (m²)
  - vlr_imposto: valor IPTU anual (R$)
  - vlr_aliquota: taxa do imposto (%)

Categóricas usadas nas análises:
  - des_finalidade: finalidade do imóvel
  - des_uso: uso do imóvel
  - nme_endloc_bairro_cdl: bairro
  - num_divisao_fiscal: divisão fiscal (3 categorias observadas)

Colunas auxiliares criadas em 02:
  - indice_original
  - num_campos_vazios
```

### Qualidade de Dados

```
Duplicatas:             5 (removidas em 02)
Linhas completamente vazias: 0
Valores ausentes:
  - des_uso: 24.152 (2,75%)
  - mtr_area_construida_total: 24.057 (2,74%)
  - vlr_venal_imovel: 43
  - nme_endloc_bairro_cdl: 507
Outliers:               Quantificados pelo IQR e mantidos; sem coluna indicadora
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
    └─ Output: dados_processados/dados_limpos.csv (876.243)
    ↓
SCRIPT 03: Amostragem AAS
    ├─ Input:  dados_processados/dados_limpos.csv
    ├─ Ações:  Cálculo de n, sorteio com seed=42
    └─ Outputs: amostra.csv (1.066), amostra_indices.csv (1.066),
                dados_com_indicador_amostra.csv (876.243)
    ↓
SCRIPT 04: Análise Descritiva
    ├─ Input:  dados_com_indicador_amostra.csv
    ├─ Ações:  Estatísticas + frequências
    └─ Outputs: 8 arquivos CSV em saidas/
    ↓
SCRIPT 05: Inferência Estatística
    ├─ Input:  dados_com_indicador_amostra.csv
    ├─ Ações:  4 testes de hipóteses
    └─ Output: saidas/testes_hipoteses.csv
```

### Dependências Entre Scripts

```
02 precisa de:      iptu_2026.csv ✓
03 precisa de:      02 (dados_limpos.csv)
04 precisa de:      saída do 03 (dados_com_indicador_amostra.csv)
05 precisa de:      saída do 03 (dados_com_indicador_amostra.csv)
```

---

## 📐 ESTATÍSTICAS CALCULADAS

### Script 02 — Preparação

| Ação | Detalhes |
|------|----------|
| Limpeza | Remoção de 5 duplicatas exatas; 0 linhas totalmente vazias |
| Tipagem | Converte as variáveis quantitativas da análise para float |
| Consolidação | Padronização de categorias |
| Detecção | Quantifica outliers com IQR e os mantém |
| Rastreabilidade | `indice_original` e `num_campos_vazios` |

### Script 03 — Amostragem

```
Fórmula: n = [z² × p(1-p) × N] / [E² × (N-1) + z² × p(1-p)]

Parâmetros:
  z = 1,96 (95% confiança)
  p = 0,50 (conservador)
  E = 0,03 (3% margem)
  N = 876.243

Resultado: n ≈ 1.066 registros
Taxa de amostragem: 0,1217%
Semente: 42 (reprodutibilidade)
```

### Script 04 — Análise Descritiva

Para cada variável quantitativa:
- Média, mediana, desvio-padrão, mínimo, Q1, Q3, máximo, amplitude e CV
- Comparação entre população e amostra no mesmo CSV

Para cada variável categórica:
- Frequência absoluta
- Percentual
- Ordenação descendente

### Script 05 — Inferência Estatística

Teste H1 — Proporção de Apartamentos
```
H₀: p = 0,40
H₁: p ≠ 0,40
Método: Z-test
α: 0,05
```

Teste H2 — Proporção Residencial
```
H₀: p = 0,85
H₁: p ≠ 0,85
Método: Z-test
α: 0,05
```

Teste H3 — Média Valor Venal
```
H₀: μ = 400.000
H₁: μ ≠ 400.000
Método: t-test (gl = n_amostra_h3 - 1)
α: 0,05
```

Teste H4 — Média Área Construída
```
H₀: μ = 100
H₁: μ ≠ 100
Método: t-test (gl = n_amostra_h4 - 1)
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
│   ├── 01_exploracao_dados.py (executado)
│   ├── 02_preparacao_dados.py
│   ├── 03_amostragem.py
│   ├── 04_analise_descritiva.py
│   └── 05_inferencia_estatistica.py
│
├── dados_processados/ (SAÍDAS DOS SCRIPTS)
│   ├── dados_limpos.csv (script 02)
│   ├── amostra.csv (script 03)
│   ├── amostra_indices.csv (script 03)
│   └── dados_com_indicador_amostra.csv (script 03)
│
├── saidas/ (RESULTADOS FINAIS)
│   ├── desc_vlr_venal_imovel.csv
│   ├── desc_mtr_area_construida_total.csv
│   ├── desc_vlr_imposto.csv
│   ├── desc_vlr_aliquota.csv
│   ├── freq_des_finalidade.csv
│   ├── freq_des_uso.csv
│   ├── freq_nme_endloc_bairro_cdl.csv
│   ├── freq_num_divisao_fiscal.csv
│   └── testes_hipoteses.csv (script 05)
│
├── 00_LEIA_PRIMEIRO.md (entrada humana)
├── 01_GUIA_PASSO_A_PASSO.md (execução humana)
├── 02_REFERENCIA_TECNICA.md (detalhes técnicos)
└── 99_CONTEXT_PARA_AGENTES.md (este arquivo)
```

Os artefatos atuais incluem 4 CSVs intermediários em `dados_processados/` e
9 CSVs de resultado em `saidas/`. O aplicativo `app.py` implementa os três
painéis locais; o vídeo e os links acessíveis exigidos no enunciado continuam
pendentes.

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
MARGEM_ERRO = 0.03      # 3 pontos percentuais no dimensionamento de proporção
PROPORCAO = 0.50        # conservadora
POPULACAO = 876243      # N após remover duplicatas
AMOSTRA_TAMANHO = 1066  # n calculado e arredondado para cima
```

---

## 📊 SAÍDAS ESPERADAS

### Formatos e nomes
- Todos os arquivos são UTF-8.
- Scripts 02 e 03: separador `;`; scripts 04 e 05: separador `,`.
- Scripts 02–05 gravam sem índice.
- Script 04: 4 `desc_<variável>.csv` e 4 `freq_<variável>.csv`, cada um comparando população e amostra.
- Script 05: `testes_hipoteses.csv`, com colunas `Hipótese`, `Estatística`, `Valor-p` e `Decisão`.

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

- Script 02 adiciona `indice_original` e `num_campos_vazios`; script 03 adiciona `em_amostra`.
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

- **p-valor < 0,05:** rejeita H₀ ao nível de significância de 5%
- **p-valor ≥ 0,05:** não rejeita H₀; isso não prova H₀
- Para ICs bilaterais de 95% compatíveis com o teste, verifique se o valor hipotético está no intervalo; para proporções, o script usa teste Z e IC de Wald, que podem divergir.

### Ao Sugerir Melhorias

- Manter comentários em Português
- Não remover linhas de validação
- Documentar qualquer mudança
- Testar com dados pequenos primeiro

---

## 🎯 QUESTÕES FREQUENTES PARA IA

**P: Posso carregar dados usando pandas.read_csv()?**  
R: Sim. A fonte usa vírgula decimal e ponto-e-vírgula entre colunas:
```python
pd.read_csv('iptu_2026.csv', sep=';', encoding='utf-8', decimal=',')
```
O pipeline atual normaliza os decimais explicitamente no script 02.

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
dados_com_indicador_amostra.csv
    ↓ [04]
    ├→ desc_*.csv (comparação de população e amostra)
    └→ freq_*.csv (comparação de população e amostra)
    ↓ [05] ← também usa dados_com_indicador_amostra.csv
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
**Última atualização:** 12/11/2026
**Público:** Agentes IA/LLM  
**Status:** Pipeline analítico e painéis locais prontos; vídeo e links pendentes

Para humanos: Leia `00_LEIA_PRIMEIRO.md` ou `01_GUIA_PASSO_A_PASSO.md`
