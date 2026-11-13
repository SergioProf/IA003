# 01 — GUIA PASSO A PASSO

**Como executar os scripts com sucesso**

---

## 📋 Antes de Começar — Checklist

- [x] Terminal aberto
- [x] Python 3.9+ instalado
- [x] Arquivo `iptu_2026.csv` na pasta (verificar)
- [x] Dependências instaladas (fazer agora)

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
✓ Sucesso! 876,248 registros lidos da base original

[... muitas informações ...]

💾 Arquivos salvos com sucesso!

🎉 PREPARAÇÃO DE DADOS CONCLUÍDA COM SUCESSO!
================================================================================
```

### Tempo esperado: 2-3 minutos

### Conversão de valores numéricos

O CSV usa vírgula como separador decimal (por exemplo, `500,0`). O script
converte essa vírgula para ponto antes de transformar as colunas numéricas em
`float`. Durante a execução, confira a quantidade de valores válidos exibida
para cada coluna. Se aparecer a indicação de valores não numéricos, esses
registros não puderam ser convertidos e devem ser verificados nos dados de
origem.

### Verificar resultado:
- Procure por: `dados_processados/dados_limpos.csv`
- Deve conter 876.243 registros após a remoção de 5 duplicatas

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
✓ Sucesso! 876,243 registros lidos

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
- Deve conter 1.066 registros (além do cabeçalho)

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
✓ Sucesso! 876,243 registros lidos

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
✓ 8 arquivos CSV descritivos criados

🎉 ANÁLISE DESCRITIVA CONCLUÍDA COM SUCESSO!
================================================================================
```

### Tempo esperado: 3-5 minutos

### Verificar resultado:
- Procure por pasta: `saidas/`
- Deve ter 8 arquivos CSV descritivos

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
✓ Sucesso! 876,243 registros lidos

TESTANDO HIPÓTESES...
✓ H1: Proporção de Apartamentos
✓ H2: Proporção de Uso Exclusivamente Residencial
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

## 📌 Situação das Entregas

### Resumo da Execução

```
Tempo estimado para executar os scripts 02–05: 10-15 minutos

Arquivos do pipeline:
├── dados_processados/ (4 arquivos)
└── saidas/ (9 arquivos)

Total: 13 arquivos CSV: 4 intermediários e 9 resultados em saidas/.

Os scripts 02–05 foram executados na ordem acima após os ajustes recentes e os
CSVs estão atualizados. Os três painéis locais estão disponíveis em `app.py`;
ainda faltam o vídeo de até 5 minutos e a publicação dos painéis em links de
acesso público.
```

## 📊 Abrir os Painéis Streamlit

Depois de executar os scripts 02 e 03 e instalar as dependências, inicie o
aplicativo na raiz do projeto:

```bash
python -m streamlit run app.py
```

Na navegação lateral, escolha um dos três painéis:

1. **População:** medidas e distribuições dos registros preparados.
2. **Amostra:** as mesmas medidas para os registros sorteados, com referência
   comparativa da população.
3. **Inferência e comparação:** quatro testes, intervalos de confiança,
   parâmetros populacionais e conclusões.

Os gráficos permitem selecionar variáveis e ajustar categorias ou a faixa
visível do histograma. O limite do histograma afeta somente a visualização; as
medidas descritivas usam todos os valores válidos. O aplicativo lê
`dados_processados/dados_com_indicador_amostra.csv` quando disponível; caso
contrário, usa `dados_painel/dados_painel.csv.gz`, versão reduzida para o deploy.
O aplicativo não altera os arquivos de dados.
Ao atualizar o arquivo de dados, o painel recarrega a versão modificada na
próxima interação.

### Publicar no Streamlit Community Cloud

Após executar os scripts 02 e 03, gere a base reduzida:

```bash
python scripts/06_exportar_dados_painel.py
```

Ela contém todos os registros, mas apenas as oito variáveis do painel e o
indicador da amostra; não contém endereços completos. Publique o arquivo gerado
no GitHub junto com o código. Gere-o novamente sempre que os dados preparados
ou a amostra mudarem. No Streamlit Community Cloud, selecione este repositório,
a branch `master` e o arquivo `app.py`. Para Python 3.14, as dependências
específicas estão definidas em `requirements.txt`.

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

- [x] Executou script 02 com sucesso
- [x] Verificou `dados_processados/dados_limpos.csv`
- [x] Executou script 03 com sucesso
- [x] Verificou `dados_processados/amostra.csv`
- [x] Executou script 04 com sucesso
- [x] Verificou arquivos em `saidas/desc_*` e `saidas/freq_*`
- [x] Executou script 05 com sucesso
- [x] Verificou `saidas/testes_hipoteses.csv`

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
4. Execute `python -m streamlit run app.py` e valide os três painéis
5. Publique os painéis e grave o vídeo de até 5 minutos

---

**Status:** Pipeline analítico e painéis locais prontos; vídeo e links finais pendentes.

Dúvidas? Releia esta documentação ou procure no código (tudo está comentado em Português!)
