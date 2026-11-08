"""
================================================================================
ANÁLISE DESCRITIVA — IPTU 2026 Porto Alegre
Trabalho Final de Estatística IA003

O QUE ESTE SCRIPT FAZ:
  Este script calcula estatísticas descritivas (números resumidos) para:
  
  1. POPULAÇÃO COMPLETA (876.248 imóveis)
     - Estatísticas gerais de todas as variáveis
  
  2. AMOSTRA (1.066 imóveis sorteados)
     - Mesmas estatísticas, apenas para a amostra
  
  3. COMPARAÇÃO
     - Colocar lado a lado população e amostra
     - Ver se a amostra representa bem a população
  
  Estatísticas calculadas:
    - Frequências (quantos de cada tipo)
    - Média (valor típico)
    - Mediana (valor do meio)
    - Desvio-padrão (quanto varia)
    - Mínimo e máximo (limites)
    - Quartis (Q1, Q2, Q3)

PARA QUEM NÃO SABE ESTATÍSTICA:
  - "Descritiva" = descrever/resumir os dados com números e gráficos
  - "Frequência" = quantas vezes algo aparece
  - "Distribuição" = como os dados estão espalhados

================================================================================
"""

import pandas as pd
import numpy as np
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

# ============================================================================
# SEÇÃO 1: CARREGAR DADOS
# ============================================================================
print("=" * 80)
print("ANÁLISE DESCRITIVA — IPTU 2026 Porto Alegre")
print("=" * 80)

BASE_DIR = Path(__file__).parent.parent
dados_dir = BASE_DIR / "dados_processados"

arquivo_com_indicador = dados_dir / "dados_com_indicador_amostra.csv"

print(f"\n📂 Carregando dados: {arquivo_com_indicador}")

if not arquivo_com_indicador.exists():
    print("❌ Arquivo não encontrado!")
    print("   Execute primeiro: python scripts/03_amostragem.py")
    exit(1)

try:
    df = pd.read_csv(arquivo_com_indicador, sep=';', encoding='utf-8')
    print(f"✓ Sucesso! {len(df):,} linhas lidas")
except Exception as e:
    print(f"❌ Erro: {e}")
    exit(1)

# Separar população e amostra
df_populacao = df.copy()
df_amostra = df[df['em_amostra'] == True].copy()

print(f"\n  População: {len(df_populacao):,} registros")
print(f"  Amostra:   {len(df_amostra):,} registros")

# ============================================================================
# SEÇÃO 2: DEFINIR VARIÁVEIS A ANALISAR
# ============================================================================
print("\n" + "=" * 80)
print("SEÇÃO 2: VARIÁVEIS A ANALISAR")
print("=" * 80)

# Variáveis quantitativas (números)
variaveis_quantitativas = [
    'vlr_venal_imovel',        # Valor venal do imóvel (R$)
    'mtr_area_construida_total',  # Área construída (m²)
    'vlr_imposto',             # IPTU (R$)
    'vlr_aliquota'             # Alíquota (%)
]

# Variáveis qualitativas (categorias)
variaveis_qualitativas = [
    'des_finalidade',          # Tipo de imóvel
    'des_uso',                 # Uso principal
    'nme_endloc_bairro_cdl',   # Bairro
    'num_divisao_fiscal'       # Divisão fiscal
]

print("\nVariáveis quantitativas a analisar:")
for var in variaveis_quantitativas:
    if var in df.columns:
        print(f"  ✓ {var}")

print("\nVariáveis qualitativas a analisar:")
for var in variaveis_qualitativas:
    if var in df.columns:
        print(f"  ✓ {var}")

# ============================================================================
# SEÇÃO 3: ANÁLISE DE VARIÁVEIS QUANTITATIVAS
# ============================================================================
print("\n" + "=" * 80)
print("SEÇÃO 3: ESTATÍSTICAS DESCRITIVAS - VARIÁVEIS QUANTITATIVAS")
print("=" * 80)

# Dicionário para armazenar resultados
resultados_quantitativas = {}

print("\nCalculando estatísticas para variáveis numéricas...")

for var in variaveis_quantitativas:
    if var not in df.columns:
        continue
    
    print(f"\n{'─' * 80}")
    print(f"📊 {var.upper()}")
    print(f"{'─' * 80}")
    
    # Dados válidos (não-nulos)
    dados_pop = df_populacao[var].dropna()
    dados_amostra = df_amostra[var].dropna()
    
    n_pop = len(dados_pop)
    n_amostra = len(dados_amostra)
    
    print(f"\nCASOS VÁLIDOS:")
    print(f"  População: {n_pop:,} ({100*n_pop/len(df_populacao):.2f}%)")
    print(f"  Amostra:   {n_amostra:,} ({100*n_amostra/len(df_amostra):.2f}%)")
    
    # Calcular estatísticas
    stats_pop = {
        'Media': dados_pop.mean(),
        'Mediana': dados_pop.median(),
        'Desvio-Padrao': dados_pop.std(),
        'Minimo': dados_pop.min(),
        'Q1': dados_pop.quantile(0.25),
        'Q3': dados_pop.quantile(0.75),
        'Maximo': dados_pop.max(),
        'Amplitude': dados_pop.max() - dados_pop.min(),
        'CV': (dados_pop.std() / dados_pop.mean() * 100) if dados_pop.mean() != 0 else np.nan
    }
    
    stats_amostra = {
        'Media': dados_amostra.mean(),
        'Mediana': dados_amostra.median(),
        'Desvio-Padrao': dados_amostra.std(),
        'Minimo': dados_amostra.min(),
        'Q1': dados_amostra.quantile(0.25),
        'Q3': dados_amostra.quantile(0.75),
        'Maximo': dados_amostra.max(),
        'Amplitude': dados_amostra.max() - dados_amostra.min(),
        'CV': (dados_amostra.std() / dados_amostra.mean() * 100) if dados_amostra.mean() != 0 else np.nan
    }
    
    # Tabela comparativa
    df_comparacao = pd.DataFrame({
        'Estatística': list(stats_pop.keys()),
        'População': list(stats_pop.values()),
        'Amostra': list(stats_amostra.values()),
    })
    
    df_comparacao['Diferença (%)'] = (
        100 * (df_comparacao['Amostra'] - df_comparacao['População']) / 
        df_comparacao['População'].abs()
    )
    
    print("\nESTATÍSTICAS DESCRITIVAS:")
    print(df_comparacao.to_string(index=False))
    
    # Interpretação
    print(f"\nINTERPRETAÇÃO:")
    print(f"  Média (valor típico):")
    print(f"    População: R$ {stats_pop['Media']:,.2f}")
    print(f"    Amostra:   R$ {stats_amostra['Media']:,.2f}")
    print(f"    Diferença: {abs(stats_pop['Media'] - stats_amostra['Media']) / stats_pop['Media'] * 100:.2f}%")
    
    print(f"\n  Desvio-Padrão (quanto varia):")
    print(f"    População: {stats_pop['Desvio-Padrao']:,.2f}")
    print(f"    Amostra:   {stats_amostra['Desvio-Padrao']:,.2f}")
    
    print(f"\n  Coeficiente de Variação (CV):")
    print(f"    População: {stats_pop['CV']:.2f}%")
    print(f"    Amostra:   {stats_amostra['CV']:.2f}%")
    if stats_pop['CV'] < 30:
        print(f"    ✓ Dados com variação BAIXA (CV < 30%)")
    elif stats_pop['CV'] < 60:
        print(f"    ⚠️  Dados com variação MÉDIA (30% ≤ CV < 60%)")
    else:
        print(f"    ⚠️  Dados com variação ALTA (CV ≥ 60%)")
    
    resultados_quantitativas[var] = {
        'populacao': stats_pop,
        'amostra': stats_amostra,
        'comparacao': df_comparacao
    }

# ============================================================================
# SEÇÃO 4: ANÁLISE DE VARIÁVEIS QUALITATIVAS
# ============================================================================
print("\n" + "=" * 80)
print("SEÇÃO 4: FREQUÊNCIAS - VARIÁVEIS QUALITATIVAS")
print("=" * 80)

resultados_qualitativas = {}

for var in variaveis_qualitativas:
    if var not in df.columns:
        continue
    
    print(f"\n{'─' * 80}")
    print(f"🏷️  {var.upper()}")
    print(f"{'─' * 80}")
    
    # Contar frequências
    freq_pop = df_populacao[var].value_counts(dropna=False)
    freq_amostra = df_amostra[var].value_counts(dropna=False)
    
    # Calcular proporções
    prop_pop = 100 * df_populacao[var].value_counts(normalize=True, dropna=False)
    prop_amostra = 100 * df_amostra[var].value_counts(normalize=True, dropna=False)
    
    # Criar tabela comparativa
    df_freq_comp = pd.DataFrame({
        'Categoria': freq_pop.index,
        'Freq_Pop': freq_pop.values,
        'Prop_Pop (%)': prop_pop.values,
        'Freq_Amostra': [freq_amostra.get(cat, 0) for cat in freq_pop.index],
        'Prop_Amostra (%)': [prop_amostra.get(cat, 0) for cat in freq_pop.index],
    })
    
    print(f"\nNÚMERO DE CATEGORIAS: {len(freq_pop)}")
    print(f"\nTOP 10 CATEGORIAS:")
    print(df_freq_comp.head(10).to_string(index=False))
    
    if len(freq_pop) > 10:
        print(f"\n... e mais {len(freq_pop) - 10} categorias")
    
    resultados_qualitativas[var] = df_freq_comp

# ============================================================================
# SEÇÃO 5: SALVAR RESULTADOS
# ============================================================================
print("\n" + "=" * 80)
print("SEÇÃO 5: SALVANDO RESULTADOS")
print("=" * 80)

# Criar pasta de saídas
saidas_dir = BASE_DIR / "saidas"
saidas_dir.mkdir(exist_ok=True)

# Salvar estatísticas quantitativas
print("\nSalvando estatísticas de variáveis quantitativas...")
for var, resultados in resultados_quantitativas.items():
    arquivo = saidas_dir / f"desc_{var}.csv"
    resultados['comparacao'].to_csv(arquivo, index=False, encoding='utf-8')
    print(f"  ✓ {arquivo.name}")

# Salvar frequências qualitativas
print("\nSalvando frequências de variáveis qualitativas...")
for var, freq_df in resultados_qualitativas.items():
    arquivo = saidas_dir / f"freq_{var}.csv"
    freq_df.to_csv(arquivo, index=False, encoding='utf-8')
    print(f"  ✓ {arquivo.name}")

# ============================================================================
# SEÇÃO 6: RESUMO GERAL
# ============================================================================
print("\n" + "=" * 80)
print("SEÇÃO 6: RESUMO GERAL")
print("=" * 80)

print(f"""
╔════════════════════════════════════════════════════════════════╗
║              ANÁLISE DESCRITIVA CONCLUÍDA                     ║
╚════════════════════════════════════════════════════════════════╝

VARIÁVEIS QUANTITATIVAS ANALISADAS: {len(variaveis_quantitativas)}
  • vlr_venal_imovel (Valor do imóvel em R$)
  • mtr_area_construida_total (Área construída em m²)
  • vlr_imposto (IPTU em R$)
  • vlr_aliquota (Alíquota em %)

VARIÁVEIS QUALITATIVAS ANALISADAS: {len(variaveis_qualitativas)}
  • des_finalidade (Tipo de imóvel)
  • des_uso (Uso principal)
  • nme_endloc_bairro_cdl (Bairro)
  • num_divisao_fiscal (Divisão fiscal)

POPULAÇÃO vs AMOSTRA:
  População: {len(df_populacao):,} registros
  Amostra:   {len(df_amostra):,} registros
  Taxa:      {100*len(df_amostra)/len(df_populacao):.4f}%

RESULTADOS SALVOS EM:
  {saidas_dir}
  
  Arquivos criados:
  • desc_*.csv (estatísticas de variáveis quantitativas)
  • freq_*.csv (frequências de variáveis qualitativas)

╚════════════════════════════════════════════════════════════════╝
""")

# ============================================================================
# SEÇÃO 7: INTERPRETAÇÃO
# ============================================================================
print("=" * 80)
print("SEÇÃO 7: COMO INTERPRETAR OS RESULTADOS")
print("=" * 80)

print("""
VARIÁVEIS QUANTITATIVAS (números):
  
  MÉDIA: valor típico
    Se a média de preço é R$ 400.000, o imóvel "médio" custa isso.
  
  MEDIANA: valor do meio
    Se a mediana é R$ 300.000, 50% dos imóveis custam menos que isso.
    Se diferente da média = há valores muito altos ou muito baixos!
  
  DESVIO-PADRÃO: quanto varia
    Valores pequenos = imóveis com preços parecidos
    Valores grandes = muita diferença entre imóveis
  
  COEFICIENTE DE VARIAÇÃO (CV):
    CV < 30% = variação BAIXA (dados homogêneos)
    30% ≤ CV < 60% = variação MÉDIA
    CV ≥ 60% = variação ALTA (dados muito dispersos)

VARIÁVEIS QUALITATIVAS (categorias):
  
  FREQUÊNCIA: quantas vezes aparece
    Ex: "Apartamento" aparece 500.000 vezes
  
  PROPORÇÃO (%): percentual do total
    Ex: "Apartamento" = 57.09% dos imóveis
  
  COMPARAÇÃO POPULAÇÃO vs AMOSTRA:
    Se as proporções são parecidas = amostra representa bem a população!
    Se são muito diferentes = verificar se amostra está enviesada

COMO SABER SE A AMOSTRA É BOA?
  ✓ Frequências/proporções parecidas com a população
  ✓ Médias próximas à população
  ✓ Desvios-padrão similares
  ✓ Sem outliers estranhos

""")

# ============================================================================
# SCRIPT FINALIZADO
# ============================================================================
print("\n" + "=" * 80)
print("🎉 ANÁLISE DESCRITIVA CONCLUÍDA COM SUCESSO!")
print("=" * 80)
print("""
O QUE FOI FEITO:
  ✓ Estatísticas calculadas para variáveis quantitativas
  ✓ Frequências calculadas para variáveis qualitativas
  ✓ População e amostra comparadas lado a lado
  ✓ Tabelas salvas em arquivos CSV

PRÓXIMA ETAPA:
  Executar: python scripts/05_inferencia_estatistica.py
  
  Esse script vai:
    • Fazer testes de hipóteses
    • Calcular intervalos de confiança
    • Verificar suposições estatísticas
    • Tirar conclusões sobre a população baseadas na amostra

IMPORTANTE:
  As análises descritivas aqui estabelecem a base para os testes!
  Revise os números antes de passar para a etapa de inferência.

""")
print("=" * 80)
