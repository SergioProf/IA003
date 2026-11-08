# 01 — GUIA PASSO A PASSO

**Como executar os scripts com sucesso**

---

## 📋 Antes de Começar — Checklist

- [ ] Terminal aberto
- [ ] Python 3.9+ instalado
- [ ] Arquivo `iptu_2026.csv` na pasta (verificar)
- [ ] Dependências instaladas (fazer agora)

---

## ✅ Etapa 1: Preparar o Ambiente

### Passo 1.1: Abrir Terminal

**No Windows:**
1. Pressione `Win + R`
2. Digite `cmd` ou `powershell`
3. Pressione Enter

**Ou clique com botão direito na pasta e escolha:** "Abrir PowerShell aqui"

### Passo 1.2: Navegar até a Pasta

```bash
cd D:\Pós_IA\Disciplinas\IA003-estatistica\TrabalhoFinal
```

Verificar se está correto:
```bash
dir iptu_2026.csv
```

Deve mostrar: `iptu_2026.csv` com tamanho de ~210 MB

### Passo 1.3: Instalar Dependências

**Primeira vez apenas:**
```bash
pip install -r requirements.txt
```

Vai demorar 1-2 minutos. Vai aparecer muito texto (normal!)

**Se der erro:**
```bash
pip install --upgrade pandas numpy scipy scikit-learn
```

---

## 🎯 Etapa 2: Executar Script 02

**O que faz:** Limpa e prepara os dados

### Comando:
```bash
python scripts/02_preparacao_dados.py
```

### O que vai ver:
```
================================================================================
PREPARAÇÃO DE DADOS — IPTU 2026 Porto Alegre
================================================================================

📂 Carregando dados de: D:\...\iptu_2026.csv
✓ Sucesso! 876,248 linhas lidas

[... muitas informações ...]

💾 Arquivos salvos com sucesso!

🎉 PREPARAÇÃO DE DADOS CONCLUÍDA COM SUCESSO!
================================================================================
```

### Tempo esperado: 2-3 minutos

### Verificar resultado:
- Procure por: `dados_processados/dados_limpos.csv`
- Deve ter ~876.248 linhas

---

## 🎯 Etapa 3: Executar Script 03

**O que faz:** Sorteia uma amostra de 1.066 registros

### Comando:
```bash
python scripts/03_amostragem.py
```

### O que vai ver:
```
================================================================================
AMOSTRAGEM — IPTU 2026 Porto Alegre
================================================================================

📂 Carregando dados preparados...
✓ Sucesso! 876,248 linhas lidas

RESULTADO: n ≈ 1.066 imóveis
✓ Amostra sorteada!

💾 Salvando amostra...
✓ Arquivo criado: amostra.csv

🎉 AMOSTRAGEM CONCLUÍDA COM SUCESSO!
================================================================================
```

### Tempo esperado: 1-2 minutos

### Verificar resultado:
- Procure por: `dados_processados/amostra.csv`
- Deve ter ~1.066 linhas

---

## 🎯 Etapa 4: Executar Script 04

**O que faz:** Calcula estatísticas (média, mediana, etc)

### Comando:
```bash
python scripts/04_analise_descritiva.py
```

### O que vai ver:
```
================================================================================
ANÁLISE DESCRITIVA — IPTU 2026 Porto Alegre
================================================================================

📂 Carregando dados...
✓ Sucesso! 876,248 linhas lidas

CALCULANDO ESTATÍSTICAS...
✓ vlr_venal_imovel
✓ mtr_area_construida_total
✓ vlr_imposto
✓ vlr_aliquota

CALCULANDO FREQUÊNCIAS...
✓ des_finalidade
✓ des_uso
✓ nme_endloc_bairro_cdl
✓ num_divisao_fiscal

💾 Arquivos salvos...
✓ 8 arquivos CSV criados

🎉 ANÁLISE DESCRITIVA CONCLUÍDA COM SUCESSO!
================================================================================
```

### Tempo esperado: 3-5 minutos

### Verificar resultado:
- Procure por pasta: `saidas/`
- Deve ter 8 arquivos CSV

---

## 🎯 Etapa 5: Executar Script 05

**O que faz:** Faz testes de hipóteses

### Comando:
```bash
python scripts/05_inferencia_estatistica.py
```

### O que vai ver:
```
================================================================================
INFERÊNCIA ESTATÍSTICA — IPTU 2026 Porto Alegre
================================================================================

📂 Carregando dados...
✓ Sucesso! 876,248 linhas lidas

TESTANDO HIPÓTESES...
✓ H1: Proporção de Apartamentos
✓ H2: Proporção de Uso Residencial
✓ H3: Média do Valor Venal
✓ H4: Média da Área Construída

💾 Salvando resultados...
✓ testes_hipoteses.csv criado

🎉 INFERÊNCIA ESTATÍSTICA CONCLUÍDA COM SUCESSO!
================================================================================
```

### Tempo esperado: 1-2 minutos

### Verificar resultado:
- Procure por: `saidas/testes_hipoteses.csv`
- Deve ter 4 testes resumidos

---

## 🎉 Tudo Pronto!

### Resumo da Execução

```
Total de tempo: 10-15 minutos ✓

Arquivos criados:
├── dados_processados/ (4 arquivos)
└── saidas/ (9 arquivos)

Total: 13 arquivos de resultado
```

---

## ⚠️ Se Algo Der Errado

### Erro: "Arquivo não encontrado"

**Solução:**
1. Verifique se está na pasta correta:
```bash
pwd  # mostra pasta atual
```

2. Verifique se `iptu_2026.csv` existe:
```bash
dir iptu_2026.csv
```

3. Se não existir, o arquivo está na pasta errada

### Erro: "ModuleNotFoundError: No module named 'pandas'"

**Solução:**
```bash
pip install --upgrade pandas numpy scipy
```

### Erro: "Python não é reconhecido"

**Solução:**
1. Reinicie o computador depois de instalar Python
2. Ou use o caminho completo:
```bash
C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python310\python.exe scripts/02_preparacao_dados.py
```

### Demora muito para carregar dados

**É normal!** O arquivo tem 210 MB. Pode levar até 1 minuto.

---

## 💡 Dicas Úteis

### Salvar saída em arquivo
```bash
python scripts/02_preparacao_dados.py > log.txt
```

Depois abra `log.txt` no Notepad para rever toda a saída.

### Executar vários de uma vez
```bash
python scripts/02_preparacao_dados.py && python scripts/03_amostragem.py && python scripts/04_analise_descritiva.py && python scripts/05_inferencia_estatistica.py
```

Isso executa todos na sequência (recomendado!).

### Ver quanto tempo levou
Note a hora no início e no final.

---

## 📖 Documentação por Arquivo

| Script | Documentação |
|--------|-------------|
| 02_preparacao_dados.py | Comece aqui |
| 03_amostragem.py | Depois deste |
| 04_analise_descritiva.py | Depois deste |
| 05_inferencia_estatistica.py | Por último |

---

## ✅ Checklist de Conclusão

- [ ] Executou script 02 com sucesso
- [ ] Verificou `dados_processados/dados_limpos.csv`
- [ ] Executou script 03 com sucesso
- [ ] Verificou `dados_processados/amostra.csv`
- [ ] Executou script 04 com sucesso
- [ ] Verificou arquivos em `saidas/desc_*` e `saidas/freq_*`
- [ ] Executou script 05 com sucesso
- [ ] Verificou `saidas/testes_hipoteses.csv`

---

## 🎓 O Que Você Aprendeu

Ao executar todos os scripts, você fez:

1. ✅ Limpeza de dados (remoção de inconsistências)
2. ✅ Amostragem aleatória (estatística)
3. ✅ Análise descritiva (cálculo de médias, medianas, etc)
4. ✅ Testes de hipóteses (inferência estatística)

**Tudo isto em 10-15 minutos!**

---

## 🚀 Próximos Passos

Depois que terminar:

1. Revise os arquivos em `saidas/`
2. Abra `testes_hipoteses.csv` para ver as conclusões
3. Leia `02_REFERENCIA_TECNICA.md` para entender em detalhe
4. Próxima etapa: Criar painéis Streamlit

---

**Status:** 🟢 Pronto para executar!

Dúvidas? Releia esta documentação ou procure no código (tudo está comentado em Português!)
