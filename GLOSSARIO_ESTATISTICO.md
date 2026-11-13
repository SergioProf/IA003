# 📚 Glossário Estatístico Simples

## Conceitos Explicados Para Leigos

Este documento explica os principais conceitos usados no script de exploração de dados, sem jargão técnico complicado.

---

## 1️⃣ População vs AMOSTRA

### População
**Definição simples:** Todos os itens que você quer estudar.

**No nosso caso:** O arquivo original tem 876.248 registros. Após remover
5 duplicatas exatas, a população analítica usada pelos scripts 02–05 tem
876.243 registros.

**Analogia:** Se você quer saber a altura média dos brasileiros, a "população" seria TODOS os brasileiros.

### Amostra
**Definição simples:** Um grupo pequeno tirado da população para representá-la.

**No nosso caso:** Foram selecionados 1.066 registros da população analítica
(aproximadamente 0,12% de 876.243).

**Analogia:** Em vez de medir TODOS os brasileiros (impossível), você mede 1.000 pessoas bem espalhadas pelo país.

---

## 2️⃣ DADOS QUANTITATIVOS vs QUALITATIVOS

### Quantitativos
**Definição:** Dados que são NÚMEROS (podem ser somados, divididos, comparados).

**Exemplos no nosso caso:**
- Valor do imóvel em R$ (ex: 500.000)
- Área construída em m² (ex: 150)
- Valor do IPTU em R$ (ex: 1.500)

**O que fazemos:** Calculamos MÉDIA, MÁXIMO, MÍNIMO, etc.

### Qualitativos
**Definição:** Dados que são CATEGORIAS/GRUPOS (não são números que você soma).

**Exemplos no nosso caso:**
- Finalidade: Apartamento, Casa, Salão, Garagem
- Uso: Exclusivamente Residencial, Não Exclusivamente Residencial, Agrícola
- Bairro: Centro, Moinhos, Petrópolis, Bom Fim

**O que fazemos:** Contamos QUANTOS em cada categoria (proporção, percentual).

---

## 3️⃣ MEDIDAS ESTATÍSTICAS PRINCIPAIS

### MÉDIA (Valor Típico)
**Definição:** Soma de todos os valores dividido pelo número de valores.

**Fórmula simples:** (Valor 1 + Valor 2 + Valor 3 + ...) ÷ Quantidade

**Exemplo com preços de imóveis:**
```
Imóvel 1: R$ 100.000
Imóvel 2: R$ 200.000
Imóvel 3: R$ 300.000
────────────────────
Soma: R$ 600.000
Quantidade: 3
MÉDIA = 600.000 ÷ 3 = R$ 200.000
```

**Quando usar:** Para saber o valor "típico" ou "representativo".

**Cuidado:** Se há valores MUITO altos ou MUITO baixos (outliers), a média fica deformada.

---

### MEDIANA (Valor do Meio)
**Definição:** O valor que fica no meio quando você ordena todos de menor para maior.

**Exemplo com 5 imóveis:**
```
Ordenados: R$ 100k → R$ 150k → R$ 200k ← MEDIANA ← R$ 250k → R$ 1.000.000
```

**Como calcular com 5 valores:** A mediana é o 3º valor.

**Como calcular com 6 valores:** A mediana é a média entre o 3º e 4º valor.

**Quando usar:** Quando há valores muito altos ou muito baixos. A mediana não é afetada por extremos.

**Comparação com a média:**
- Se Média = R$ 200.000 e Mediana = R$ 150.000 → há imóveis MUITO caros puxando a média para cima
- Se Média = Mediana → os dados estão bem distribuídos

---

### DESVIO-PADRÃO (Quanto Varia)
**Definição:** Número que indica quanto os valores "se espalham" em relação à média.

**Interpretação simples:**
- Desvio-padrão PEQUENO = todos os imóveis custam parecido
- Desvio-padrão GRANDE = há imóveis caros e baratos muito diferentes

**Exemplo:**
```
Grupo A (preços): 100k, 110k, 105k, 95k, 100k
Média: 102k
Desvio-padrão: PEQUENO (tudo bem parecido)

Grupo B (preços): 50k, 100k, 200k, 500k, 1.000k
Média: 350k
Desvio-padrão: GRANDE (muito espalhado)
```

**Regra de ouro:** Cerca de 68% dos valores ficam entre (Média - Desvio-Padrão) e (Média + Desvio-Padrão).

---

### MÍNIMO e MÁXIMO
**Definição:** Os valores mais baixo e mais alto.

**Exemplo:**
```
Mínimo: R$ 10.000 (o imóvel mais barato)
Máximo: R$ 5.000.000 (o imóvel mais caro)
```

**Uso:** Para entender o "alcance" dos dados.

---

### QUARTIS (Q1, Q2, Q3)
**Definição:** Valores que dividem os dados em 4 partes iguais.

**Visualização:**
```
0%         25%        50%        75%        100%
|──────────|──────────|──────────|──────────|
Mínimo     Q1         Q2         Q3         Máximo
(Mediana)
```

**Interpretação:**
- Q1 (25%): 25% dos imóveis custam menos que esse valor
- Q2 (50%): 50% dos imóveis custam menos que esse valor (= MEDIANA)
- Q3 (75%): 75% dos imóveis custam menos que esse valor

**Exemplo com 100 imóveis ordenados por preço:**
```
Posição 0: R$ 50.000 (Mínimo)
Posição 25: R$ 150.000 (Q1)
Posição 50: R$ 250.000 (Q2/Mediana)
Posição 75: R$ 400.000 (Q3)
Posição 100: R$ 1.000.000 (Máximo)
```

---

## 4️⃣ DADOS FALTANTES (AUSÊNCIAS)

### O Que São?
**Definição:** Campos vazios ou em branco no banco de dados.

**Exemplos:**
- Um imóvel sem o valor do aluguel registrado
- Uma pessoa sem data de nascimento
- Um produto sem preço

**No nosso caso:** Alguns imóveis não têm valor registrado, área construída, etc.

### Como Lidamos?
**Opção 1:** Ignorar esses registros (usar só os completos)

**Opção 2:** Tentar "adivinhar" o valor faltante (imputação - mais avançado)

**Regra prática:** Se faltam <5% dos dados, é ok usar. Se faltam >20%, cuidado!

---

## 5️⃣ DUPLICATAS

### O Que São?
**Definição:** O mesmo registro aparecendo duas vezes (ou mais).

**Exemplo:**
```
Linha 1: Rua A, Apto 101, R$ 200.000, 60m²
Linha 2: Rua A, Apto 101, R$ 200.000, 60m² ← DUPLICADA!
```

### Por Que é Problema?
- Contamos o mesmo imóvel duas vezes
- As estatísticas ficam erradas
- A análise fica enviesada

### Solução
Procurar por duplicatas e remover as cópias.

---

## 6️⃣ PROPORÇÃO vs FREQUÊNCIA

### Frequência
**Definição:** Quantas vezes algo aparece.

**Exemplo genérico:**
```
Categoria A: 3
Categoria B: 5
Categoria C: 2
Total: 10
```

### Proporção
**Definição:** Frequência dividida pelo total (virou porcentagem).

**Fórmula:** Proporção = Frequência ÷ Total

**Exemplo genérico:**
```
Categoria A: 3 ÷ 10 = 0,30 = 30%
Categoria B: 5 ÷ 10 = 0,50 = 50%
Categoria C: 2 ÷ 10 = 0,20 = 20%
Total: 100%
```

---

## 7️⃣ TESTES DE HIPÓTESES (Preview)

### O Que É Uma Hipótese?
**Definição:** Uma suposição que você quer verificar se é verdadeira.

**Exemplo:**
- Hipótese 1: "40% dos imóveis são apartamentos"
- Hipótese 2: "O valor médio de um imóvel é R$ 400.000"

### Como Testamos?
**Processo:**
1. Formulamos a hipótese nula (H₀) e a alternativa (H₁)
2. Coletamos dados (de uma amostra)
3. Calculamos uma estatística de teste
4. Comparamos com um valor crítico
5. Decidimos se rejeitamos ou não rejeitamos H₀

**Analogia:** É como um julgamento. A evidência pode levar à rejeição de H₀,
mas não rejeitar H₀ não prova que ela seja verdadeira.

---

## 8️⃣ INTERVALOS DE CONFIANÇA (Preview)

### O Que É?
**Definição:** Um intervalo calculado por um método que, em amostragens
repetidas, contém o parâmetro verdadeiro na proporção de vezes indicada pelo
nível de confiança, sob os pressupostos do método.

**Exemplo:**
```
Amostra de 100 imóveis tem valor médio: R$ 250.000

Intervalo de confiança de 95%: 
Entre R$ 200.000 e R$ 300.000

Interpretação: o método de 95% de confiança produz intervalos que conteriam
o verdadeiro valor médio em cerca de 95% das amostragens repetidas.
```

**Por que não só um número?**
- Quando trabalha com amostra, há incerteza
- Precisamos de um "intervalo de segurança"
- Um intervalo mais amplo pode ter maior cobertura, mas é menos preciso

---

## 9️⃣ NÍVEL DE SIGNIFICÂNCIA (α)

### O Que É?
**Definição:** Limite escolhido para a probabilidade de erro tipo I: rejeitar
H₀ quando H₀ é verdadeira, a longo prazo e sob os pressupostos do teste.

**No nosso caso:** Usaremos α = 0,05 (5%)

**Interpretação:**
- α = 5% é o critério usado para decidir se o resultado é estatisticamente
  significativo; não é a probabilidade de H₀ ser verdadeira ou falsa.

**Nota:** α = 0,05 não significa que há 95% de chance de a conclusão específica estar correta.

---

## 🔟 P-VALOR

### O Que É?
**Definição:** Supondo que H₀ seja verdadeira, é a probabilidade de obter uma
estatística de teste tão extrema quanto a observada, ou mais extrema, segundo
a alternativa considerada.

**Interpretação simples:**
- p-valor < 0,05: você rejeita H₀ (resultado significativo)
- p-valor ≥ 0,05: você não rejeita H₀ (resultado não significativo)

**Exemplo:**
```
Teste de hipótese:
  H₀: "40% dos imóveis são apartamentos"
  Resultado: p-valor = 0,02
  
  Interpretação: se H₀ fosse verdadeira, um resultado tão extremo quanto esse
  teria probabilidade de 2% segundo o teste.
  → Como 0,02 < 0,05, rejeitamos H₀ ao nível de 5%.
```

---

## Resumo Rápido

| Termo | Significado Simples |
|-------|-------------------|
| **Média** | Valor típico (soma ÷ quantidade) |
| **Mediana** | Valor do meio (não afetado por extremos) |
| **Desvio-Padrão** | Quanto os valores variam |
| **Q1/Q3** | 25% e 75% dos valores |
| **Proporção** | Percentual (frequência ÷ total) |
| **Dados Faltantes** | Campos vazios (problema!) |
| **Duplicatas** | Mesmo registro 2x (problema!) |
| **Amostra** | Grupo pequeno que representa o total |
| **Teste de Hipótese** | Verificar se uma suposição é verdadeira |
| **Intervalo de Confiança** | Faixa onde o valor provavelmente está |
| **p-valor** | Probabilidade dos dados (ou de resultado mais extremo) sob H₀ |

---

## Perguntas Frequentes

### P: Por que não analisar todos os 876.243 registros em vez de só 1.066?

**R:** 
- Analisar todos é mais lento (computador gasta mais tempo)
- Uma amostra BEM ESCOLHIDA representa a população
- A amostra reduz o custo de processamento, mas suas estimativas têm incerteza
  amostral; a precisão depende da variável, dos dados válidos e do método.
- Economizamos tempo e recursos

### P: E se minha amostra for "enviesada" (não representar bem)?

**R:**
- Por isso usamos AMOSTRAGEM ALEATÓRIA (seleção ao acaso)
- Cada imóvel tem a mesma chance de ser escolhido
- Isso garante que a amostra representa bem a população

### P: O que significa "95% de confiança"?

**R:**
- Se você repetisse o experimento 100 vezes
- 95 vezes o resultado estaria correto
- 5 vezes (só) o resultado seria errado
- Isso é o padrão em estatística

### P: Como sei se o resultado é importante?

**R:**
- Se p-valor < 0,05, o resultado é "estatisticamente significativo"
- Significa que é improvável ser por acaso
- Mas "significativo" ≠ "importante na prática"

### P: Preciso memorizar essas fórmulas?

**R:**
- NÃO! O computador calcula tudo
- O importante é ENTENDER o que cada número significa
- Assim você vai interpretar os resultados corretamente

---

## Próximos Passos

1. **Leia este documento** enquanto executa o script
2. **Procure pelos nomes** (média, mediana, etc) na saída do script
3. **Compare** com as explicações aqui
4. **Anote dúvidas** para perguntar depois

---

**Preparado em:** 7 de novembro de 2026  
**Para:** Pessoas sem base em estatística  
**Objetivo:** Entender o script de exploração de dados
