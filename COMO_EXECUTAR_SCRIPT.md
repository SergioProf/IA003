# 🚀 Como Executar o Script de Exploração de Dados

## Passo-a-Passo Completo

Siga os passos abaixo para executar o script 01_exploracao_dados.py

---

## PASSO 1: Abra o Terminal/Prompt de Comando

### No Windows:
1. Pressione `Win + R`
2. Digite `cmd` ou `powershell`
3. Clique em Enter

OU

1. Clique com botão direito em qualquer pasta
2. Escolha "Abrir PowerShell aqui" ou "Abrir Terminal aqui"

### No Linux/Mac:
1. Abra o Terminal (pesquise por "Terminal")

---

## PASSO 2: Navegue até a Pasta do Projeto

Copie e cole no terminal:

```bash
cd D:\Pós_IA\Disciplinas\IA003-estatistica\TrabalhoFinal
```

**O que significa:**
- `cd` = "change directory" (mudar de pasta)
- O caminho é onde estão os arquivos do projeto

**Como verificar:** Você deve ver o caminho mudando no terminal.

---

## PASSO 3: Instale as Dependências (se ainda não fez)

Execute uma única vez:

```bash
pip install -r requirements.txt
```

**O que vai acontecer:**
- O Python vai baixar as bibliotecas necessárias (pandas, numpy, etc)
- Pode demorar 1-2 minutos
- Vai aparecer muito texto na tela (é normal!)
- Quando terminar, você volta ao prompt

**Dica:** Se der erro, tente:
```bash
pip install --upgrade -r requirements.txt
```

---

## PASSO 4: Execute o Script

Digite este comando:

```bash
python scripts/01_exploracao_dados.py
```

**O que vai acontecer:**
1. O Python vai carregar o arquivo CSV (876.248 linhas) — isso demora alguns segundos
2. Vai aparecer muitos números e tabelas na tela
3. No final, vai dizer "EXPLORAÇÃO CONCLUÍDA"
4. Dois novos arquivos serão criados:
   - `01_analise_ausencias.csv`
   - `01_descritivas_populacao.csv`

---

## PASSO 5: Veja a Saída do Script

O terminal vai mostrar:

```
================================================================================
EXPLORAÇÃO INICIAL — IPTU 2026 Porto Alegre
================================================================================

Arquivo: D:\Pós_IA\Disciplinas\IA003-estatistica\TrabalhoFinal\iptu_2026.csv
Existe: True

================================================================================
SEÇÃO 2: CARREGANDO O ARQUIVO DE DADOS
================================================================================

✓ Sucesso! Lido: 876,248 linhas (imóveis) e 32 colunas (informações)

[... muitos números aparecerão aqui ...]

================================================================================
SEÇÃO 10: SALVANDO RESULTADOS EM ARQUIVOS
================================================================================

Salvando análise de dados faltantes...
✓ Arquivo criado: 01_analise_ausencias.csv

Salvando estatísticas descritivas...
✓ Arquivo criado: 01_descritivas_populacao.csv

💾 Arquivos salvos com sucesso!

🎉 EXPLORAÇÃO DE DADOS CONCLUÍDA COM SUCESSO!
```

---

## PASSO 6: Verifique se os Arquivos Foram Criados

Os dois arquivos devem aparecer na pasta raiz do projeto:

```
TrabalhoFinal/
├── 01_analise_ausencias.csv          ✓ NOVO!
├── 01_descritivas_populacao.csv      ✓ NOVO!
├── iptu_2026.csv (original)
└── ... (outros arquivos)
```

**Para verificar:**

No Windows PowerShell:
```powershell
Get-Item *.csv
```

No Linux/Mac:
```bash
ls *.csv
```

---

## PASSO 7: Abra os Arquivos Gerados

### Opção A: No Excel
1. Procure por `01_analise_ausencias.csv` na pasta
2. Clique duas vezes para abrir no Excel
3. Repita para `01_descritivas_populacao.csv`

### Opção B: No Google Sheets
1. Acesse drive.google.com
2. Clique em "Novo" → "Upload"
3. Selecione os arquivos CSV
4. Abra no Google Sheets

### O Que Você Vai Ver

**01_analise_ausencias.csv:**
```
Coluna,Faltantes,Percentual (%)
nivel,794604,90.68254649368671
complemento,764494,87.24630469912627
pavimento,402407,45.92387086760826
[... mais linhas ...]
des_finalidade,0,0.0
```

Isso mostra: quantos dados faltam em cada coluna.

**01_descritivas_populacao.csv:**
```
,count,mean,std,min,25%,50%,75%,max
ano_exercicio,876248.0,2026.0,0.0,2026.0,2026.0,2026.0,2026.0,2026.0
num_divisao_fiscal,876248.0,1.948680,0.868459,1.0,1.0,2.0,3.0,3.0
[... mais linhas ...]
```

Isso mostra: números resumidos (média, mínimo, máximo, etc).

---

## ⚠️ Se Algo Dar Errado

### Erro: "Python não é reconhecido"

**Solução:**
```bash
C:\Users\SeuUsuario\AppData\Local\Python\pythoncore-3.14-64\python.exe scripts/01_exploracao_dados.py
```

Ou reinicie o computador depois de instalar Python.

### Erro: "Arquivo não encontrado"

**Solução:**
1. Verifique se você está na pasta correta:
   ```powershell
   pwd   # mostra pasta atual
   ```

2. Verifique se `iptu_2026.csv` existe:
   ```powershell
   Get-Item iptu_2026.csv
   ```

### Erro: "ModuleNotFoundError: No module named 'pandas'"

**Solução:**
```bash
pip install --upgrade pandas numpy scipy
```

### Demora Muito Para Carregar

**É normal!** O arquivo tem 210 MB. Pode levar 30-60 segundos.

---

## 📊 Interpretando a Saída

### Quando Vir Isto:
```
✓ Sucesso! Lido: 876,248 linhas
```
**Significa:** O arquivo foi carregado corretamente! Próximo passo começou.

### Quando Vir Isto:
```
📊 vlr_venal_imovel
   Valores preenchidos: 876.205 de 876.248
   Média: 387,720.50
```
**Significa:** 
- Essa variável tem 876.205 valores válidos (43 faltam)
- O imóvel médio custa R$ 387.720,50
- Há imóveis muito mais caros ou mais baratos

### Quando Vir Isto:
```
🏷️  des_finalidade
   Quantidade de categorias diferentes: 45
   Categorias mais comuns:
```
**Significa:** 
- Há 45 tipos diferentes de finalidade de imóvel
- Vai listar os 10 mais comuns

### Quando Vir Isto:
```
Linhas duplicadas encontradas: 5
```
**Significa:** 
- Há 5 linhas que são cópias exatas de outras
- Precisamos remover essas duplicatas depois

---

## ✅ Checklist de Sucesso

- [x] Terminal aberto
- [x] Navegou até a pasta certa
- [x] Dependências instaladas
- [x] Script executado: `python scripts/01_exploracao_dados.py`
- [x] Mensagem "EXPLORAÇÃO CONCLUÍDA" apareceu
- [x] Dois arquivos CSV foram criados
- [x] Abriu os arquivos CSV para visualizar

---

## 🎯 O Que Fazer Depois

### 1. Entender os Resultados
- Leia o documento `GLOSSARIO_ESTATISTICO.md`
- Abra os arquivos CSV e veja os números
- Procure entender o que cada número significa

### 2. Próxima Etapa
Quando estiver pronto, execute:

```bash
python scripts/02_preparacao_dados.py
```

---

## 💾 Dicas Úteis

### Salvar a Saída do Script em um Arquivo
```bash
python scripts/01_exploracao_dados.py > saida_exploracao.txt
```

Isso cria um arquivo `saida_exploracao.txt` com tudo que apareceu.

### Executar o Script e Pausar no Final
```bash
python scripts/01_exploracao_dados.py && pause
```

Isso mantém a janela aberta para você ler tudo (Windows).

### Ver Quantas Linhas o Script Executou
Procure pela linha:
```
✓ Sucesso! Lido: 876,248 linhas
```

---

## 📞 Perguntas Frequentes

**P: Preciso fechar e abrir de novo a pasta cada vez?**
R: Não! Na mesma janela do terminal, você pode executar o próximo script.

**P: Quanto tempo leva?**
R: Cerca de 30-60 segundos. Varia com a velocidade do computador.

**P: Os arquivos CSV vão substituir os antigos?**
R: Sim! Cada vez que executa o script, recria os arquivos. Isso é ok.

**P: Preciso lembrar desses comandos de cor?**
R: Não! Copie e cole os comandos deste documento no terminal.

---

**Preparado em:** 7 de novembro de 2026  
**Para:** Primeira execução do script  
**Tempo estimado:** 5 minutos (+ 1 minuto para o script rodar)

🎉 **Boa sorte! Você consegue!**
