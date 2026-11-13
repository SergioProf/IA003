# Roadmap — Trabalho final de Estatística

> **Estado em 12/11/2026:** os scripts 01–05 e os seus artefatos existem no
> repositório, e os scripts 02–05 foram reexecutados após os ajustes recentes.
> Os três painéis, o vídeo de até cinco
> minutos e os links acessíveis exigidos no enunciado continuam pendentes.
> Para o estado detalhado e a ordem de leitura, consulte
> [00_LEIA_PRIMEIRO.md](./00_LEIA_PRIMEIRO.md).

## 1. Objetivo do trabalho

Aplicar amostragem, intervalos de confiança e testes de hipóteses a uma base grande, comparando parâmetros calculados na população com estimativas feitas a partir de uma amostra aleatória simples (AAS). A entrega pede três painéis interativos (população, amostra e inferência/comparação), vídeo de até 5 minutos e links acessíveis.

## 2. Base encontrada e diagnóstico inicial

- **Arquivo:** iptu_2026.csv, cerca de 221 MB.
- **Fonte oficial correspondente:** [IPTU — Dados Abertos de Porto Alegre](https://dadosabertos.poa.br/dataset/iptu). O conjunto descreve o Sistema Integrado de Arrecadação Tributária (SIAT), tem periodicidade anual e licença Creative Commons Attribution.
- **Dimensão:** 876.248 registros e 32 colunas. Todas as linhas observadas são do exercício 2026.
- **Unidade analítica:** cada linha do arquivo; após remover 5 duplicatas exatas, N = 876.243. Consulte o dicionário antes de interpretar cada registro como unidade imobiliária distinta.
- **Tipos:** categóricas (bairro, uso, finalidade, zona, divisão fiscal) e quantitativas (áreas, valores venais, alíquota, IPTU e TCL).
- **Ausências:** bairro (507), uso (24.152), valor venal do imóvel (43), área construída (24.057), entre outros. Informar o N válido por variável e não converter ausência em zero.
- **Assimetria:** valores extremos afetam as médias. No valor venal do imóvel, média preliminar ≈ R$ 387.720 e mediana ≈ R$ 158.073. Mostrar ambas e examinar distribuições antes de eleger a variável inferencial.
- **Candidatas à descrição:** finalidade, uso, unidades por bairro/divisão fiscal, área construída, valor venal, IPTU e TCL. Identificar unidades monetárias (R$) e áreas (m²).

### Fonte confirmada

O arquivo [fonteDosDados.txt](./fonteDosDados.txt), o CSV e o dicionário
correspondem ao IPTU 2026. O conjunto oficial está em
[Dados Abertos de Porto Alegre](https://dadosabertos.poa.br/dataset/iptu).

## 3. Decisões já refletidas no pipeline

- Fonte: IPTU 2026 de Porto Alegre.
- Ferramenta planejada para os painéis: Streamlit + Plotly.
- Hipóteses implementadas no script 05: p = 0,40; p = 0,85; μ = R$ 400.000; μ = 100 m².
- Os testes usam α = 0,05, alternativas bilaterais e casos válidos por variável.
- Prazo indicado no enunciado: 15/11/2026; confirme diretamente com a disciplina se a data ainda for relevante.

## 4. Roteiro de execução

### Etapa A — Fixar escopo, população e variáveis

- Confirmar fonte IPTU e registrar o link da página do conjunto.
- Contextualizar como dados anuais do cadastro/lançamento tributário imobiliário municipal.
- Usar N = 876.243 registros após remover 5 duplicatas exatas da fonte de 876.248 linhas. A interpretação como unidades distintas depende da documentação da fonte.
- Montar tabela de variáveis: nome, descrição oficial, tipo, unidade, ausência e uso na análise.
- Conferir duplicidades e lotes com múltiplas unidades. A área territorial do lote pode repetir entre unidades; não interpretá-la como área exclusiva da unidade sem validação.

### Etapa B — Preparar e auditar os dados

- Preservar o CSV original e criar fluxo reproduzível de limpeza.
- O script 02 lê o arquivo UTF-8 separado por ponto-e-vírgula, normaliza vírgulas decimais e converte as variáveis quantitativas antes da análise.
- Conferir tipos, faixas, vazios, linhas repetidas e consistência entre componentes do valor venal e tributos.
- Definir tratamento das ausências por variável: usar casos válidos e informar o N efetivo; não imputar zero automaticamente.
- Usar leitura eficiente, evitando cópias integrais desnecessárias do arquivo em memória.

### Etapa C — Dimensionar e sortear a AAS

- Parâmetros adotados: confiança de 95%, margem de erro de 3 pontos percentuais e p = 0,50 (opção conservadora para dimensionar proporções).
- Com N = 876.243 e correção para população finita, a conta resulta em **1.066 registros** (z = 1,96; p = 0,50; E = 0,03).
- Sortear sem reposição usando IDs estáveis das linhas e semente fixa. Guardar semente, método, tamanho final e IDs para reprodução.
- Garantir chance igual para cada unidade da população; não filtrar/ordenar antes do sorteio, a menos que a população seja redefinida explicitamente.
- Considerar o efeito das ausências sobre o tamanho válido da amostra e os intervalos/testes.

### Etapa D — Painel 1: população

- Mostrar N total e N válido por variável.
- Exibir frequências e proporções de uso, finalidade, bairro e divisão fiscal; agrupar categorias raras quando necessário e justificar.
- Mostrar média, mediana, desvio-padrão, quartis e distribuições quantitativas.
- Usar histogramas e boxplots para áreas/valores. Se usar escala logarítmica, explicá-la; valores extremos não devem ocultar o padrão.
- Distinguir registros, unidades e bairros; rotular bem moeda e área.

### Etapa E — Painel 2: amostra

- Reproduzir os indicadores e gráficos usando exclusivamente os registros sorteados.
- Informar N total/válido, semente e método de seleção.
- Manter definições, categorias e escalas comparáveis ao Painel 1.
- Interpretar diferenças como variabilidade amostral e/ou efeito de dados faltantes, sem tratá-las automaticamente como erro.

### Etapa F — Painel 3: inferência e comparação

- Fixar o nível de significância antes das conclusões (sugestão: α = 5%).
- Por hipótese, informar estimativa, intervalo de confiança, H₀/H₁, estatística, valor-p e conclusão em contexto.
- Comparar estimativa e intervalo com o parâmetro populacional calculado diretamente na base completa. O valor populacional não entra no cálculo do teste/intervalo.
- Verificar pressupostos, extremos, tamanho válido e independência; várias unidades podem pertencer ao mesmo lote fiscal.

**Quatro hipóteses implementadas no script 05** (o enunciado pede pelo menos duas de proporção e duas de média):

1. **Proporção — finalidade APARTAMENTO:** nenhuma ausência observada no diagnóstico. Exemplo bilateral: H₀: p = 0,40 versus H₁: p ≠ 0,40.
2. **Proporção — uso exclusivamente residencial:** há 24.152 ausências no campo uso; definir previamente a população válida e usar o denominador de respostas válidas. Exemplo bilateral: H₀: p = 0,85 versus H₁: p ≠ 0,85.
3. **Média — valor venal do imóvel (R$):** casos válidos. Exemplo bilateral: H₀: μ = R$ 400.000 versus H₁: μ ≠ R$ 400.000.
4. **Média — área construída total (m²):** casos válidos. Exemplo bilateral: H₀: μ = 100 m² versus H₁: μ ≠ 100 m².

Os valores de referência foram adotados no código, mas precisam de justificativa substantiva na apresentação. A média do valor venal é bastante assimétrica e a área construída tem ausências; relatar os casos válidos e limitações. Uma amostra grande ajuda a aproximação, mas não elimina o efeito de extremos nem problemas de dependência.

### Etapa G — Construir e publicar painéis

- Ferramenta escolhida: **Streamlit + Plotly**, usando gráficos Plotly quando forem úteis para interação.
- Implementar os três painéis como seções/páginas no Streamlit, com títulos, unidades, fonte, filtros e notas metodológicas.
- Reutilizar definições e codificação visual para facilitar comparação.
- Verificar legibilidade, interações e acesso sem solicitação de autorização.
- Publicar e guardar os links finais.

### Etapa H — Vídeo e entrega

- **Prazo informado:** 15/11/2026 (domingo; confirmar se a referência era sábado, 14/11/2026).
- Os painéis ainda não estão no repositório; concluir e validar antes de gravar.
- Roteiro de até 5 minutos: contexto/fonte (≈40 s), população/AAS (≈60 s), painéis descritivos (≈60 s), inferência/comparação (≈100 s), limitações/conclusão (≈40 s).
- Explicar interpretação: diferença entre estimativa e parâmetro, o que o intervalo permite concluir e como a variabilidade amostral limita a leitura.
- Gravar, revisar duração/áudio/legibilidade e publicar no YouTube com acesso adequado à disciplina.
- Checklist: 3 links de painéis, vídeo, base/fonte, população/unidade, dimensionamento e método da AAS, hipóteses e testes de médias/proporções conforme o enunciado, pressupostos e limitações.

## 5. Próximas etapas

1. Construir e validar os três painéis interativos exigidos no enunciado.
2. Gravar e publicar o vídeo com até cinco minutos.
3. Disponibilizar e testar os links de entrega.
4. Justificar os valores de referência das hipóteses e relatar pressupostos, casos válidos e limitações.

## 6. Referências

- [Conjunto IPTU — Dados Abertos de Porto Alegre](https://dadosabertos.poa.br/dataset/iptu)
- [Recurso IPTU 2026](https://dadosabertos.poa.br/dataset/iptu/resource/1129ea5b-bf51-4102-a115-756343e86d27)
- [Dicionário oficial IPTU](https://dadosabertos.poa.br/dataset/26246f17-3c52-4cf2-ac33-4ac97b4d1d47/resource/8b0fa7d8-4e0b-4e5e-9c00-bcfb5724fe5b/download/dicionario-de-dados.pdf)
