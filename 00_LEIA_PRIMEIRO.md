# 🎯 LEIA PRIMEIRO — Guia de Início Rápido

**Tempo de leitura:** 3 minutos  
**Status:** Pipeline 02–05 executado com o código atual | ⬜ Painéis e vídeo pendentes

---

## 📌 Três Fatos Essenciais

1. **Você tem 5 scripts Python prontos**
   - 1 para exploração (já feito)
   - 4 novos para análise completa

2. **Scripts 02–05: aproximadamente 10-15 minutos**
   - Esta estimativa cobre apenas o pipeline de análise, não os painéis nem o vídeo

3. **Seguir a sequência: 02 → 03 → 04 → 05**
   - Cada script depende do anterior

---

## 🚀 Comece Agora (3 passos)

### 1️⃣ Abra o Terminal
```bash
cd D:\Pós_IA\Disciplinas\IA003-estatistica\TrabalhoFinal
```

### 2️⃣ Instale dependências (primeira vez)
```bash
pip install -r requirements.txt
```

### 3️⃣ Execute os scripts na ordem
```bash
python scripts/02_preparacao_dados.py
python scripts/03_amostragem.py
python scripts/04_analise_descritiva.py
python scripts/05_inferencia_estatistica.py
```

Os scripts geram os arquivos de preparação, amostra e análise. Os scripts
02–05 foram executados após os ajustes recentes e os CSVs foram atualizados.
Os painéis interativos e o vídeo exigidos no enunciado ainda precisam ser
produzidos.

---

## 📚 Próximos Passos (Escolha um)

### Se Quer Entender Antes de Executar
👉 Leia: **`01_GUIA_PASSO_A_PASSO.md`** (5 min)

### Se Quer Detalhes Técnicos
👉 Leia: **`02_REFERENCIA_TECNICA.md`** (20 min)

### Se Quer Executar Agora
👉 Vá para o terminal e execute os comandos acima

---

## ✨ O Que Os Scripts Fazem

| # | Script | Ação | Tempo |
|---|--------|------|-------|
| 2 | `02_preparacao_dados.py` | Limpa dados | 2-3 min |
| 3 | `03_amostragem.py` | Sorteia amostra | 1-2 min |
| 4 | `04_analise_descritiva.py` | Calcula estatísticas | 3-5 min |
| 5 | `05_inferencia_estatistica.py` | Testa hipóteses | 1-2 min |

---

## 📊 Dados Processados

- **Base original:** 876.248 registros, 32 colunas
- **População analítica após remover 5 duplicatas:** 876.243 registros
- **Amostra:** 1.066 registros
- **Testes:** 4 hipóteses
- **Saídas analíticas:** 8 CSVs descritivos + 1 CSV de testes

---

## ✅ Você Vai Ter

Após executar tudo:

```
dados_processados/
├── dados_limpos.csv
├── amostra.csv
├── amostra_indices.csv
└── dados_com_indicador_amostra.csv

saidas/
├── desc_<variável>.csv (4 arquivos comparando população e amostra)
├── freq_<variável>.csv (4 arquivos comparando população e amostra)
└── testes_hipoteses.csv
```

Os 13 arquivos CSV citados neste bloco correspondem a 4 arquivos
intermediários em `dados_processados/` e 9 resultados em `saidas/`, gerados
pela execução mais recente do pipeline.

---

## ❓ Perguntas Rápidas

**P: Quanto tempo leva?**  
R: A execução dos scripts 02–05 é estimada em 10-15 minutos. Painéis e vídeo
exigidos no enunciado são etapas separadas e continuam pendentes.

**P: Posso executar um de cada vez?**  
R: Sim! Mas devem ser na ordem 02 → 03 → 04 → 05

**P: O que se der erro?**  
R: Leia a mensagem de erro. Provavelmente falta instalar dependências

**P: Onde encontro ajuda?**  
R: Veja `01_GUIA_PASSO_A_PASSO.md`, seção "Se Algo Der Errado".

---

## 📖 Documentação

| Arquivo | Quando Usar |
|---------|------------|
| **00_LEIA_PRIMEIRO.md** | Agora (você está aqui) |
| 01_GUIA_PASSO_A_PASSO.md | Quer entender como executar |
| 02_REFERENCIA_TECNICA.md | Quer detalhes técnicos |
| 99_CONTEXT_PARA_AGENTES.md | Para agentes IA/LLM |

---

## 🎯 Decisão: O Que Fazer Agora?

### Opção A: Executar Logo
```bash
python scripts/02_preparacao_dados.py
```
↳ Vá para o terminal e comece!

### Opção B: Entender Antes
👉 Leia `01_GUIA_PASSO_A_PASSO.md` (5 min)

### Opção C: Referência Completa
👉 Leia `02_REFERENCIA_TECNICA.md` (20 min)

---

## ⏱️ Timeline

```
Agora       → Você lê este arquivo (3 min) ← VOCÊ ESTÁ AQUI
            → Decide ler 01 ou executar
5 min       → Começa execução (se escolher 01 primeiro)
15-20 min   → Tudo terminado ✓
```

---

**Status:** 🟢 Pronto!  
**Próximo:** Escolha uma opção acima!

🚀 **Vamos começar?**
