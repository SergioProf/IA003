# 📊 Trabalho Final — Estatística IA003

## Análise de Amostragem, Intervalos de Confiança e Testes de Hipóteses  
### IPTU 2026 — Porto Alegre

---

## 🎯 Objetivo

Aplicar conceitos de **amostragem**, **estimação por intervalos de confiança** e **testes de hipóteses** na análise de uma grande base de dados (876.248 imóveis), comparando resultados populacionais com estimativas amostrais através de painéis interativos e apresentação em vídeo.

---

## 📋 Documentação

### 📌 Comece por aqui
1. **[GUIA_RAPIDO.md](./GUIA_RAPIDO.md)** ← Leia primeiro (5 min)
   - Resumo de tudo em uma página
   - Próximos passos
   - Timeline

2. **[00_SUMARIO_EXECUTIVO.md](./00_SUMARIO_EXECUTIVO.md)** ← Contexto completo
   - Validação dos dados
   - Análise de ausências
   - Dimensionamento da amostra
   - Hipóteses confirmadas

### 📚 Referência Detalhada
3. **[ANALISE_INICIAL.md](./ANALISE_INICIAL.md)** ← Análise profunda
   - Especificação da tarefa
   - Base de dados detalhada
   - Plano de execução completo
   - Todas as etapas descritas

4. **[AMBIENTE_TRABALHO.md](./AMBIENTE_TRABALHO.md)** ← Guia técnico
   - Estrutura de pastas
   - Dependências Python
   - Instruções de execução
   - Cronograma detalhado
   - Checklist de validação

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

### Executar próxima etapa
```bash
python scripts/02_preparacao_dados.py
```

### Abrir painéis (depois de tudo)
```bash
streamlit run paineis/app_streamlit.py
```

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
│   ├── 00_README.md                    ← Este arquivo
│   ├── GUIA_RAPIDO.md                  ← Resumo em 1 página
│   ├── 00_SUMARIO_EXECUTIVO.md         ← Análise executiva
│   ├── ANALISE_INICIAL.md              ← Análise completa
│   ├── AMBIENTE_TRABALHO.md            ← Guia técnico
│   └── roadmap.md                      ← Plano original (disciplina)
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
│   ├── 02_preparacao_dados.py          ⬜ Próximo
│   ├── 03_amostragem.py                ⬜ Pronto
│   ├── 04_analise_descritiva.py        ⬜ Pronto
│   └── 05_inferencia_estatistica.py    ⬜ Pronto
│
├── 📁 dados_processados/
│   ├── 01_analise_ausencias.csv        ✅ Criado
│   ├── 01_descritivas_populacao.csv    ✅ Criado
│   ├── amostra_indices.csv             (será criado)
│   ├── dados_limpos.csv                (será criado)
│   └── resultados_descritivos.csv      (será criado)
│
├── 📁 paineis/
│   ├── app_streamlit.py                ⬜ Pronto
│   ├── config.yaml                     (será criado)
│   └── assets/                         (será criado)
│
└── 📁 saidas/
    ├── relatorio_inferencia.md         (será criado)
    └── links_entrega.txt               (será criado)
```

---

## 📈 Timeline (8 dias)

| Data | Tarefa | Tempo | Status |
|------|--------|-------|--------|
| **07/11** | Preparação ambiente | 2h | ✅ |
| **07-08/11** | Preparação dados | 1h | ⬜ |
| **08/11** | Amostragem | 0.5h | ⬜ |
| **08-09/11** | Descritivas | 1.5h | ⬜ |
| **09/11** | Inferência | 1h | ⬜ |
| **09-10/11** | Painéis | 2h | ⬜ |
| **10-14/11** | Vídeo | 1.5h | ⬜ |
| **15/11** | **ENTREGA** | — | ⬜ |

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
paineis/app_streamlit.py
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
streamlit run paineis/app_streamlit.py
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
- Scripts usam chunks para eficiência

---

## 📝 Próximas Ações

### Imediato (hoje)
1. Ler este documento (5 min)
2. Ler [GUIA_RAPIDO.md](./GUIA_RAPIDO.md) (5 min)
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

## 🎯 Conclusão

✅ **O ambiente está completamente preparado e documentado.**

Todos os scripts estão prontos para execução sequencial. A base de dados foi validada, o tamanho amostral foi calculado e as hipóteses foram definidas.

**Comece pelo [GUIA_RAPIDO.md](./GUIA_RAPIDO.md) e execute `python scripts/02_preparacao_dados.py` em seguida.**

---

**Preparado em:** 7 de novembro de 2026  
**Tempo de preparação:** ~2 horas  
**Status:** 🟢 PRONTO PARA EXECUÇÃO

---

*Última atualização: 07/11/2026 15:45*
