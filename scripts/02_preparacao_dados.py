"""
================================================================================
PREPARAÇÃO DE DADOS — IPTU 2026 Porto Alegre
Trabalho Final de Estatística IA003

O QUE ESTE SCRIPT FAZ:
  Este script "limpa" e "prepara" os dados para serem usados nas análises.
  
  É como "organizar a cozinha" antes de cozinhar:
  - Remove dados que não faz sentido (ex: valores negativos)
  - Corrige tipos de dados (ex: número que estava como texto)
  - Remove linhas com problemas críticos (ex: todas as informações vazias)
  - Padroniza nomes de categorias (ex: "Apto" e "Apartamento" → mesma coisa)
  - Salva os dados "limpos" em um novo arquivo

PARA QUEM NÃO SABE ESTATÍSTICA:
  - "Limpeza de dados" = corrigir erros nos dados
  - "Tipo de dado" = como o Python entende a informação (número, texto, etc)
  - "Outlier" = valor muito diferente dos outros (ex: imóvel custando 1 trilhão)

================================================================================
"""

import pandas as pd
import numpy as np
from pathlib import Path
import warnings

# Oculta avisos de bibliotecas para deixar o relatório do processamento mais
# legível; erros continuam sendo tratados explicitamente nos blocos try/except.
warnings.filterwarnings('ignore')

# ============================================================================
# SEÇÃO 1: CARREGAR O ARQUIVO ORIGINAL
# ============================================================================
# Os caminhos são calculados a partir da localização deste script, não da pasta
# atual do terminal. Assim, o comando funciona mesmo quando executado de outro
# diretório.
print("=" * 80)
print("PREPARAÇÃO DE DADOS — IPTU 2026 Porto Alegre")
print("=" * 80)

BASE_DIR = Path(__file__).parent.parent
DATA_FILE = BASE_DIR / "iptu_2026.csv"

print(f"\n📂 Carregando dados de: {DATA_FILE}")

try:
    # O arquivo usa ponto-e-vírgula entre colunas e UTF-8 para preservar acentos.
    # O DataFrame `df` será a tabela de trabalho modificada nas etapas seguintes.
    df = pd.read_csv(
        DATA_FILE,
        sep=';',
        encoding='utf-8',
        low_memory=False,
        on_bad_lines='skip'
    )
    print(f"✓ Sucesso! {len(df):,} linhas lidas")
except Exception as e:
    print(f"❌ Erro: {e}")
    exit(1)

# ============================================================================
# SEÇÃO 2: DOCUMENTAR ESTADO INICIAL
# ============================================================================
# Guardamos a quantidade inicial de linhas para comparar com o resultado final
# e informar quantos registros foram removidos durante a limpeza.
print("\n" + "=" * 80)
print("SEÇÃO 2: ESTADO DOS DADOS ANTES DA LIMPEZA")
print("=" * 80)

linhas_iniciais = len(df)
colunas = len(df.columns)
print(f"\nDados iniciais:")
print(f"  Linhas: {linhas_iniciais:,}")
print(f"  Colunas: {colunas}")

# ============================================================================
# SEÇÃO 3: REMOVER LINHAS COMPLETAMENTE VAZIAS
# ============================================================================
# `axis=1` avalia cada linha; `all` só marca linhas em que todas as colunas
# estão ausentes. Linhas com pelo menos um valor são preservadas.
print("\n" + "=" * 80)
print("SEÇÃO 3: REMOVER LINHAS COMPLETAMENTE VAZIAS")
print("=" * 80)

# Contar linhas completamente vazias (todas as colunas são NaN)
linhas_vazias = df.isna().all(axis=1).sum()
print(f"\nLinhas completamente vazias: {linhas_vazias}")

if linhas_vazias > 0:
    df = df.dropna(how='all')
    print(f"✓ Linhas vazias removidas!")

# ============================================================================
# SEÇÃO 4: REMOVER DUPLICATAS
# ============================================================================
# A comparação considera todas as colunas. `drop_duplicates()` mantém a
# primeira ocorrência e remove apenas cópias exatas das linhas.
print("\n" + "=" * 80)
print("SEÇÃO 4: REMOVER LINHAS DUPLICADAS")
print("=" * 80)

duplicatas_antes = df.duplicated().sum()
print(f"\nLinhas duplicadas encontradas: {duplicatas_antes}")

if duplicatas_antes > 0:
    df = df.drop_duplicates()
    linhas_apos = len(df)
    print(f"✓ Duplicatas removidas! Linhas restantes: {linhas_apos:,}")

# ============================================================================
# SEÇÃO 5: CORRIGIR E PADRONIZAR TIPOS DE DADOS
# ============================================================================
# As listas incluem nomes de colunas de versões diferentes do arquivo. O teste
# `col in df.columns` permite processar apenas as variáveis que estão presentes.
print("\n" + "=" * 80)
print("SEÇÃO 5: CORRIGIR E PADRONIZAR TIPOS DE DADOS")
print("=" * 80)

# Variáveis quantitativas (números)
variaveis_numericas = [
    'VLR_VENAL_IM',
    'AREA_CONSTRUIDA',
    'VALOR_IPTU',
    'ALIQUOTA',
    'mtr_area_construida_total',
    'vlr_venal_imovel',
    'vlr_imposto',
    'vlr_aliquota'
]

# Variáveis categóricas (texto)
variaveis_categoricas = [
    'FINALIDADE',
    'USO',
    'BAIRRO',
    'DIVISAO_FISCAL',
    'des_finalidade',
    'des_uso',
    'nme_endloc_bairro_cdl',
    'num_divisao_fiscal'
]

print("\nConvertendo variáveis numéricas para tipo float...")
for col in variaveis_numericas:
    if col in df.columns:
        # Os valores usam vírgula decimal (ex.: "500,0"), enquanto o Python
        # espera ponto. Primeiro normalizamos o texto e depois convertemos.
        valores = df[col].astype("string").str.replace(",", ".", regex=False)
        # `errors='coerce'` transforma em NaN qualquer conteúdo que não seja
        # numérico, em vez de interromper o processamento da coluna inteira.
        convertidos = pd.to_numeric(valores, errors='coerce')
        # Comparamos a origem com o resultado para distinguir ausências que já
        # existiam de valores preenchidos que falharam na conversão.
        falhas = df[col].notna() & convertidos.isna()
        df[col] = convertidos
        detalhe_falhas = f"; {falhas.sum():,} valores não numéricos" if falhas.any() else ""
        print(f"  ✓ {col}: {df[col].notna().sum():,} valores válidos{detalhe_falhas}")

print("\nConvertendo variáveis categóricas para tipo string...")
for col in variaveis_categoricas:
    if col in df.columns:
        # Texto padronizado facilita comparar categorias e remover diferenças
        # causadas por espaços antes/depois dos nomes.
        df[col] = df[col].astype(str).str.strip()
        print(f"  ✓ {col}")

# ============================================================================
# SEÇÃO 6: REMOVER VALORES NEGATIVOS INVÁLIDOS
# ============================================================================
# Valores negativos não fazem sentido para as medidas monetárias e de área
# deste projeto. Em vez de apagar o registro inteiro, substituímos somente o
# campo inválido por NaN, preservando as outras informações do imóvel.
print("\n" + "=" * 80)
print("SEÇÃO 6: REMOVER VALORES NEGATIVOS (quando não faz sentido)")
print("=" * 80)

# Variáveis que nunca devem ser negativas
deve_ser_positivo = [
    'VLR_VENAL_IM', 'AREA_CONSTRUIDA', 'VALOR_IPTU', 'ALIQUOTA',
    'mtr_area_construida_total', 'vlr_venal_imovel', 'vlr_imposto', 'vlr_aliquota'
]

print("\nVerificando valores negativos...")
for col in deve_ser_positivo:
    if col in df.columns:
        negativos = (df[col] < 0).sum()
        if negativos > 0:
            print(f"  {col}: {negativos} valores negativos encontrados")
            # Substituir por NaN (dados faltantes)
            df.loc[df[col] < 0, col] = np.nan
            print(f"    ✓ Convertidos para dados faltantes")

# ============================================================================
# SEÇÃO 7: PADRONIZAR CATEGORIAS (consolidar valores similares)
# ============================================================================
# A comparação é feita em maiúsculas para não depender de como a categoria foi
# capitalizada no CSV. `str.contains` também captura rótulos que contenham o
# termo (por exemplo, descrições mais longas).
print("\n" + "=" * 80)
print("SEÇÃO 7: PADRONIZAR CATEGORIAS")
print("=" * 80)

# Consolidar categorias de finalidade
if 'des_finalidade' in df.columns:
    print("\n📌 Finalizando FINALIDADE...")
    # Converter para maiúsculas para comparação
    df['des_finalidade_upper'] = df['des_finalidade'].str.upper()
    
    # Mapear sinônimos
    mapa_finalidade = {
        'APARTAMENTO': 'Apartamento',
        'APTO': 'Apartamento',
        'CASA': 'Casa',
        'TERRENO': 'Terreno',
        'SALA': 'Sala Comercial',
        'LOJA': 'Sala Comercial',
        'GARAGEM': 'Garagem',
        'ESTACIONAMENTO': 'Garagem'
    }
    
    for chave, valor in mapa_finalidade.items():
        máscara = df['des_finalidade_upper'].str.contains(chave, na=False)
        df.loc[máscara, 'des_finalidade'] = valor
    
    df = df.drop('des_finalidade_upper', axis=1)
    unicos = df['des_finalidade'].nunique()
    print(f"  ✓ Categorias consolidadas: {unicos} tipos únicos")

# Consolidar categorias de uso
if 'des_uso' in df.columns:
    print("\n📌 Padronizando USO...")
    df['des_uso_upper'] = df['des_uso'].str.upper()
    
    mapa_uso = {
        'RESIDENCIAL': 'Residencial',
        'RESIDENCIA': 'Residencial',
        'COMERCIAL': 'Comercial',
        'COMERCIO': 'Comercial',
        'INDUSTRIAL': 'Industrial',
        'MISTO': 'Misto'
    }
    
    for chave, valor in mapa_uso.items():
        máscara = df['des_uso_upper'].str.contains(chave, na=False)
        df.loc[máscara, 'des_uso'] = valor
    
    df = df.drop('des_uso_upper', axis=1)
    unicos = df['des_uso'].nunique()
    print(f"  ✓ Categorias consolidadas: {unicos} tipos únicos")

# ============================================================================
# SEÇÃO 8: TRATAMENTO DE OUTLIERS (valores extremos)
# ============================================================================
# O intervalo interquartil (IQR = Q3 - Q1) mede a dispersão dos 50% centrais.
# Valores fora de Q1 - 1,5×IQR e Q3 + 1,5×IQR são sinalizados para inspeção,
# mas não removidos: valores extremos podem ser imóveis reais.
print("\n" + "=" * 80)
print("SEÇÃO 8: IDENTIFICAR OUTLIERS (valores muito altos ou baixos)")
print("=" * 80)

# Para cada variável numérica, identificar outliers usando IQR
print("\nMétodo: Intervalo Interquartil (IQR)")
print("Um valor é outlier se estiver fora do intervalo [Q1 - 1.5×IQR, Q3 + 1.5×IQR]")
print("Outliers serão MANTIDOS nos dados (importante para análise)!")

for col in variaveis_numericas:
    if col in df.columns and df[col].notna().sum() > 0:
        # Quartis e limites são calculados ignorando valores ausentes.
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        
        outliers = ((df[col] < limite_inferior) | (df[col] > limite_superior)).sum()
        
        if outliers > 0:
            pct = 100 * outliers / df[col].notna().sum()
            print(f"\n  {col}:")
            print(f"    Outliers: {outliers} ({pct:.2f}%)")
            print(f"    Intervalo normal: [{limite_inferior:,.2f}, {limite_superior:,.2f}]")
            print(f"    ⚠️  MANTIDOS nos dados para análise!")

# ============================================================================
# SEÇÃO 9: CRIAR VARIÁVEIS DE CONTROLE
# ============================================================================
# Essas colunas ajudam a rastrear a posição de cada linha no conjunto já limpo
# e a avaliar a completude de cada registro nas etapas posteriores.
print("\n" + "=" * 80)
print("SEÇÃO 9: CRIAR VARIÁVEIS ADICIONAIS")
print("=" * 80)

# Adicionar índice original para rastreamento
df['indice_original'] = range(len(df))
print("  ✓ Variável 'indice_original' criada (para rastreabilidade)")

# Adicionar indicador de dados faltantes por linha
df['num_campos_vazios'] = df.isna().sum(axis=1)
print("  ✓ Variável 'num_campos_vazios' criada")

# ============================================================================
# SEÇÃO 10: RESUMO FINAL DA LIMPEZA
# ============================================================================
# O resumo compara os totais inicial e final e calcula a proporção de registros
# preservados. A contagem de ausências destaca campos úteis para as análises.
print("\n" + "=" * 80)
print("SEÇÃO 10: RESUMO FINAL DA LIMPEZA")
print("=" * 80)

linhas_finais = len(df)
linhas_removidas = linhas_iniciais - linhas_finais

print(f"""
╔════════════════════════════════════════════════════════════════╗
║                    RESUMO DA LIMPEZA                          ║
╚════════════════════════════════════════════════════════════════╝

Linhas iniciais:         {linhas_iniciais:>12,}
Linhas removidas:        {linhas_removidas:>12,}
  ├─ Linhas vazias:      {linhas_vazias:>12}
  └─ Linhas duplicadas:  {duplicatas_antes:>12}

Linhas finais:           {linhas_finais:>12,}
Percentual mantido:      {100*linhas_finais/linhas_iniciais:>11.2f}%

Colunas:                 {colunas:>12}

DADOS FALTANTES POR VARIÁVEL (principais):
""")

# Mostrar as principais variáveis com dados faltantes
principais = ['vlr_venal_imovel', 'des_uso', 'mtr_area_construida_total',
              'des_finalidade', 'nme_endloc_bairro_cdl']
for col in principais:
    if col in df.columns:
        faltantes = df[col].isna().sum()
        pct = 100 * faltantes / len(df)
        print(f"  {col}: {faltantes:>8,} ({pct:>5.2f}%)")

print("""
╚════════════════════════════════════════════════════════════════╝
""")

# ============================================================================
# SEÇÃO 11: SALVAR DADOS LIMPOS
# ============================================================================
# A pasta é criada apenas se ainda não existir. O arquivo mantém o separador e
# a codificação usados na leitura para facilitar as próximas etapas do projeto.
print("=" * 80)
print("SEÇÃO 11: SALVANDO DADOS PREPARADOS")
print("=" * 80)

# Criar pasta de dados processados se não existir
dados_dir = BASE_DIR / "dados_processados"
dados_dir.mkdir(exist_ok=True)

# Salvar dados limpos
arquivo_limpo = dados_dir / "dados_limpos.csv"
print(f"\n💾 Salvando em: {arquivo_limpo}")

try:
    df.to_csv(arquivo_limpo, sep=';', encoding='utf-8', index=False)
    print(f"✓ Arquivo criado com sucesso!")
    print(f"  Linhas: {len(df):,}")
    print(f"  Colunas: {len(df.columns)}")
except Exception as e:
    print(f"❌ Erro ao salvar: {e}")
    exit(1)

# ============================================================================
# SCRIPT FINALIZADO
# ============================================================================
print("\n" + "=" * 80)
print("🎉 PREPARAÇÃO DE DADOS CONCLUÍDA COM SUCESSO!")
print("=" * 80)
print("""
O QUE FOI FEITO:
  ✓ Dados carregados e validados
  ✓ Linhas vazias removidas
  ✓ Linhas duplicadas removidas
  ✓ Tipos de dados corrigidos
  ✓ Valores negativos inválidos tratados
  ✓ Categorias padronizadas
  ✓ Outliers identificados (mantidos para análise)
  ✓ Variáveis de controle adicionadas
  ✓ Dados salvos em arquivo limpo

PRÓXIMA ETAPA:
  Executar: python scripts/03_amostragem.py
  
  Esse script vai:
    • Selecionar uma amostra de ~1.066 imóveis
    • Usar método de amostragem aleatória simples (AAS)
    • Guardar os índices da amostra para análise

IMPORTANTE:
  Os dados agora estão prontos para amostragem e análise!
  Nenhum dado foi "descartado", apenas reorganizado e validado.

""")
print("=" * 80)
