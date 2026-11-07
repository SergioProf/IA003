"""
================================================================================
EXPLORAÇÃO DE DADOS — IPTU 2026 Porto Alegre
Trabalho Final de Estatística IA003

O QUE ESTE SCRIPT FAZ:
  Este script examina e valida um grande conjunto de dados sobre imóveis em 
  Porto Alegre. Pense nisso como uma "radiografia" dos dados para garantir que 
  estão corretos antes de começar análises mais importantes.

  O script:
  1. Carrega um arquivo CSV (tipo de banco de dados em texto)
  2. Verifica se os dados estão corretos e completos
  3. Calcula números importantes (média, máximo, mínimo, etc)
  4. Procura por erros ou inconsistências
  5. Salva um resumo dos resultados

PARA QUEM NÃO SABE ESTATÍSTICA:
  - Não se assuste com os nomes "técnicos" — tudo será explicado!
  - Você verá números como "média" (valor típico) e "desvio-padrão" 
    (quanto varia em relação à média)
  - Dados "faltantes" = campos em branco (ex: imóvel sem valor de aluguel)

================================================================================
"""

# Importar as bibliotecas (ferramentas) que o script precisa
import pandas as pd         # Biblioteca para trabalhar com tabelas de dados
import numpy as np          # Biblioteca para cálculos matemáticos
from pathlib import Path    # Biblioteca para trabalhar com caminhos de arquivos
import warnings             # Para ignorar avisos menos importantes

# Ignorar avisos que não são essenciais (deixa a tela mais limpa)
warnings.filterwarnings('ignore')

# ============================================================================
# SEÇÃO 1: DEFINIR O CAMINHO DO ARQUIVO
# ============================================================================
# Explicação: O computador precisa saber ONDE está o arquivo que queremos ler.
# BASE_DIR = pasta raiz (acima da pasta "scripts")
# DATA_FILE = caminho completo para o arquivo iptu_2026.csv

BASE_DIR = Path(__file__).parent.parent  # Volta um nível acima (sai de scripts/)
DATA_FILE = BASE_DIR / "iptu_2026.csv"   # Arquivo na pasta raiz

# Mostrar um título bonito
print("=" * 80)
print("EXPLORAÇÃO INICIAL — IPTU 2026 Porto Alegre")
print("=" * 80)
print(f"\nArquivo: {DATA_FILE}")
print(f"Existe: {DATA_FILE.exists()}")  # True = arquivo encontrado, False = erro

# Se o arquivo não existir, parar o script e mostrar erro
if not DATA_FILE.exists():
    print("❌ Arquivo não encontrado. Verifique o caminho.")
    exit(1)  # Sair do programa com erro

# ============================================================================
# SEÇÃO 2: CARREGAR O ARQUIVO DE DADOS
# ============================================================================
# Explicação: Um CSV é um arquivo de texto que parece uma tabela. Cada linha 
# é um imóvel, cada coluna é uma informação (preço, área, bairro, etc).
#
# Configurações importantes:
#   - sep=';' = o arquivo usa ponto-e-vírgula como separador entre colunas
#   - encoding='utf-8' = o arquivo usa codificação UTF-8 (suporta acentos)
#   - low_memory=False = ler tudo de uma vez (mais rápido para arquivos grandes)
#   - on_bad_lines='skip' = se encontrar linha com erro, pular e continuar

print("\n" + "=" * 80)
print("SEÇÃO 2: CARREGANDO O ARQUIVO DE DADOS")
print("=" * 80)

try:
    # Usar a biblioteca pandas para ler o arquivo CSV
    df = pd.read_csv(
        DATA_FILE,
        sep=';',              # Separador: ponto-e-vírgula
        encoding='utf-8',     # Codificação: suporta acentos
        low_memory=False,     # Ler tudo de uma vez
        on_bad_lines='skip'   # Pular linhas com erro
    )
    # "df" é uma tabela (DataFrame) com todos os dados carregados
    print(f"✓ Sucesso! Lido: {len(df):,} linhas (imóveis) e {len(df.columns)} colunas (informações)")
except Exception as e:
    # Se der erro, mostrar mensagem e parar
    print(f"❌ Erro ao ler: {e}")
    exit(1)

# ============================================================================
# SEÇÃO 3: VALIDAÇÃO BÁSICA DOS DADOS
# ============================================================================
# Explicação: Queremos entender a "forma" dos dados:
#   - Quantas linhas? (quantos imóveis temos)
#   - Quantas colunas? (quantas informações cada imóvel tem)
#   - Quanto espaço ocupam na memória? (importante para arquivos grandes)
#   - Que tipos de dados temos? (números, texto, datas, etc)

print("\n" + "=" * 80)
print("SEÇÃO 3: VALIDAÇÃO BÁSICA DOS DADOS")
print("=" * 80)

# df.shape retorna (número de linhas, número de colunas)
# Exemplo: (876248, 32) significa 876.248 linhas e 32 colunas
print(f"\nTamanho dos dados (linhas, colunas): {df.shape}")

# Calcular quanto espaço o arquivo ocupa na memória do computador
memoria_mb = df.memory_usage(deep=True).sum() / 1e6
print(f"Memória usada: {memoria_mb:.2f} MB")

# Mostrar o nome de cada coluna (cada informação que temos sobre os imóveis)
print("\nNomes das 32 colunas (informações sobre cada imóvel):")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2d}. {col}")

# Mostrar o tipo de dados de cada coluna
# - int64 = número inteiro (ex: número de quartos)
# - float64 = número decimal (ex: valor em reais)
# - object = texto (ex: bairro, endereco)
# - bool = verdadeiro/falso
print("\nTipo de dados de cada coluna:")
print(df.dtypes)

# ============================================================================
# SEÇÃO 4: VER AS PRIMEIRAS LINHAS (AMOSTRA DO DADOS)
# ============================================================================
# Explicação: Antes de fazer cálculos, vamos ver como são os dados.
# É como abrir um jornal e ler os primeiros artigos para entender o conteúdo.
# df.head() mostra as primeiras 5 linhas por padrão.

print("\n" + "=" * 80)
print("SEÇÃO 4: PRIMEIRAS 5 LINHAS DOS DADOS (amostra)")
print("=" * 80)
print("\nIsso nos mostra como os dados realmente parecem:")
print(df.head())

# ============================================================================
# SEÇÃO 5: CALCULAR ESTATÍSTICAS DESCRITIVAS
# ============================================================================
# Explicação: Aqui calculamos números "resumidos" para entender os dados:
#
# MÉDIA: valor típico
#   Ex: Se 3 imóveis custam R$ 100k, R$ 200k e R$ 300k, a média é R$ 200k
#
# MEDIANA: valor do meio (quando ordenamos do menor para o maior)
#   Ex: Se temos R$ 100k, R$ 200k, R$ 300k, a mediana é R$ 200k
#   (diferente da média quando há valores muito altos ou baixos)
#
# DESVIO-PADRÃO: quanto os valores variam em relação à média
#   Ex: Se desvio-padrão é pequeno, todos os imóveis custam parecido
#   Se desvio-padrão é grande, há imóveis muito mais caros e muito mais baratos
#
# MÍN/MÁX: valor mínimo e máximo (menor e maior imóvel)
#
# Q1 (25%) e Q3 (75%): quartis
#   Q1 = 25% dos imóveis custam menos que isso
#   Q3 = 75% dos imóveis custam menos que isso

print("\n" + "=" * 80)
print("SEÇÃO 5: ESTATÍSTICAS DESCRITIVAS (resumo dos números)")
print("=" * 80)
print("\nEstas são as principais medidas estatísticas dos dados numéricos:")
print("  - Média: valor típico")
print("  - Mediana: valor do meio (50% acima, 50% abaixo)")
print("  - Desvio-padrão: quanto variam em relação à média")
print("  - Min/Max: menor e maior valor")
print("  - Q1/Q3: quartis (25% e 75%)\n")

# df.describe() calcula todas essas estatísticas automaticamente
desc = df.describe()
print(desc)

# ============================================================================
# SEÇÃO 6: ANÁLISE DE DADOS FALTANTES (AUSÊNCIAS)
# ============================================================================
# Explicação: Nem todos os imóveis têm informações completas!
# Alguns podem não ter o valor do imóvel, outros podem não ter a área construída.
# Precisamos saber QUANTOS dados estão faltando e EM QUAIS COLUNAS.
#
# DADOS FALTANTES = campos em branco (representados como "NaN" = "Not a Number")
# Se muitos dados faltam, não podemos fazer análises confiáveis naquela coluna.

print("\n" + "=" * 80)
print("SEÇÃO 6: ANÁLISE DE DADOS FALTANTES (campos em branco)")
print("=" * 80)
print("\nProcurando por campos vazios no dataset...")

# Contar quantos dados faltam em cada coluna
missing = df.isnull().sum()

# Calcular a porcentagem de dados faltantes
missing_pct = 100 * df.isnull().sum() / len(df)

# Criar uma tabela com os resultados
missing_df = pd.DataFrame({
    'Coluna': df.columns,
    'Faltantes': missing.values,
    'Percentual (%)': missing_pct.values
}).sort_values('Faltantes', ascending=False)  # Ordenar do maior para o menor

print("\nResultado (ordenado de maior para menor falta de dados):")
print(missing_df.to_string(index=False))
print("\n💡 Dica: Se uma coluna tem poucos faltantes (<5%), é ok usar ela.")

# ============================================================================
# SEÇÃO 7: ANÁLISE DETALHADA DAS VARIÁVEIS PRINCIPAIS
# ============================================================================
# Explicação: Agora fazemos um "mergulho mais profundo" nas variáveis que 
# vamos usar para as análises futuras.
#
# Variáveis QUANTITATIVAS = números que podemos somar/subtrair
#   Ex: valor do imóvel em R$, área em m²
#
# Variáveis QUALITATIVAS = categorias/grupos
#   Ex: bairro (Bom Fim, Centro, Moinhos, etc), finalidade (apartamento, casa)
#
# Para cada uma, mostramos:
# - Quantos valores válidos (não vazios)
# - Valores principais (média, mediana, mín, máx, etc)

print("\n" + "=" * 80)
print("SEÇÃO 7: ANÁLISE DETALHADA DAS VARIÁVEIS PRINCIPAIS")
print("=" * 80)

# VARIÁVEIS QUANTITATIVAS (números)
print("\n" + "-" * 80)
print("VARIÁVEIS QUANTITATIVAS (números: valores em R$, áreas em m²)")
print("-" * 80)

quantitativas = ['VLR_VENAL_IM', 'AREA_CONSTRUIDA', 'VALOR_IPTU', 'ALIQUOTA']

for col in quantitativas:
    if col in df.columns:
        # Contar quantos valores não são vazios
        valid_count = df[col].notna().sum()
        
        print(f"\n📊 {col}:")
        print(f"   Valores preenchidos: {valid_count:,} de {len(df):,}")
        print(f"   Média (valor típico): {df[col].mean():,.2f}")
        print(f"   Mediana (valor do meio): {df[col].median():,.2f}")
        print(f"   Desvio-padrão (quanto varia): {df[col].std():,.2f}")
        print(f"   Valor mínimo: {df[col].min():,.2f}")
        print(f"   Valor máximo: {df[col].max():,.2f}")
        print(f"   25% dos valores estão abaixo de: {df[col].quantile(0.25):,.2f}")
        print(f"   75% dos valores estão abaixo de: {df[col].quantile(0.75):,.2f}")

# VARIÁVEIS QUALITATIVAS (categorias/grupos)
print("\n" + "-" * 80)
print("VARIÁVEIS QUALITATIVAS (categorias: tipos de imóvel, bairros, etc)")
print("-" * 80)

categoricas = ['FINALIDADE', 'USO', 'BAIRRO', 'DIVISAO_FISCAL']

for col in categoricas:
    if col in df.columns:
        print(f"\n🏷️  {col}:")
        print(f"   Quantidade de categorias diferentes: {df[col].nunique()}")
        print(f"   Categorias mais comuns:")
        # value_counts() mostra quantas vezes cada categoria aparece
        print(df[col].value_counts().head(10).to_string())

# ============================================================================
# SEÇÃO 8: VERIFICAÇÃO DE DUPLICATAS
# ============================================================================
# Explicação: Às vezes o mesmo imóvel aparece DUAS VEZES no banco de dados.
# Isso é um erro! Precisamos verificar se há linhas duplicadas.
#
# LINHA DUPLICADA = uma cópia exata de outra linha
# (mesmo imóvel, mesmos valores, tudo igual)
#
# Se encontrarmos muitas duplicatas, precisa "limpar" os dados antes de analisar.

print("\n" + "=" * 80)
print("SEÇÃO 8: VERIFICAÇÃO DE DUPLICATAS (mesma linha aparecendo 2x)")
print("=" * 80)

# df.duplicated() encontra linhas que são cópias exatas de outras
# .sum() conta quantas são
duplicate_rows = df.duplicated().sum()
print(f"\nLinhas duplicadas encontradas: {duplicate_rows}")

if duplicate_rows == 0:
    print("✓ Ótimo! Não há linhas duplicadas nos dados.")
else:
    print(f"⚠️ Atenção! Encontradas {duplicate_rows} linhas duplicadas!")

# Se houver coluna de ID, verificar também se há IDs duplicados
if 'ID' in df.columns or 'id' in df.columns.str.lower():
    id_col = [c for c in df.columns if 'id' in c.lower()][0]
    duplicate_ids = df[id_col].duplicated().sum()
    print(f"IDs duplicados: {duplicate_ids}")

# ============================================================================
# SEÇÃO 9: RESUMO FINAL — POPULAÇÃO
# ============================================================================
# Explicação: Aqui fazemos um RESUMO EXECUTIVO dos dados.
# É como um "relatório" que diz:
# - Quantos imóveis temos
# - Que informações temos sobre cada imóvel
# - Quais variáveis vamos usar para as análises
# - O que fazer a seguir
#
# POPULAÇÃO = todos os imóveis no banco de dados (876.248)

print("\n" + "=" * 80)
print("SEÇÃO 9: RESUMO FINAL — POPULAÇÃO COMPLETA")
print("=" * 80)

print(f"""
╔════════════════════════════════════════════════════════════════╗
║                  RESUMO DOS DADOS EXPLORADOS                 ║
╚════════════════════════════════════════════════════════════════╝

Total de imóveis (população): {len(df):,}
Período dos dados: 2026
Fonte: Dados Abertos de Porto Alegre — IPTU (Imposto Predial)

VARIÁVEIS QUANTITATIVAS QUE USAREMOS:
  📊 vlr_venal_imovel
     → Valor de mercado estimado do imóvel em R$
     → Usaremos para calcular MÉDIAS
  
  📊 mtr_area_construida_total
     → Área total construída em m²
     → Usaremos para calcular MÉDIAS
  
  📊 vlr_imposto
     → Valor do IPTU em R$
  
  📊 vlr_aliquota
     → Taxa/percentual de tributação

VARIÁVEIS QUALITATIVAS QUE USAREMOS:
  🏷️  des_finalidade
     → Tipo de imóvel: Apartamento, Casa, Salão, etc
     → Usaremos para calcular PROPORÇÕES
  
  🏷️  des_uso
     → Uso principal: Residencial, Comercial, etc
     → Usaremos para calcular PROPORÇÕES
  
  🏷️  nme_endloc_bairro_cdl
     → Qual bairro fica o imóvel
  
  🏷️  num_divisao_fiscal
     → Divisão administrativa (1, 2 ou 3)

PRÓXIMOS PASSOS:
  1️⃣  Selecionar uma AMOSTRA de ~1.066 imóveis (em vez de usar todos)
  2️⃣  Calcular estatísticas descritivas (média, mediana, etc)
  3️⃣  Fazer testes de hipóteses
  4️⃣  Comparar resultados da amostra com a população completa

IMPORTANTE:
  ⚠️  Alguns imóveis têm informações incompletas (dados faltantes)
  ⚠️  Alguns valores são muito altos ou muito baixos (outliers)
  ⚠️  Precisamos contar com esses problemas na análise futura
╚════════════════════════════════════════════════════════════════╝
""")

# ============================================================================
# SEÇÃO 10: SALVAR OS RESULTADOS EM ARQUIVOS
# ============================================================================
# Explicação: Temos dois tipos de resultados:
#
# 1. ANÁLISE DE AUSÊNCIAS: quantos dados faltam em cada coluna
#    → Será salvo em "01_analise_ausencias.csv"
#
# 2. ESTATÍSTICAS DESCRITIVAS: números resumidos (média, mediana, etc)
#    → Será salvo em "01_descritivas_populacao.csv"
#
# CSV = formato de arquivo que pode ser aberto em Excel, Google Sheets, etc
# Os arquivos servem como "base" para análises futuras.

print("\n" + "=" * 80)
print("SEÇÃO 10: SALVANDO RESULTADOS EM ARQUIVOS")
print("=" * 80)

# Salvar análise de dados faltantes em arquivo CSV
print("\nSalvando análise de dados faltantes...")
missing_df.to_csv(BASE_DIR / "01_analise_ausencias.csv", index=False)
print(f"✓ Arquivo criado: 01_analise_ausencias.csv")

# Salvar estatísticas descritivas em arquivo CSV
print("\nSalvando estatísticas descritivas...")
desc.to_csv(BASE_DIR / "01_descritivas_populacao.csv")
print(f"✓ Arquivo criado: 01_descritivas_populacao.csv")

print("\n💾 Arquivos salvos com sucesso!")
print("   Você pode abrir esses arquivos em Excel ou Google Sheets para visualizar melhor.")

# ============================================================================
# SCRIPT FINALIZADO
# ============================================================================
print("\n" + "=" * 80)
print("🎉 EXPLORAÇÃO DE DADOS CONCLUÍDA COM SUCESSO!")
print("=" * 80)
print("""
O QUE APRENDEMOS NESTE SCRIPT:
  ✓ Quantos imóveis temos: 876.248 registros
  ✓ Que informações temos sobre cada imóvel: 32 colunas
  ✓ Quais informações estão incompletas (dados faltantes)
  ✓ Números importantes de cada variável:
    - Média: valor típico
    - Mediana: valor do meio
    - Desvio-padrão: quanto varia
    - Mínimo e máximo: limites dos dados
  ✓ Quais dados estão prontos para análise

PRÓXIMA ETAPA:
  Executar o script: python scripts/02_preparacao_dados.py
  
  Esse script vai:
    • Limpar os dados (remover erros)
    • Converter tipos de números corretamente
    • Preparar os dados para seleção da amostra

DÚVIDAS SOBRE ESTE SCRIPT?
  Releia os comentários detalhados acima de cada seção.
  Leia também o documento: GUIA_RAPIDO.md
""")
print("=" * 80)
