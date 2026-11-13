# 📊 Trabalho Final — Estatística IA003

> **Documento de contexto inicial (histórico).** O status, a estrutura de
> arquivos e as próximas ações abaixo foram registrados antes da execução do
> pipeline. Para instruções e resultados atuais, siga esta ordem:
> [00_LEIA_PRIMEIRO.md](./00_LEIA_PRIMEIRO.md) →
> [01_GUIA_PASSO_A_PASSO.md](./01_GUIA_PASSO_A_PASSO.md) →
> [02_REFERENCIA_TECNICA.md](./02_REFERENCIA_TECNICA.md).
> Painéis, vídeo e links de entrega ainda estão pendentes conforme o
> [Enunciado.txt](./Enunciado.txt).
> As instruções de execução neste documento são históricas; para os comandos
> atuais e a regeneração dos CSVs, use
> [01_GUIA_PASSO_A_PASSO.md](./01_GUIA_PASSO_A_PASSO.md).

## Análise de Amostragem, Intervalos de Confiança e Testes de Hipóteses  
### IPTU 2026 — Porto Alegre

---

## 🎯 Objetivo

Aplicar conceitos de **amostragem**, **estimação por intervalos de confiança** e **testes de hipóteses** na análise de uma grande base de dados (876.248 imóveis), comparando resultados populacionais com estimativas amostrais através de painéis interativos e apresentação em vídeo.

---

## 📋 Documentação

### Documentação atual
1. [00_LEIA_PRIMEIRO.md](./00_LEIA_PRIMEIRO.md) — ponto inicial e status atual
2. [01_GUIA_PASSO_A_PASSO.md](./01_GUIA_PASSO_A_PASSO.md) — execução dos scripts
3. [02_REFERENCIA_TECNICA.md](./02_REFERENCIA_TECNICA.md) — implementação e artefatos
4. [99_CONTEXT_PARA_AGENTES.md](./99_CONTEXT_PARA_AGENTES.md) — contexto estruturado para IA

Consulte também [README_ESTRUTURA.md](./README_ESTRUTURA.md) para o mapa de
leitura e [GLOSSARIO_ESTATISTICO.md](./GLOSSARIO_ESTATISTICO.md) para conceitos.

---

## ⚡ Status Atual

```
Etapa A: Exploração de Dados           ✅ CONCLUÍDO
Etapa B: Preparação de Dados           ⬜ PRONTO PARA EXECUTAR
Etapa C: Amostragem                    ⬜ PRONTO PARA EXECUTAR
Etapa D: Análise Descritiva            ⬜ PRONTO PARA EXECUTAR
Etapa E: Inferência Estatística        ⬜ PRONTO PARA EXECUTAR
Etapa F: Painéis Interativos           ⬜ PRONTO PARA EXECUTAR
Etapa G: Vídeo e Entrega               ⬜ PENDENTE
```

---

## 🚀 Execução Rápida

### Instalar dependências (1 vez)
```bash
pip install -r requirements.txt
```

### Reexecutar o pipeline (se necessário)
```bash
python scripts/02_preparacao_dados.py
python scripts/03_amostragem.py
python scripts/04_analise_descritiva.py
python scripts/05_inferencia_estatistica.py
```

Os painéis ainda não foram implementados; não há comando para abri-los.

---

## 📊 Dataset

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `iptu_2026.csv` |
| **Registros** | 876.248 imóveis |
| **Período** | 2026 |
| **Tamanho** | 210.53 MB |
| **Variáveis** | 32 colunas |
| **Fonte** | [Dados Abertos POA](https://dadosabertos.poa.br/dataset/iptu) |

### Tamanho da Amostra
```
n = 1.066 registros (95% confiança, 3% erro)
```

---

## 🎯 Hipóteses Estatísticas

| # | Tipo | Variável | H₀ | H₁ |
|---|------|----------|-----|------|
| 1️⃣ | Proporção | Apartamento | p = 0,40 | p ≠ 0,40 |
| 2️⃣ | Proporção | Residencial | p = 0,85 | p ≠ 0,85 |
| 3️⃣ | Média | Valor Venal | μ = 400k | μ ≠ 400k |
| 4️⃣ | Média | Área Construída | μ = 100 | μ ≠ 100 |

---

## 📁 Estrutura de Pastas

```
TrabalhoFinal/
│
├── 📄 Documentação
│   ├── 00_README.md                    ← Este registro histórico
│   ├── 00_LEIA_PRIMEIRO.md             ← Entrada humana
│   ├── 01_GUIA_PASSO_A_PASSO.md        ← Execução
│   ├── 02_REFERENCIA_TECNICA.md        ← Referência técnica
│   ├── 99_CONTEXT_PARA_AGENTES.md     ← Contexto para agentes
│   ├── GLOSSARIO_ESTATISTICO.md        ← Conceitos
│   ├── REFERENCIA_RAPIDA.md            ← Fatos e atalhos atuais
│   ├── RESUMO_REORGANIZACAO.md         ← Resumo da documentação
│   ├── README_ESTRUTURA.md             ← Mapa de leitura
│   ├── _MAPA_DE_LIMPEZA.md             ← Mapa da documentação
│   ├── 00_SUMARIO_EXECUTIVO.md         ← Registro histórico
│   └── roadmap.md                      ← Estado e etapas pendentes
│
├── 📄 Dados e Configuração
│   ├── iptu_2026.csv                   ← Dataset (210.53 MB)
│   ├── requirements.txt                ← Dependências Python
│   ├── Enunciado.txt                   ← Tarefa (disciplina)
│   ├── dicionario-de-dados.pdf         ← Variáveis (disciplina)
│   └── fonteDosDados.txt               ← Fonte (disciplina)
│
├── 📁 scripts/
│   ├── 01_exploracao_dados.py          ✅ Executado
│   ├── 02_preparacao_dados.py          ✅ Executado
│   ├── 03_amostragem.py                ✅ Executado
│   ├── 04_analise_descritiva.py        ✅ Executado
│   └── 05_inferencia_estatistica.py    ✅ Executado
│
├── 📁 dados_processados/
│   ├── dados_limpos.csv
│   ├── amostra.csv
│   ├── amostra_indices.csv
│   └── dados_com_indicador_amostra.csv
│
├── 📁 saidas/ (9 CSVs, resultados do pipeline)
│
└── Painéis, vídeo e links de entrega     ⬜ Pendentes
```

**Estado dos arquivos:** atualizado após executar os scripts 02–05 em
12/11/2026. A pasta `paineis/` não foi criada porque os painéis continuam
pendentes.

---

## 📞 Arquivos Gerados na Exploração

Executada a etapa de exploração (01_exploracao_dados.py). Saídas:

✅ **01_analise_ausencias.csv** (1,1 KB)
- Contagem de valores faltantes por variável
- Percentuais e ranking

✅ **01_descritivas_populacao.csv** (0,87 KB)
- Estatísticas descritivas (variáveis numéricas)
- Média, mediana, desvio-padrão, quartis

---

## ⚙️ Instalação do Ambiente

### Pré-requisitos
- Python 3.9+
- pip

### 1. Criar ambiente virtual (opcional)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Verificar instalação
```bash
python -c "import pandas, numpy, scipy, streamlit; print('✓ Tudo OK')"
```

---

## 🔄 Workflow de Execução

### Sequência Obrigatória

```
02_preparacao_dados.py
        ↓
03_amostragem.py
        ↓
04_analise_descritiva.py
        ↓
05_inferencia_estatistica.py
        ↓
Construir os três painéis interativos (pendente)
        ↓
Gravação de vídeo
        ↓
ENTREGA (links)
```

### Executar cada etapa
```bash
python scripts/02_preparacao_dados.py
python scripts/03_amostragem.py
python scripts/04_analise_descritiva.py
python scripts/05_inferencia_estatistica.py
```

---

## 📊 Painéis Esperados

### Painel 1: Análise Descritiva da População
- Estatísticas resumidas
- Distribuições por variável
- Gráficos (histogramas, boxplots, barras)
- Frequências qualitativas

### Painel 2: Análise Descritiva da Amostra
- Reprodução exata do Painel 1
- Usando apenas dados amostrais (n=1.066)
- Permitir comparação com população

### Painel 3: Inferência e Comparação
- Intervalos de confiança (2 proporções, 2 médias)
- Testes de hipóteses e valor-p
- Comparação com parâmetros populacionais
- Discussão de variabilidade amostral

---

## ⚠️ Pontos de Atenção

1. **Decimais com vírgula:** CSV usa `,` como separador
   - Converter ao ler (implementado nos scripts)

2. **Distribuição assimétrica:** Valor venal tem outliers
   - Documentar e validar pressupostos

3. **Valores faltantes:**
   - `des_uso`: 2,76% (24.152)
   - `mtr_area_construida_total`: 2,75% (24.057)
   - Outros: negligenciáveis

4. **Independência:** Múltiplas unidades por lote
   - Documentar possível falta de independência

5. **Reprodutibilidade:** Usar semente fixa
   - `random_state=42` (recomendado)

---

## 🔗 Recursos Úteis

### Documentação
- [Scipy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly Docs](https://plotly.com/python/)

### Dados
- [IPTU — Dados Abertos POA](https://dadosabertos.poa.br/dataset/iptu)

### Calculadoras
- [Tamanho Amostral — USP/Bauru](https://www.usp.br/)

---

## 🎓 Critérios de Avaliação

| Critério | Peso |
|----------|------|
| Escolha e descrição da base | 10% |
| Dimensionamento da amostra | 10% |
| Painel descritivo — população | 10% |
| Painel descritivo — amostra | 10% |
| Correção dos testes/intervalos | 20% |
| Interpretação e comparação | 20% |
| Qualidade da apresentação (vídeo) | 20% |
| **TOTAL** | **100%** |

---

## ✅ Checklist Inicial

- [x] Base de dados validada
- [x] Documentação criada
- [x] Scripts preparados
- [x] Ambiente pronto
- [x] Etapa A (exploração) concluída
- [ ] Etapa B (preparação) — PRÓXIMA
- [ ] Etapa C (amostragem)
- [ ] Etapa D (descritivas)
- [ ] Etapa E (inferência)
- [ ] Etapa F (painéis)
- [ ] Etapa G (vídeo)
- [ ] Entrega

---

## 🆘 Suporte

### Se algo não funcionar

**Erro: ModuleNotFoundError**
```bash
pip install --upgrade -r requirements.txt
```

**Erro: Arquivo não encontrado**
```bash
cd D:\Pós_IA\Disciplinas\IA003-estatistica\TrabalhoFinal
python scripts/02_preparacao_dados.py
```

**Erro: Lentidão**
- Normal com 876.248 linhas
- O script 02 carrega o CSV inteiro em memória; pode exigir alguns minutos e memória disponível.

---

## 📝 Próximas Ações

### Imediato (hoje)
1. Ler este documento (5 min)
2. Ler [01_GUIA_PASSO_A_PASSO.md](./01_GUIA_PASSO_A_PASSO.md) (10 min)
3. Verificar ambiente Python (2 min)

### Curto Prazo (próximas 24h)
```bash
pip install -r requirements.txt
python scripts/02_preparacao_dados.py
```

### Médio Prazo (próximos 3 dias)
- Completar etapas B-F
- Gerar painéis interativos
- Começar a gravar vídeo

---

## 📊 Contato e Informações

- **Aluno:** Sergio Prof.
- **Disciplina:** IA003 — Estatística
- **Data de Entrega:** 15 de novembro de 2026
- **Prazo Restante:** 8 dias

---

## 🎯 Registro histórico

Este documento registra a situação em 7 de novembro de 2026, antes da execução
dos scripts 02–05. Não use a recomendação de execução nem os status abaixo como
estado atual. Para a sequência vigente, comece por
[00_LEIA_PRIMEIRO.md](./00_LEIA_PRIMEIRO.md).

---

**Preparado em:** 7 de novembro de 2026  
**Tempo de preparação:** ~2 horas  
**Status naquele registro:** PRONTO PARA EXECUÇÃO

---

*Última atualização: 07/11/2026 15:45*
