# Ambiente de Trabalho — Trabalho Final de Estatística

## Estrutura de Pastas

```
TrabalhoFinal/
├── 📄 Enunciado.txt                    # Enunciado completo da tarefa
├── 📄 dicionario-de-dados.pdf          # Descrição das variáveis
├── 📄 fonteDosDados.txt                # Link da fonte dos dados
├── 📄 roadmap.md                       # Plano de execução
├── 📊 iptu_2026.csv                    # Dataset principal (210.53 MB)
├── 📄 ANALISE_INICIAL.md              # Esta análise (novo)
│
├── 📁 scripts/                         # Scripts Python
│   ├── 01_exploracao_dados.py          # Exploração inicial dos dados
│   ├── 02_preparacao_dados.py          # Limpeza e validação
│   ├── 03_amostragem.py                # Seleção da amostra aleatória
│   ├── 04_analise_descritiva.py        # Estatísticas descritivas
│   └── 05_inferencia_estatistica.py    # Testes e intervalos de confiança
│
├── 📁 dados_processados/               # Dados intermediários
│   ├── amostra_indices.csv             # Índices da amostra selecionada
│   ├── dados_limpos.csv                # Dataset após limpeza
│   └── resultados_descritivos.csv      # Sumários estatísticos
│
├── 📁 paineis/                         # Dashboards interativos
│   ├── app_streamlit.py                # Aplicação Streamlit (3 painéis)
│   ├── config.yaml                     # Configurações dos painéis
│   └── assets/                         # Imagens e ícones
│
└── 📁 saidas/                          # Resultados finais
    ├── relatorio_inferencia.md         # Resultados dos testes
    └── links_entrega.txt               # Links dos painéis e vídeo
```

## Dependências Python

```
pandas>=1.5.0
numpy>=1.23.0
scipy>=1.10.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0
streamlit>=1.28.0
```

## Instalação do Ambiente

### 1. Criar virtualenv
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

## Etapas de Execução

### ✅ Etapa A: Exploração e Validação
**Script:** `01_exploracao_dados.py`  
**Tempo estimado:** 30-45 min  
**Saída:** Relatório de validação, análise de ausências

```bash
python scripts/01_exploracao_dados.py
```

### ⬜ Etapa B: Preparação dos Dados
**Script:** `02_preparacao_dados.py`  
**Tempo estimado:** 20-30 min  
**Saída:** Dataset limpo e validado

```bash
python scripts/02_preparacao_dados.py
```

### ⬜ Etapa C: Amostragem
**Script:** `03_amostragem.py`  
**Tempo estimado:** 10-15 min  
**Saída:** Índices e dados da amostra (n ≈ 1.066)

```bash
python scripts/03_amostragem.py
```

### ⬜ Etapa D: Análise Descritiva
**Script:** `04_analise_descritiva.py`  
**Tempo estimado:** 30-45 min  
**Saída:** Estatísticas e gráficos (população e amostra)

```bash
python scripts/04_analise_descritiva.py
```

### ⬜ Etapa E: Inferência Estatística
**Script:** `05_inferencia_estatistica.py`  
**Tempo estimado:** 20-30 min  
**Saída:** Intervalos de confiança e testes de hipóteses

```bash
python scripts/05_inferencia_estatistica.py
```

### ⬜ Etapa F: Painéis Interativos
**Script:** `paineis/app_streamlit.py`  
**Tempo estimado:** 45-60 min  
**Saída:** Aplicação Streamlit com 3 painéis interativos

```bash
streamlit run paineis/app_streamlit.py
```

### ⬜ Etapa G: Vídeo
**Ferramentas:** OBS Studio + YouTube  
**Tempo estimado:** 45-60 min  
**Saída:** Vídeo de até 5 minutos no YouTube

---

## Cronograma

| Data | Etapa | Status | Notas |
|------|-------|--------|-------|
| 07/11 | Análise inicial | ✅ Concluído | Documentação e escopo |
| 07-08/11 | Exploração (A) | ⬜ Pendente | Scripts preparados |
| 08-09/11 | Preparação (B) | ⬜ Pendente | Limpeza de dados |
| 09/11 | Amostragem (C) | ⬜ Pendente | n ≈ 1.066 registros |
| 09-10/11 | Descritivas (D) | ⬜ Pendente | Pop. e amostra |
| 10/11 | Inferência (E) | ⬜ Pendente | 4 hipóteses |
| 10-11/11 | Painéis (F) | ⬜ Pendente | Streamlit |
| 11-14/11 | Vídeo (G) | ⬜ Pendente | YouTube |
| 15/11 | **ENTREGA** | ⬜ Pendente | Links finais |

---

## Checklist de Validação

### Dados
- [ ] Dataset carregado corretamente (876.248 linhas)
- [ ] Separador e codificação validados
- [ ] Ausências documentadas por variável
- [ ] Duplicatas verificadas
- [ ] Tipos de dados confirmados

### Amostragem
- [ ] Tamanho amostral calculado (n ≈ 1.066)
- [ ] Semente de aleatoriedade fixada
- [ ] Índices da amostra salvos
- [ ] Método AAS documentado

### Análise Descritiva
- [ ] Média, mediana, desvio-padrão calculados
- [ ] Distribuições examinadas (histogramas, boxplots)
- [ ] Categorias de variáveis qualitativas documentadas
- [ ] Comparação população vs. amostra realizada

### Inferência
- [ ] 4 hipóteses formuladas e justificadas
- [ ] Intervalos de confiança calculados
- [ ] Testes de hipóteses executados
- [ ] Pressupostos verificados
- [ ] Valor-p e conclusões registrados
- [ ] Parâmetros populacionais calculados para comparação

### Painéis
- [ ] Painel 1 (População): Descritivas e gráficos
- [ ] Painel 2 (Amostra): Reprodução com dados amostrais
- [ ] Painel 3 (Inferência): Testes e comparações
- [ ] Interatividade testada
- [ ] Links acessíveis e públicos

### Vídeo
- [ ] Roteiro escrito (máx. 5 min)
- [ ] Gravação realizada
- [ ] Edição completa
- [ ] Publicado no YouTube
- [ ] Link compartilhado

---

## Recursos Externos

- **Fonte dos dados:** [IPTU — Dados Abertos POA](https://dadosabertos.poa.br/dataset/iptu)
- **Calculadora amostral:** [USP/Bauru](https://www.usp.br/)
- **Streamlit:** [streamlit.io](https://streamlit.io)
- **Plotly:** [plotly.com](https://plotly.com)
- **Scipy Stats:** [docs.scipy.org](https://docs.scipy.org/doc/scipy/reference/stats.html)

---

## Contato e Dúvidas

- **Disciplina:** IA003 — Estatística
- **Aluno:** Sergio Prof.
- **Prazo:** 15 de novembro de 2026

---

**Preparado em:** 7 de novembro de 2026 | **Status:** 🟡 Preparação Inicial
