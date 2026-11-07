# Análise Inicial — Trabalho Final de Estatística

**Data:** 7 de novembro de 2026  
**Disciplina:** IA003 — Estatística  
**Tarefa:** Aplicar amostragem, intervalos de confiança e testes de hipóteses

---

## 1. Visão Geral da Tarefa

### Objetivo Principal
Aplicar conceitos de amostragem, estimação por intervalos de confiança e testes de hipóteses em uma base de dados grande, comparando parâmetros da população com estimativas de uma amostra aleatória simples (AAS).

### Entregáveis Exigidos
1. **Painel 1:** Análise descritiva da população
2. **Painel 2:** Análise descritiva da amostra
3. **Painel 3:** Inferência estatística e comparação dos resultados
4. **Vídeo:** Apresentação (máx. 5 minutos) no YouTube
5. **Links:** Painéis, vídeo e base de dados

### Critérios de Avaliação (Pesos)
- Escolha e contextualização da base: 10%
- Dimensionamento e seleção da amostra: 10%
- Qualidade do painel da população: 10%
- Qualidade do painel da amostra: 10%
- Correção dos intervalos e testes: 20%
- Interpretação e comparação população/amostra: 20%
- Clareza e qualidade do vídeo: 20%

**Prazo:** 15 de novembro de 2026 (confirmado: domingo)

---

## 2. Base de Dados Selecionada

### Identificação
- **Nome:** IPTU 2026 — Porto Alegre
- **Fonte Oficial:** [Dados Abertos de Porto Alegre](https://dadosabertos.poa.br/dataset/iptu)
- **Descrição:** Sistema Integrado de Arrecadação Tributária (SIAT) — dados anuais do cadastro/lançamento tributário imobiliário municipal
- **Licença:** Creative Commons Attribution
- **Periodicidade:** Anual

### Características do Dataset
| Aspecto | Valor |
|---------|-------|
| **Tamanho do arquivo** | 210.53 MB |
| **Total de linhas** | 876.249 (1 linha cabeçalho + 876.248 registros) |
| **Número de colunas** | 32 |
| **Período** | Exercício 2026 |
| **Unidade de análise** | Registro de unidade imobiliária/cadastro IPTU |

### Variáveis Disponíveis

#### Variáveis Qualitativas (Categóricas)
- **Finalidade:** Tipo de finalidade do imóvel (ex: apartamento, casa, etc.)
- **Uso:** Classificação de uso (ex: residencial, comercial, etc.)
- **Bairro:** Localização do imóvel na cidade
- **Zona:** Zoneamento municipal
- **Divisão Fiscal:** Divisão administrativa/fiscal

#### Variáveis Quantitativas
- **Área Territorial do Lote (m²):** Dimensão do terreno
- **Área Construída (m²):** Dimensão total construída
- **Valor Venal do Imóvel (R$):** Valor de mercado estimado
- **Alíquota (%):** Percentual de tributação
- **IPTU (R$):** Imposto sobre Propriedade Predial e Territorial Urbana
- **TCL (R$):** Taxa de Contribuição de Melhoria (se aplicável)

### Dados Faltantes (Ausências)
| Variável | Registros sem valor | Observação |
|----------|-------------------|-----------|
| Bairro | 507 | Mínimo |
| Uso | 24.152 | Significativo |
| Valor Venal do Imóvel | 43 | Mínimo |
| Área Construída | 24.057 | Significativo |

**Tratamento:** Utilizar casos válidos e informar o N efetivo por variável; não converter ausências em zero.

### Distribuições Observadas
- **Valor Venal:** Altamente assimétrica
  - Média preliminar: ~R$ 387.720
  - Mediana: ~R$ 158.073
  - Presença de valores extremos
- **Área Construída:** Distribuição com outliers
- **Categorias:** Algumas categorias raras podem necessitar agrupamento

---

## 3. População e Unidade Amostral

### Definição da População
- **População (N):** Todos os registros de unidade imobiliária do exercício 2026 no dataset IPTU
- **Tamanho:** N = 876.248 unidades imobiliárias
- **Unidade Amostral:** Registro individual de cadastro IPTU

### Contexto
Os dados representam o universo de unidades imobiliárias sujeitas ao IPTU em Porto Alegre em 2026, cobrindo residências, comercial, industrial e outros usos.

---

## 4. Plano de Amostragem

### Dimensionamento da Amostra Aleatória Simples (AAS)

#### Parâmetros Iniciais
- **Nível de Confiança:** 95% (z = 1,96)
- **Margem de Erro:** 3 pontos percentuais (E = 0,03)
- **Proporção:** p = 0,50 (opção conservadora)
- **População Finita:** N = 876.248 (aplicar correção para população finita)

#### Cálculo do Tamanho Amostral
Fórmula com correção para população finita:

```
n = (z² × p × (1-p)) / E²  ÷  (1 + (z² × p × (1-p)) / (E² × N))
```

**Resultado esperado:** Aproximadamente **1.066 registros**

### Procedimento de Seleção
- Usar seleção aleatória sem reposição
- Semente fixa para reprodutibilidade
- IDs estáveis das linhas
- Documentar: semente, método, tamanho final, IDs selecionados

### Garantias
- Cada unidade da população tem probabilidade igual de seleção
- Sem filtros ou ordenações prévias
- Independência respeitada (nota: múltiplas unidades podem pertencer ao mesmo lote)

---

## 5. Hipóteses para Análise Inferencial

### Hipótese 1: Proporção — Finalidade "Apartamento"
- **Variável:** Finalidade
- **Evento:** Imóvel com finalidade "Apartamento"
- **H₀:** p = 0,40 (40% de apartamentos)
- **H₁:** p ≠ 0,40 (bilateral)
- **Justificativa:** Validar proporção de apartamentos em Porto Alegre

### Hipótese 2: Proporção — Uso Residencial
- **Variável:** Uso
- **Evento:** Imóvel com uso exclusivamente residencial
- **Nota:** 24.152 ausências; usar denominador de respostas válidas
- **H₀:** p = 0,85 (85% de usos residenciais)
- **H₁:** p ≠ 0,85 (bilateral)
- **Justificativa:** Verificar proporção de imóveis residenciais

### Hipótese 3: Média — Valor Venal do Imóvel
- **Variável:** Valor Venal (R$)
- **N válido:** 876.205 (após exclusão de 43 ausências)
- **H₀:** μ = R$ 400.000
- **H₁:** μ ≠ R$ 400.000 (bilateral)
- **Observações:**
  - Distribuição altamente assimétrica
  - Presença de valores extremos
  - Média vs. mediana muito diferentes
  - Amostra grande ajuda com aproximação normal

### Hipótese 4: Média — Área Construída
- **Variável:** Área Construída (m²)
- **N válido:** 852.191 (após exclusão de 24.057 ausências)
- **H₀:** μ = 100 m²
- **H₁:** μ ≠ 100 m² (bilateral)
- **Observações:**
  - Dados com outliers
  - Significativa proporção de ausências
  - Verificar distribuição antes de testes

### Nível de Significância
- **α = 0,05 (5%)** — Fixado antes das conclusões

---

## 6. Estrutura de Trabalho Proposta

### Etapa A: Exploração e Validação dos Dados
- [ ] Ler e auditar o CSV (separador, codificação, tipos)
- [ ] Validar dicionário de dados vs. conteúdo real
- [ ] Identificar duplicatas e inconsistências
- [ ] Documentar ausências e validações

### Etapa B: Preparação dos Dados
- [ ] Criar script reproduzível de limpeza (sem modificar original)
- [ ] Validar decimais (vírgula vs. ponto)
- [ ] Definir tratamento de ausências por variável
- [ ] Gerar dataset processado para análises

### Etapa C: Amostragem
- [ ] Calcular tamanho da amostra (confirmar com calculadora USP/Bauru)
- [ ] Implementar seleção aleatória simples
- [ ] Documentar semente e procedimento
- [ ] Salvar índices/IDs para reprodução

### Etapa D: Análise Descritiva — População
- [ ] Calcular estatísticas descritivas por variável
- [ ] Gerar gráficos exploratórios
- [ ] Examinar distribuições (histogramas, boxplots)
- [ ] Preparar painel interativo (Painel 1)

### Etapa E: Análise Descritiva — Amostra
- [ ] Reproduzir estatísticas com dados amostrais
- [ ] Gerar gráficos equivalentes aos da população
- [ ] Documentar método de seleção
- [ ] Preparar painel interativo (Painel 2)

### Etapa F: Análise Inferencial
- [ ] Calcular intervalos de confiança para proporções
- [ ] Calcular intervalos de confiança para médias
- [ ] Realizar testes de hipóteses (proporções)
- [ ] Realizar testes de hipóteses (médias)
- [ ] Verificar pressupostos e documentar limitações
- [ ] Comparar estimativas com parâmetros populacionais

### Etapa G: Painel 3 — Inferência e Comparação
- [ ] Apresentar resultados dos 4 testes
- [ ] Exibir intervalos de confiança graficamente
- [ ] Comparar estimativas amostrais vs. parâmetros populacionais
- [ ] Interpretar diferenças e variabilidade amostral

### Etapa H: Painéis Interativos
- [ ] Escolher ferramenta (Streamlit + Plotly recomendado)
- [ ] Implementar os 3 painéis
- [ ] Garantir legibilidade e interatividade
- [ ] Publicar e guardar links

### Etapa I: Vídeo e Entrega
- [ ] Planejar roteiro (máx. 5 minutos)
- [ ] Gravar apresentação
- [ ] Publicar no YouTube
- [ ] Compilar links finais

---

## 7. Ferramentas Recomendadas

### Análise e Preparação de Dados
- **Python 3.9+** com bibliotecas:
  - `pandas`: leitura e manipulação de dados
  - `numpy`: operações numéricas
  - `scipy.stats`: testes estatísticos
  - `scikit-learn`: amostragem

### Visualização
- **Plotly:** Gráficos interativos
- **Matplotlib/Seaborn:** Gráficos estáticos complementares

### Painéis Interativos
- **Streamlit:** Framework leve para dashboards
- (Alternativas: Power BI, Looker Studio, Tableau — a critério)

### Vídeo
- Software de gravação de tela: OBS Studio, Camtasia, etc.
- Edição: DaVinci Resolve (gratuito) ou similar
- Plataforma: YouTube

---

## 8. Próximas Ações

### Imediatas
1. ✅ Analisar e documentar tarefa (este documento)
2. ⬜ Confirmar ferramenta para painéis (Streamlit?)
3. ⬜ Validar base de dados (ler amostra, conferir dicionário)
4. ⬜ Iniciar script de exploração Python

### Curto Prazo (próximos dias)
- Exploração completa dos dados
- Cálculo do tamanho amostral
- Seleção da amostra
- Primeiras análises descritivas

### Médio Prazo
- Análise inferencial (testes e intervalos)
- Construção dos painéis
- Documentação de metodologia

### Longo Prazo
- Gravação do vídeo
- Publicação dos painéis
- Entrega final (15/11/2026)

---

## 9. Notas Importantes

- **Correção do fonteDosDados.txt:** Atualmente lista "ITBI" mas deve ser "IPTU"
- **Independência:** Múltiplas unidades podem pertencer ao mesmo lote; documentar se houver implicações estatísticas
- **Tamanho grande:** Com N ≈ 876.248, a amostra n ≈ 1.066 é pequena; variabilidade amostral será notável
- **Extremos:** Valor venal e área construída têm distribuições assimétricas; examinar antes de escolher teste (t-test requer normalidade ou n grande)
- **Prazos apertados:** Etapas D, E, F, G devem rodar em paralelo ao máximo

---

**Preparado em:** 7 de novembro de 2026
