# 🎬 ROTEIRO DE VÍDEO — Apresentação dos Painéis Streamlit
## IPTU 2026 — Porto Alegre

**Duração:** 4–5 minutos (máximo)  
**Público:** Docentes e colegas da disciplina IA003 (Estatística)  
**Linguagem:** Português (brasileiro)  
**Tom:** Profissional, explicativo, baseado em dados  

---

## 📺 ESTRUTURA DO VÍDEO

```
ABERTURA            0:00 — 0:15  (15 seg)
│
├─ PAINEL 1         0:15 — 1:30  (75 seg)
├─ PAINEL 2         1:30 — 2:45  (75 seg)
├─ PAINEL 3         2:45 — 4:30  (105 seg)
│
└─ ENCERRAMENTO     4:30 — 5:00  (30 seg)
────────────────────
TOTAL:                            ~5 minutos
```

---

## 🎯 ROTEIRO DETALHADO

### [00:00–00:15] ABERTURA

**O que mostrar:**
- Tela com título do projeto
- Logo ou imagem de Porto Alegre (opcional)
- Seu nome e data

**O que dizer:**
> "Olá. Eu sou Sérgio e esta é a apresentação de um análise estatística do IPTU de Porto Alegre no exercício de 2026.
> 
> Neste vídeo vou mostrar três painéis interativos desenvolvidos em Streamlit que apresentam a análise descritiva da população completa de 876 mil imóveis, a amostra sorteada de 1.066 registros, e os testes de hipóteses com intervalos de confiança.
> 
> Então vamos lá!."

**Tempo:** 15 segundos

---

### [00:15–01:30] PAINEL 1: ANÁLISE DESCRITIVA DA POPULAÇÃO

**Navegação:**
- Abra o Streamlit: `streamlit run app.py`
- Clique em **"População"** na barra lateral
- Selecione uma variável numérica primeiro (ex: "Valor venal do imóvel")

---

#### **Segmento 1A: Dados da População (00:15–00:45)**

**O que mostrar:**
- Painel de "População" carregado
- Selectbox "Variável para explorar" com a primeira variável numérica selecionada
- As três métricas no topo: "Registros", "Casos válidos", "Ausências"
- A tabela "Medidas descritivas" (N válido, Média, Mediana, Desvio-padrão, Min, Q1, Q3, Máximo)

**O que dizer:**
> "Este é o primeiro painel: **Análise descritiva da população**.
>
> A população analisada é a base do IPTU de Porto Alegre depois da preparação no script 02. Foram removidas linhas completamente vazias e 5 duplicatas; valores inválidos em campos numéricos foram tratados como ausentes, sem excluir o imóvel inteiro. Assim, trabalhamos com cerca de **876 mil registros únicos preparados** — não com o arquivo bruto sem tratamento.
>
> Aqui estou explorando o **Valor venal do imóvel**. Você pode ver:
>
> - **N válido:** quantos imóveis têm este valor registrado
> - **Média:** o valor médio — aproximadamente [leia o número exato da tela]
> - **Mediana:** o valor do meio, que é [leia] — note que é diferente da média, o que indica assimetria
> - **Desvio-padrão:** a dispersão dos valores em torno da média — bem grande, porque imóveis têm valores bem diversos
> - **Mínimo e Máximo:** o intervalo completo de valores
> - **Q1 e Q3:** o primeiro e terceiro quartis — 25% e 75% dos dados estão nestes pontos
>
> Lembre-se: a mediana é mais robusta a valores extremos do que a média. Aqui, a mediana é menor que a média, o que sugere que há alguns imóveis muito caros puxando a média para cima."

**Tempo:** 30 segundos

---

#### **Segmento 1B: Distribuição Visual (00:45–01:15)**

**O que mostrar:**
- Gráfico de densidade (histograma)
- Slider de percentil (deixe em 99%)
- Tabela com contagens de categorias (se numérica, pule; se categórica, mostre)

**O que dizer:**
> "Agora veja o gráfico de distribuição. Aqui você vê a **forma** como os valores se distribuem.
>
> Estou mostrando até o percentil 99%, o que exclui os 1% de imóveis mais caros. Mesmo assim, você vê a [descreva a forma]:
> Esta é uma distribuição **assimétrica à direita** — há uma cauda longa de imóveis caros

> Fora do intervalo exibido, há 8,762 registros. Estes são outliers — imóveis com valores muito altos."

**Tempo:** 30 segundos

---

#### **Segmento 1C: Variável Categórica (01:15–01:30)**

**O que fazer:**
- Mude a variável para uma categórica (ex: "Finalidade" ou "Uso")
- Mostre o gráfico de barras

**O que dizer:**
> "Deixa eu mudar para uma variável categórica — por exemplo, **Uso do imóvel**.
>
> Aqui você vê as categorias e o percentual de imóveis em cada uma. A categoria **[cite a maior]** é a mais frequente — [diga o percentual]% dos imóveis. As demais categorias representam [descreva brevemente].
>
> Note que [cite uma observação interessante, como] 'Imóveis residenciais representam a grande maioria, o que é típico de um cadastro de uma cidade'.
>
> A tabela abaixo mostra os números exatos."

**Tempo:** 15 segundos

---

### [01:30–02:45] PAINEL 2: ANÁLISE DESCRITIVA DA AMOSTRA

**Navegação:**
- Clique em **"Amostra"** na barra lateral
- Selecione a mesma variável numérica (para comparação)

---

#### **Segmento 2A: Diferença Entre Amostra e População (01:30–02:00)**

**O que mostrar:**
- Painel de "Amostra" carregado
- Métricas no topo (Registros: ~1.066, Casos válidos, Ausências)
- Tabela com três colunas: "Medida", "População", "Amostra"

**O que dizer:**
> "Este é o segundo painel: **Análise descritiva da amostra**.
>
> Enquanto a população tem 876 mil imóveis, a **amostra tem 1.066 registros** — aproximadamente 0,12% da população. Esta é uma amostra aleatória simples (AAS) sem reposição, sorteada com semente 42, para garantir reproducibilidade.
>
> A tabela agora mostra **três colunas**: a medida estatística, o valor na população completa, e o valor na amostra.
>
> Veja: para a variável **Valor venal**, a população tem média de [leia], enquanto a amostra tem média de [leia]. Muito próximas! Isto é um bom sinal — significa que a amostra é representativa da população.
>
> Compare também a mediana — na população é [leia], na amostra é [leia]. A semelhança sugere que o processo de amostragem funcionou bem."

**Tempo:** 30 segundos

---

#### **Segmento 2B: Comparação Visual (02:00–02:30)**

**O que mostrar:**
- Gráfico com **duas linhas** (População e Amostra sobrepostas)
- Menção ao slider de percentil

**O que dizer:**
> "Agora veja o gráfico de comparação. As duas linhas — **população em azul** e **amostra em vermelho** — seguem a mesma forma. Elas quase se sobrepõem!
>
> Isto confirma que a amostra **espelha bem a população**. Não há viés de seleção aparente.
>
> Note que ambas têm [descreva a forma — assimetria, bimodalidade, etc.]. A correlação visual é excelente.
>
> Se movimentarmos o slider para mostrar um percentil diferente, a similaridade continua. Isto é a prova de que o tamanho da amostra — 1.066 registros — foi suficiente para capturar as características da população."

**Tempo:** 30 segundos

---

#### **Segmento 2C: Ausências e Dados Faltantes (02:30–02:45)**

**O que mostrar:**
- Métricas de "Ausências" (mostr se houver)
- Menção à tabela abaixo (se aplicável)

**O que dizer:**
> "Um último ponto: veja a métrica de **Ausências**. A população tem [leia] ausências, a amostra tem [leia].
>
> Como a amostra foi sorteada aleatoriamente da população, proporcionalmente, o número de ausências é praticamente o mesmo percentualmente.
>
> Isto é outro indicador de que o processo de amostragem foi bem-sucedido e que a amostra é bem representativa."

**Tempo:** 15 segundos

---

### [02:45–04:30] PAINEL 3: INFERÊNCIA ESTATÍSTICA E TESTES DE HIPÓTESES

**Navegação:**
- Clique em **"Inferência e comparação"** na barra lateral

---

#### **Segmento 3A: O Que São Testes de Hipóteses (02:45–03:15)**

**O que mostrar:**
- Painel de "Inferência e comparação" carregado
- Título "Resumo dos quatro testes"
- A tabela principal com as 4 linhas de testes

**O que dizer:**
> "Este é o terceiro painel: **Inferência estatística e testes de hipóteses**.
>
> Agora saímos da estatística **descritiva** (que só descreve os dados) e entramos na **inferência** (que faz conclusões sobre a população com base na amostra).
>
> Vamos testar quatro hipóteses — afirmações sobre a população que são testadas usando dados da amostra.
>
> A ideia é simples:
> - Formulamos uma **hipótese nula** (H₀) — uma afirmação sobre a população
> - Coletamos dados da amostra
> - Calculamos uma **estatística de teste** — um número que resume a evidência contra H₀
> - Calculamos um **valor-p** — a probabilidade de observar estes dados se H₀ fosse verdadeira
> - Se o valor-p for muito pequeno (menor que 0,05), **rejeitamos H₀** — concluímos que H₀ provavelmente é falsa
> - Se o valor-p for grande, **não rejeitamos H₀** — os dados não contradizem H₀
>
> Nível de significância: **α = 5%** (padrão em estatística).
>
> Vamos aos quatro testes."

**Tempo:** 30 segundos

---

#### **Segmento 3B: Teste 1 — Proporção de Apartamentos (03:15–03:35)**

**O que mostrar:**
- Primeira linha da tabela: "Proporção de apartamentos"
- Expandir o expander correspondente (clique na linha)

**O que dizer:**
> "**Teste 1: Proporção de Apartamentos**
>
> A hipótese nula é: **p = 40%** — afirmamos que 40% dos imóveis em Porto Alegre são apartamentos.
>
> Vendo a tabela:
> - **Parâmetro populacional** (verdadeiro valor na população): [leia]%
> - **Estimativa amostral** (valor na amostra): [leia]%
> - **IC 95% da amostra** (intervalo de confiança): de [leia]% a [leia]%
> - **Valor-p**: [leia] — [SE > 0.05: GRANDE, MAIOR QUE 5%] [SE < 0.05: PEQUENO, MENOR QUE 5%]
> - **Decisão**: [Não rejeitar H₀ OU Rejeitar H₀]
>
> [Se não rejeita] Interpretação: Não temos evidência suficiente para contradizer a hipótese de que 40% dos imóveis são apartamentos. A diferença que observamos na amostra pode ser apenas variação aleatória.
>
> [Se rejeita] Interpretação: Rejeitamos a hipótese de 40%. A proporção de apartamentos é significativamente diferente de 40%. Olhando o parâmetro populacional e a estimativa, vemos que a proporção é [maior/menor] que 40%."

**Tempo:** 20 segundos

---

#### **Segmento 3C: Teste 2 — Proporção de Uso Exclusivamente Residencial (03:35–03:50)**

**O que mostrar:**
- Segunda linha: "Proporção de uso exclusivamente residencial"
- Expandir o expander

**O que dizer:**
> "**Teste 2: Proporção de Uso Exclusivamente Residencial**
>
> Hipótese nula: **p = 85%** — afirmamos que 85% dos imóveis com uso informado têm uso exclusivamente residencial.
>
> Os números:
> - **Parâmetro populacional**: [leia]%
> - **Estimativa amostral**: [leia]%
> - **IC 95%**: [leia]%
> - **Valor-p**: [leia] — [GRANDE OU PEQUENO?]
> - **Decisão**: [Não rejeitar H₀ OU Rejeitar H₀]
>
> [Se não rejeita] Não há evidência suficiente para rejeitar que 85% dos imóveis com uso informado sejam exclusivamente residenciais.
>
> [Se rejeita] A proporção real é significativamente diferente de 85%. A população real tem uma proporção de [leia]%, que é [maior/menor] que os 85% esperados.
>
> A categoria 'não exclusivamente residencial' é distinta e não significa necessariamente que o imóvel seja comercial."

**Tempo:** 15 segundos

---

#### **Segmento 3D: Teste 3 — Média do Valor Venal (03:50–04:10)**

**O que mostrar:**
- Terceira linha: "Média do valor venal"
- Expandir o expander

**O que dizer:**
> "**Teste 3: Média do Valor Venal do Imóvel**
>
> Hipótese nula: **μ = R$ 400.000** — afirmamos que o valor médio dos imóveis é 400 mil reais.
>
> Os resultados:
> - **Parâmetro populacional**: R$ [leia]
> - **Estimativa amostral**: R$ [leia]
> - **IC 95%**: de R$ [leia] a R$ [leia]
> - **Estatística t**: t = [leia] — isto é a razão entre a diferença observada e o erro-padrão
> - **Valor-p**: [leia] — [PEQUENO? GRANDE?]
> - **Decisão**: [Não rejeitar H₀ OU Rejeitar H₀]
>
> [Se rejeita — que é o caso esperado] Rejeitamos H₀! O valor médio real é significativamente diferente de 400 mil. Olhando o parâmetro populacional, a verdadeira média é R$ [MAIOR/MENOR]. 
>
> Este teste usa a distribuição **t de Student** porque estamos trabalhando com a média de uma variável contínua.
>
> Atenção: a distribuição de valores venais é muito assimétrica — há alguns imóveis caríssimos que puxam a média para cima. O teste pressupõe independência dos dados; em um lote podem haver vários imóveis, então há uma leve violação deste pressuposto."

**Tempo:** 20 segundos

---

#### **Segmento 3E: Teste 4 — Média da Área Construída (04:10–04:30)**

**O que mostrar:**
- Quarta linha: "Média da área construída"
- Expandir o expander

**O que dizer:**
> "**Teste 4: Média da Área Construída**
>
> Última hipótese: **μ = 100 m²** — afirmamos que o imóvel médio tem 100 metros quadrados construídos.
>
> Os dados:
> - **Parâmetro populacional**: [leia] m²
> - **Estimativa amostral**: [leia] m²
> - **IC 95%**: de [leia] m² a [leia] m²
> - **Valor-p**: [leia]
> - **Decisão**: [Não rejeitar H₀ OU Rejeitar H₀]
>
> [Se não rejeita] Não há evidência significativa de que a área média seja diferente de 100 m². O intervalo de confiança contém o valor 100 m², o que apoia esta conclusão.
>
> [Se rejeita] A área média é significativamente diferente de 100 m², sendo aproximadamente [leia] m² — [maior/menor].
>
> Este teste também usa a distribuição **t de Student**. Note que a área tem outliers — alguns imóveis tem áreas minúsculas (erros de digitação?) e outros têm áreas gigantescas (complexos comerciais?). Apesar disso, com n = 1.066, o teorema do limite central nos permite usar o teste t com segurança."

**Tempo:** 20 segundos

---

#### **Segmento 3F: Resumo e Interpretação (04:30–04:45) — Se houver tempo**

**O que mostrar:**
- Caixa de aviso (info) no rodapé: "Limitações..."

**O que dizer:**
> "Resumindo os quatro testes:
> - [Liste as decisões — Rejeitar ou Não rejeitar para cada um]
>
> Limitações importantes:
> - Os intervalos de confiança de proporção usam a aproximação de Wald (normal), que é boa aqui pelas grandes amostras
> - Os testes t pressupõem que os dados são independentes — mas alguns imóveis podem estar no mesmo lote
> - As distribuições de valores monetários são muito assimétricas
> - Ausências foram automaticamente excluídas de cada teste
>
> Apesar desses cuidados, os testes fornecem uma visão sólida sobre como a amostra representa a população."

**Tempo:** 15 segundos

---

### [04:30–05:00] ENCERRAMENTO

**O que mostrar:**
- Volta à tela inicial do Streamlit
- Resumo das três abas

**O que dizer:**
> "Isto conclui a apresentação dos três painéis.
>
> Para resumir:
> - **Painel 1 (População)**: Explora descritivamente todos os 876 mil imóveis
> - **Painel 2 (Amostra)**: Mostra que a amostra de 1.066 é representativa
> - **Painel 3 (Inferência)**: Testa quatro hipóteses sobre a população usando a amostra
>
> Todos os painéis são interativos — você pode mudar variáveis, ajustar sliders e ver os resultados em tempo real. Este é um exemplo de análise estatística aplicada a dados reais de um governo municipal.
>
> Os dados vêm do [IPTU de Porto Alegre](https://dadosabertos.poa.br/dataset/iptu), da prefeitura. O código está em Python, usando Pandas para dados, Plotly para gráficos, e Streamlit para os painéis.
>
> Obrigado por acompanhar. Fim do vídeo."

**Tempo:** 30 segundos

---

## 🎥 DICAS DE GRAVAÇÃO

### Preparação Técnica
- **Software:** OBS Studio (gratuito) ou Camtasia
- **Resolução:** 1920×1080 (Full HD) ou 1440×900 no mínimo
- **Taxa de frames:** 30 fps ou 60 fps
- **Áudio:** Microfone bom, em ambiente silencioso
- **Fundo:** Simples (parede, cortina). Evite barulhos.

### Dicas de Apresentação
1. **Fale claro e devagar** — a audiência precisa entender estatística, não é um jogo
2. **Leia os números exatos** da tela — não aproxime
3. **Pause no gráfico** por 2–3 segundos para deixar a audiência processar
4. **Use o cursor/seta** para apontar elementos importantes
5. **Não mexa rápido** — deixe cada item visível por tempo suficiente
6. **Se errar**, pare, refaça o trecho — edite depois. Não corrija falando.
7. **Evite "uhs", "ahhs"** — fale com segurança
8. **Zoom na tela** se os números ficarem pequenos
9. **Grave a apresentação em etapas** — painel 1, painel 2, painel 3. Edite depois.

### Edição
- **Corte** trechos onde você erra ou hesita
- **Música de fundo** (bem baixa): evite copyrighted. Use biblioteca do YouTube Studio ou Freepik
- **Título e encerramento:** text overlay simples
- **Legendas** (optional mas recomendado) — melhora acessibilidade
- **Comprimento final:** 4–5 minutos (máximo)

### Upload
- **Plataforma:** YouTube (unlisted ou private se preferir, depois mudar para público)
- **Título:** "Análise IPTU Porto Alegre 2026 — Painéis Streamlit"
- **Descrição:** Link para o repositório GitHub + breve resumo
- **Tags:** iptu, porto alegre, estatística, streamlit, python

---

## 📊 TABELA DE REFERÊNCIA RÁPIDA

Use isto enquanto grava para não esquecer o que dizer:

| Painel | Duração | Foco | Ações-Chave |
|--------|---------|------|------------|
| **1: População** | 75 seg | Descritivo de todos os 876k | Mudar variável, ler tabela, descrever gráfico |
| **2: Amostra** | 75 seg | Comparar amostra (1.066) com população | Ler tabela lado a lado, comparar visual, mencionar AAS |
| **3: Inferência** | 105 seg | Testes de hipóteses, valor-p, decisão | Expandir 4 testes, ler estatísticas, interpretar decisão |
| **Encerramento** | 30 seg | Resumo e conclusão | Recapitular, agradecer |

---

## ⚠️ PONTOS-CHAVE PARA NÃO ESQUECER

1. **Population = 876.248 (ou 876.243 após remover 5 duplicatas)**
2. **Sample = 1.066** (AAS sem reposição, semente 42)
3. **Α (nível de significância) = 5% = 0,05**
4. **Valor-p pequeno (<0,05) → Rejeitar H₀**
5. **Valor-p grande (≥0,05) → Não rejeitar H₀**
6. **IC 95% = Intervalo de confiança de 95%**
7. **Testes 1–2 usam Z (proporção)**
8. **Testes 3–4 usam t (média)**

---

## 📝 SCRIPT PRONTOS PARA COPIAR-COLAR

Se preferir ler durante a gravação:

### [Abertura]
"Olá, eu sou [NOME]. Esta é a apresentação de uma análise estatística do IPTU de Porto Alegre para o exercício de 2026. Vou mostrar três painéis interativos que cobrem análise descritiva, comparação amostra-população, e testes de hipóteses."

### [Painel 1 — Início]
"Este é o painel de análise descritiva da população. Contém todos os 876 mil imóveis preparados."

### [Painel 2 — Início]
"Aqui vemos a amostra de 1.066 registros, que representam 0,12% da população. Veja como os valores são muito parecidos com a população."

### [Painel 3 — Início]
"Agora vamos aos testes de hipóteses. Vamos testar quatro afirmações sobre a população usando dados da amostra."

### [Encerramento]
"Isto conclui a apresentação. Os três painéis demonstram análise estatística aplicada em dados reais. Obrigado por acompanhar."

---

## ✅ CHECKLIST PRÉ-GRAVAÇÃO

- [ ] Streamlit rodando corretamente (`streamlit run app.py`)
- [ ] Todos os três painéis carregando sem erros
- [ ] Dados visíveis e números legíveis
- [ ] Microfone testado
- [ ] Sem abas abertas (email, chat, etc.)
- [ ] Modo foco/turbo ligado no SO (sem notificações)
- [ ] Software de gravação aberto e testado
- [ ] Resolução de tela adequada
- [ ] Ter este roteiro à mão para consultar

---

## 🎯 RESUMO FINAL

**O que entregar:**
- Vídeo de 4–5 minutos
- Áudio claro
- Cobertura dos 3 painéis
- Explicação dos 4 testes
- Link público (YouTube)

**Como graças:**
- Siga este roteiro sequencialmente
- Faça takes múltiplas se necessário
- Edite para remover erros
- Publique com legenda descritiva

**Resultado esperado:**
- Avaliador entende o pipeline completo (população → amostra → testes)
- Conclusões sobre cada hipótese são claras
- Código e metodologia refletem rigor estatístico

---

**Preparado para:** Apresentação de Trabalho Final — IA003 (Estatística)  
**Última atualização:** 2026-11-13  
**Status:** Pronto para gravação

Boa sorte! 🎬📊
