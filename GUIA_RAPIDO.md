# 🚀 GUIA RÁPIDO — Início Imediato

## Estado Atual: ✅ AMBIENTE PRONTO

**Última atualização:** 7 de novembro de 2026, 15:45  
**Prazo de entrega:** 15 de novembro de 2026

---

## 📊 Dados Validados

| Aspecto | Valor |
|---------|-------|
| **Dataset** | `iptu_2026.csv` ✅ |
| **Registros** | 876.248 imóveis |
| **Colunas** | 32 variáveis |
| **Tamanho** | 210.53 MB |
| **Período** | 2026 |
| **Duplicatas** | 5 (negligenciável) |

---

## 📋 Amostra Dimensionada

```
Nível de Confiança:  95%  (z = 1,96)
Margem de Erro:      3%   (E = 0,03)
Proporção:           50%  (p = 0,50)
População:           N = 876.248

RESULTADO:  n ≈ 1.066 imóveis
```

---

## 🎯 Hipóteses Estatísticas

| # | Tipo | Variável | H₀ | H₁ | α |
|---|------|----------|----|----|---|
| 1️⃣ | Proporção | Finalidade = Apartamento | p = 0,40 | p ≠ 0,40 | 0,05 |
| 2️⃣ | Proporção | Uso = Residencial | p = 0,85 | p ≠ 0,85 | 0,05 |
| 3️⃣ | Média | Valor Venal (R$) | μ = 400k | μ ≠ 400k | 0,05 |
| 4️⃣ | Média | Área Construída (m²) | μ = 100 | μ ≠ 100 | 0,05 |

---

## 🔄 Próximos Passos (Em Ordem)

### 1. Preparação de Dados (30 min)
```bash
python scripts/02_preparacao_dados.py
```
Saída: `dados_limpos.csv`

### 2. Amostragem (15 min)
```bash
python scripts/03_amostragem.py
```
Saída: `amostra_indices.csv`

### 3. Análise Descritiva (45 min)
```bash
python scripts/04_analise_descritiva.py
```
Saída: Gráficos e tabelas (pop. + amostra)

### 4. Inferência Estatística (30 min)
```bash
python scripts/05_inferencia_estatistica.py
```
Saída: Testes e intervalos

### 5. Painéis Interativos (2h)
```bash
streamlit run paineis/app_streamlit.py
```
Saída: 3 painéis web + links públicos

### 6. Vídeo (1h)
Gravar e publicar no YouTube (máx. 5 min)

---

## 📁 Estrutura Criada

```
TrabalhoFinal/
├── 📄 00_SUMARIO_EXECUTIVO.md      ← Resumo detalhado (novo)
├── 📄 ANALISE_INICIAL.md           ← Análise completa (novo)
├── 📄 AMBIENTE_TRABALHO.md         ← Guia de execução (novo)
├── 📄 GUIA_RAPIDO.md               ← Este arquivo
├── 📄 requirements.txt             ← Dependências Python (novo)
│
├── 📁 scripts/
│   ├── 01_exploracao_dados.py      ✅ EXECUTADO
│   ├── 02_preparacao_dados.py      ⬜ PRONTO
│   ├── 03_amostragem.py            ⬜ PRONTO
│   ├── 04_analise_descritiva.py    ⬜ PRONTO
│   └── 05_inferencia_estatistica.py ⬜ PRONTO
│
├── 📁 dados_processados/           (será preenchido)
├── 📁 paineis/                     (será preenchido)
└── 📁 saidas/                      (será preenchido)
```

---

## ⚙️ Dependências

### Instalar (uma única vez)
```bash
pip install -r requirements.txt
```

### Principais bibliotecas
- **pandas** — Leitura/manipulação de dados
- **numpy** — Operações numéricas
- **scipy** — Testes estatísticos
- **scikit-learn** — Amostragem aleatória
- **plotly** — Gráficos interativos
- **streamlit** — Dashboards web

---

## 🎒 Checklist Rápido

### Antes de começar
- [ ] Ter `iptu_2026.csv` na pasta raiz
- [ ] Ter Python 3.9+ instalado
- [ ] Ter executado `pip install -r requirements.txt`

### Durante o trabalho
- [ ] Executar scripts em sequência
- [ ] Verificar saídas de cada etapa
- [ ] Documentar decisões metodológicas
- [ ] Manter semente de aleatoriedade fixa

### Antes de entregar
- [ ] Validar 3 painéis (pop., amostra, inferência)
- [ ] Vídeo gravado e publicado
- [ ] Links compartilhados e públicos
- [ ] Todos os documentos completados

---

## 📞 Referência Rápida — Variáveis Chave

### Para Proporção
- **Finalidade:** `des_finalidade` (valores: Apartamento, Casa, etc.)
- **Uso:** `des_uso` (valores: Residencial, Comercial, etc.)

### Para Média
- **Valor Venal:** `vlr_venal_imovel` (em R$, usar vírgula→ponto)
- **Área Construída:** `mtr_area_construida_total` (em m²)

### Para Contexto
- **Bairro:** `nme_endloc_bairro_cdl`
- **Divisão Fiscal:** `num_divisao_fiscal` (1, 2 ou 3)

---

## ⚠️ Pontos de Atenção

1. **Decimais com vírgula:** CSV usa `,` como separador decimal
2. **Distribuição assimétrica:** Valor venal tem outliers — documentar
3. **Ausências:** `des_uso` (2.76%) e `mtr_area_construida_total` (2.75%)
4. **Tamanho grande:** População N = 876.248 permite aproximação normal
5. **Reprodutibilidade:** Usar semente fixa (ex: `random_state=42`)

---

## 📈 Timeline Estimada

```
07/11 (hoje)   → Preparação ✅         (2h)
07-08/11       → Etapas B-C           (1.5h)
08-09/11       → Etapas D-E           (2h)
09-10/11       → Painel (Etapa F)     (2h)
10-14/11       → Vídeo (Etapa G)      (1.5h)
15/11          → ENTREGA              
─────────────────────────────────────
TOTAL:         ~9 horas de trabalho
```

---

## 🔗 Links Úteis

- 📚 [Scipy Stats Docs](https://docs.scipy.org/doc/scipy/reference/stats.html)
- 🎨 [Streamlit Docs](https://docs.streamlit.io)
- 📊 [Plotly Docs](https://plotly.com/python)
- 📖 [IPTU Porto Alegre](https://dadosabertos.poa.br/dataset/iptu)

---

## 🆘 Se Algo Quebrar

### Erro: "Arquivo não encontrado"
```bash
# Verificar se está na pasta correta
cd D:\Pós_IA\Disciplinas\IA003-estatistica\TrabalhoFinal
python scripts/01_exploracao_dados.py
```

### Erro: "ModuleNotFoundError"
```bash
# Reinstalar dependências
pip install --upgrade -r requirements.txt
```

### Lentidão ao processar dados
```bash
# Usar chunks para ler o CSV
# (já implementado nos scripts)
```

---

## 📝 Próxima Ação Imediata

**Execute em 5 minutos:**

```bash
cd D:\Pós_IA\Disciplinas\IA003-estatistica\TrabalhoFinal
pip install -r requirements.txt
python scripts/02_preparacao_dados.py
```

Depois disso, o próximo passo automático será `03_amostragem.py`.

---

**Status:** 🟢 PRONTO PARA EXECUÇÃO  
**Documentação:** Completa (4 arquivos .md)  
**Scripts:** 5 preparados (1 testado)  
**Tempo até entrega:** 8 dias

🎯 **Let's go!**
