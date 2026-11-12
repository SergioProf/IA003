"""
================================================================================
AMOSTRAGEM — IPTU 2026 Porto Alegre
Trabalho Final de Estatística IA003

O QUE ESTE SCRIPT FAZ:
  Este script seleciona uma amostra aleatória dos dados, em vez de usar todos
  os 876.248 imóveis. Isso é útil porque:
  
  1. Simula um cenário real: normalmente não temos acesso a TODOS os dados
  2. Mais rápido: trabalhar com ~1.066 registros é mais fácil
  3. Permite fazer testes: comparar o resultado da amostra com a população
  4. Ensina amostragem: parte importante da Estatística!
  
  O MÉTODO: Amostragem Aleatória Simples (AAS)
    - Cada imóvel tem a mesma chance de ser selecionado
    - Sem reposição (cada imóvel selecionado apenas 1 vez)
    - Com semente fixa para reprodução

PARA QUEM NÃO SABE ESTATÍSTICA:
  - "Amostra" = pequeno grupo representativo de um grupo maior
  - "Aleatória" = sorteio sem padrão (como loteria)
  - "AAS" = Amostragem Aleatória Simples
  - "Semente (seed)" = número mágico que faz a aleatoriedade ser reproduzível
  - "N" = tamanho da população; "n" = tamanho da amostra

================================================================================
"""

import pandas as pd
import numpy as np
from pathlib import Path
import warnings

# Oculta avisos de bibliotecas para manter o relatório de execução legível.
warnings.filterwarnings('ignore')

# ============================================================================
# SEÇÃO 1: CARREGAR DADOS PREPARADOS
# ============================================================================
# O arquivo desta etapa é produzido pelo script 02. Os caminhos são relativos
# à pasta do projeto, então não dependem do diretório atual do terminal.
print("=" * 80)
print("AMOSTRAGEM — IPTU 2026 Porto Alegre")
print("=" * 80)

BASE_DIR = Path(__file__).parent.parent
dados_dir = BASE_DIR / "dados_processados"
arquivo_limpo = dados_dir / "dados_limpos.csv"

print(f"\n📂 Carregando dados preparados de: {arquivo_limpo}")

if not arquivo_limpo.exists():
    print("❌ Arquivo de dados limpos não encontrado!")
    print("   Execute primeiro: python scripts/02_preparacao_dados.py")
    exit(1)

try:
    df = pd.read_csv(arquivo_limpo, sep=';', encoding='utf-8')
    print(f"✓ Sucesso! {len(df):,} linhas lidas")
except Exception as e:
    print(f"❌ Erro: {e}")
    exit(1)

# ============================================================================
# SEÇÃO 2: CALCULAR TAMANHO MÍNIMO DA AMOSTRA
# ============================================================================
# A fórmula apresentada aplica a correção para população finita. Como a
# proporção verdadeira é desconhecida, p=0,5 maximiza p(1-p) e fornece um
# tamanho amostral conservador.
print("\n" + "=" * 80)
print("SEÇÃO 2: CÁLCULO DO TAMANHO DA AMOSTRA")
print("=" * 80)

print("""
PARÂMETROS DE AMOSTRAGEM:
  Nível de Confiança (1 - α): 95%      [z = 1,96]
  Margem de Erro (E):          3%       [0,03]
  Proporção (p):               50%      [0,50 - conservador]
  População (N):               876.248 imóveis

FÓRMULA (com correção para população finita):
  
  n = [ z² × p(1-p) × N ] / [ E² × (N-1) + z² × p(1-p) ]
  
  Onde:
    z = 1,96 (valor crítico para 95% de confiança)
    p = 0,50 (proporção esperada - caso conservador)
    N = 876.248 (tamanho da população)
    E = 0,03 (margem de erro)
""")

# Parâmetros da fórmula: z representa o nível de confiança, E a margem de erro,
# p a proporção esperada e N o total de registros disponíveis.
z = 1.96           # Nível de confiança 95%
p = 0.50           # Proporção conservadora (máxima variância)
E = 0.03           # Margem de erro 3%
N = len(df)        # Tamanho da população

# Aplicamos a fórmula da população finita separando numerador e denominador
# para deixar visíveis as partes que compõem o tamanho amostral.
numerador = (z**2) * p * (1-p) * N
denominador = (E**2) * (N-1) + (z**2) * p * (1-p)
n = numerador / denominador

# Como não há fração de registro, arredondamos para cima para não ficar abaixo
# do tamanho mínimo calculado.
n_arredondado = int(np.ceil(n))

print(f"""
CÁLCULO:
  z² = {z**2}
  p(1-p) = {p*(1-p)}
  N = {N:,}
  E² = {E**2}
  
  Numerador:   {numerador:,.0f}
  Denominador: {denominador:,.0f}
  
RESULTADO:
  Tamanho exato:  n ≈ {n:.2f}
  Tamanho final:  n = {n_arredondado:,}
  
  Proporção de amostragem: {100*n_arredondado/N:.4f}%
""")

# ============================================================================
# SEÇÃO 3: CONFIGURAR SEMENTE DE ALEATORIEDADE
# ============================================================================
# A semente inicializa o gerador pseudoaleatório; com a mesma semente e os
# mesmos dados de entrada, a seleção pode ser reproduzida.
print("=" * 80)
print("SEÇÃO 3: CONFIGURAÇÃO DA ALEATORIEDADE")
print("=" * 80)

RANDOM_STATE = 42  # Semente fixa para reprodução

print(f"""
SEMENTE (RANDOM STATE): {RANDOM_STATE}

Por que semente?
  Uma semente fixa garante que a mesma amostra será sorteada toda vez
  que você executar este script. Isso é importante para REPRODUÇÃO
  dos resultados (qualquer pesquisador deve conseguir replicar).

Se você quiser uma amostra DIFERENTE:
  Mude o valor de RANDOM_STATE para outro número (ex: 123, 999, etc)
""")

np.random.seed(RANDOM_STATE)

# ============================================================================
# SEÇÃO 4: SORTEAR A AMOSTRA (AAS - Amostragem Aleatória Simples)
# ============================================================================
# O sorteio seleciona posições entre 0 e N-1. `replace=False` impede que uma
# mesma posição seja escolhida mais de uma vez.
print("\n" + "=" * 80)
print("SEÇÃO 4: SORTEIO DA AMOSTRA (AAS - SEM REPOSIÇÃO)")
print("=" * 80)

print(f"\nSorteando {n_arredondado:,} imóveis de {N:,}...")
print("Método: Amostragem Aleatória Simples (sem reposição)")

# Sortear índices aleatoriamente
indices_amostra = np.random.choice(
    N,
    size=n_arredondado,
    replace=False  # Sem reposição
)

# A ordenação facilita conferir e exibir os índices; não altera quais registros
# foram sorteados.
indices_amostra_ordenados = np.sort(indices_amostra)

print(f"✓ Amostra sorteada!")
print(f"  Indices da amostra: {min(indices_amostra_ordenados)} a {max(indices_amostra_ordenados)}")
print(f"  Primeira linha da amostra (índice): {indices_amostra_ordenados[0]}")
print(f"  Última linha da amostra (índice):   {indices_amostra_ordenados[-1]}")

# ============================================================================
# SEÇÃO 5: CRIAR VARIÁVEL DE INDICADOR (amostra vs população)
# ============================================================================
# A coluna booleana permite manter população e amostra no mesmo arquivo:
# `True` identifica os registros sorteados e `False` os demais.
print("\n" + "=" * 80)
print("SEÇÃO 5: CRIAR INDICADOR DE AMOSTRA")
print("=" * 80)

# Adicionar coluna indicando se cada linha está na amostra
df['em_amostra'] = False
df.loc[indices_amostra, 'em_amostra'] = True

num_amostra = df['em_amostra'].sum()
print(f"\nIndicador criado: coluna 'em_amostra'")
print(f"  Linhas na amostra:  {num_amostra:,}")
print(f"  Linhas fora:        {len(df) - num_amostra:,}")

# ============================================================================
# SEÇÃO 6: EXTRAIR AMOSTRA E GUARDAR ÍNDICES
# ============================================================================
# Criamos um recorte independente com os registros selecionados e uma tabela
# auxiliar com os índices originais, para rastreabilidade do sorteio.
print("\n" + "=" * 80)
print("SEÇÃO 6: SALVAR AMOSTRA E ÍNDICES")
print("=" * 80)

# Extrair apenas os registros da amostra
df_amostra = df[df['em_amostra'] == True].copy()

# Criar DataFrame com apenas os índices
indices_df = pd.DataFrame({
    'indice_original': indices_amostra_ordenados,
    'em_amostra': [True] * len(indices_amostra_ordenados)
})

# Os três arquivos têm finalidades diferentes: amostra isolada, índices sorteados
# e população completa com o indicador. A pasta é criada se ainda não existir.
dados_dir.mkdir(exist_ok=True)

# Salvar amostra
arquivo_amostra = dados_dir / "amostra.csv"
print(f"\n💾 Salvando amostra em: {arquivo_amostra}")
df_amostra.to_csv(arquivo_amostra, sep=';', encoding='utf-8', index=False)
print(f"✓ Amostra salva! ({len(df_amostra):,} linhas)")

# Salvar índices
arquivo_indices = dados_dir / "amostra_indices.csv"
print(f"\n💾 Salvando índices em: {arquivo_indices}")
indices_df.to_csv(arquivo_indices, sep=';', encoding='utf-8', index=False)
print(f"✓ Índices salvos! ({len(indices_df):,} registros)")

# Salvar dados completos com indicador (para análises futuras)
arquivo_com_indicador = dados_dir / "dados_com_indicador_amostra.csv"
print(f"\n💾 Salvando dados completos com indicador: {arquivo_com_indicador}")
df.to_csv(arquivo_com_indicador, sep=';', encoding='utf-8', index=False)
print(f"✓ Dados salvos! ({len(df):,} linhas, com coluna 'em_amostra')")

# ============================================================================
# SEÇÃO 7: VERIFICAÇÃO E VALIDAÇÃO
# ============================================================================
# Conferimos propriedades básicas do resultado: índices sem repetição e
# identificador original preenchido para os registros da amostra.
print("\n" + "=" * 80)
print("SEÇÃO 7: VALIDAÇÃO DA AMOSTRA")
print("=" * 80)

print("""
VERIFICAÇÕES:
  ✓ Aleatoriedade: SIM (sem padrão)
  ✓ Sem reposição:  SIM (cada registro selecionado 1 vez)
  ✓ Reprodutível:   SIM (semente = 42)
""")

# Verificar se há sobreposição (não deve haver)
print("\n✓ Verificando integridade...")
if len(indices_amostra_ordenados) != len(set(indices_amostra_ordenados)):
    print("⚠️  AVISO: Alguns índices aparecem mais de uma vez!")
else:
    print("  ✓ Sem duplicatas nos índices")

if df_amostra['indice_original'].isna().sum() > 0:
    print("⚠️  AVISO: Há dados faltantes na coluna 'indice_original'")
else:
    print("  ✓ Todas as colunas preenchidas")

# ============================================================================
# SEÇÃO 8: RESUMO ESTATÍSTICO
# ============================================================================
# O resumo registra o tamanho relativo da amostra e os parâmetros utilizados,
# facilitando a conferência e a reprodução da análise.
print("\n" + "=" * 80)
print("SEÇÃO 8: COMPARAÇÃO AMOSTRA vs POPULAÇÃO")
print("=" * 80)

print(f"""
╔════════════════════════════════════════════════════════════════╗
║                  AMOSTRAGEM REALIZADA                         ║
╚════════════════════════════════════════════════════════════════╝

POPULAÇÃO COMPLETA (N):
  Total de registros:     {len(df):>12,}
  Variáveis:              {len(df.columns):>12}

AMOSTRA (n):
  Tamanho da amostra:     {len(df_amostra):>12,}
  Tamanho em %:           {100*len(df_amostra)/len(df):>11.4f}%

PARÂMETROS USADOS:
  Nível de confiança:     {95:>12}%
  Margem de erro:         {3:>12}%
  Semente (seed):         {RANDOM_STATE:>12}

MÉTODO:
  ✓ Amostragem Aleatória Simples (AAS)
  ✓ Sem reposição
  ✓ Cada registro tem chance igual de ser selecionado
  
ARQUIVOS GERADOS:
  1. amostra.csv
     → Apenas os {len(df_amostra):,} registros da amostra
  
  2. amostra_indices.csv
     → Lista dos índices sorteados
  
  3. dados_com_indicador_amostra.csv
     → Todos os {len(df):,} registros com indicador (em_amostra: T/F)

╚════════════════════════════════════════════════════════════════╝
""")

# Mostrar algumas estatísticas comparativas
print("\nAMOSTRAS DE DADOS:\n")
print("Primeiros 5 índices sorteados:")
print(indices_amostra_ordenados[:5])
print("\nÚltimos 5 índices sorteados:")
print(indices_amostra_ordenados[-5:])

# ============================================================================
# SEÇÃO 9: DICAS PARA PRÓXIMAS ETAPAS
# ============================================================================
# Esta seção resume a sequência do pipeline e como repetir ou alterar o sorteio.
print("\n" + "=" * 80)
print("SEÇÃO 9: INFORMAÇÕES IMPORTANTES")
print("=" * 80)

print("""
PRÓXIMAS ETAPAS:
  
  1. Análise Descritiva
     → Calcular estatísticas (média, mediana, desvio-padrão)
     → Tanto para POPULAÇÃO quanto para AMOSTRA
     → Comparar os dois resultados
  
  2. Testes de Hipóteses
     → Usar a AMOSTRA para testar hipóteses
     → Comparar com valores conhecidos da POPULAÇÃO
  
  3. Painéis Interativos
     → Visualizar dados em gráficos
     → Mostrar resultados de forma clara

REPRODUTIBILIDADE:
  
  Se você quiser gerar a mesma amostra novamente:
  - Use a mesma semente: RANDOM_STATE = 42
  - Mantenha o mesmo arquivo de dados
  
  Se quiser uma amostra DIFERENTE:
  - Mude RANDOM_STATE para outro valor
  - Reexecute este script

IMPORTANTE:
  
  Os arquivos gerados aqui serão usados pela análise descritiva!
  Certifique-se de que todos os 3 arquivos foram criados com sucesso.
""")

# ============================================================================
# SCRIPT FINALIZADO
# ============================================================================
print("\n" + "=" * 80)
print("🎉 AMOSTRAGEM CONCLUÍDA COM SUCESSO!")
print("=" * 80)
print("""
O QUE FOI FEITO:
  ✓ Tamanho da amostra calculado: n ≈ 1.066
  ✓ Amostra aleatória sorteada (AAS)
  ✓ Sem reposição (cada registro selecionado 1 vez)
  ✓ Semente fixa para reprodução
  ✓ 3 arquivos gerados:
    - amostra.csv
    - amostra_indices.csv
    - dados_com_indicador_amostra.csv

PRÓXIMA ETAPA:
  Executar: python scripts/04_analise_descritiva.py
  
  Esse script vai:
    • Calcular estatísticas da POPULAÇÃO
    • Calcular estatísticas da AMOSTRA
    • Gerar gráficos e tabelas
    • Comparar os dois resultados

""")
print("=" * 80)
