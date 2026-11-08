"""
================================================================================
INFERÊNCIA ESTATÍSTICA — IPTU 2026 Porto Alegre
Trabalho Final de Estatística IA003

O QUE ESTE SCRIPT FAZ:
  Este script faz testes de hipóteses sobre a população usando dados da
  amostra. É a parte mais interessante da Estatística!
  
  Você vai:
  1. Escolher uma HIPÓTESE sobre a população
  2. Testar se essa hipótese é verdadeira usando a amostra
  3. Calcular intervalos de confiança
  4. Tirar CONCLUSÕES com embasamento estatístico
  
  QUATRO HIPÓTESES TESTADAS:
    H1: Proporção de Apartamentos = 40%
    H2: Proporção de Uso Residencial = 85%
    H3: Média do Valor Venal = R$ 400.000
    H4: Média da Área Construída = 100 m²

PARA QUEM NÃO SABE ESTATÍSTICA:
  - "Hipótese" = suposição que você quer testar
  - "Teste de hipótese" = procedimento para verificar se está certa
  - "Valor-p (p-value)" = probabilidade de estar errado
  - "Intervalo de confiança" = "margem de segurança" para estimativas
  - "Nível de significância (α)" = quanto de risco você aceita (5%)

================================================================================
"""

import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

# ============================================================================
# SEÇÃO 1: CARREGAR DADOS
# ============================================================================
print("=" * 80)
print("INFERÊNCIA ESTATÍSTICA — IPTU 2026 Porto Alegre")
print("=" * 80)

BASE_DIR = Path(__file__).parent.parent
dados_dir = BASE_DIR / "dados_processados"

arquivo_com_indicador = dados_dir / "dados_com_indicador_amostra.csv"

print(f"\n📂 Carregando dados: {arquivo_com_indicador}")

if not arquivo_com_indicador.exists():
    print("❌ Arquivo não encontrado!")
    print("   Execute antes: python scripts/03_amostragem.py")
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
# SEÇÃO 2: PARÂMETROS DOS TESTES
# ============================================================================
print("\n" + "=" * 80)
print("SEÇÃO 2: CONFIGURAÇÃO DOS TESTES DE HIPÓTESES")
print("=" * 80)

# Nível de significância (α)
alpha = 0.05  # 5%

print(f"""
PARÂMETROS DE TESTE:
  Nível de significância (α): {alpha} (5%)
  
  Significado:
    Se valor-p < 0,05 → rejeitar H₀ (hipótese nula)
    Se valor-p ≥ 0,05 → não rejeitar H₀
    
  Isso significa: estamos dispostos a aceitar 5% de risco de erro.

TIPO DE TESTE:
  Bilateral (two-tailed)
    Testamos se μ ≠ valor esperado (não apenas maior ou menor)
""")

# ============================================================================
# SEÇÃO 3: HIPÓTESE 1 - PROPORÇÃO DE APARTAMENTOS
# ============================================================================
print("\n" + "=" * 80)
print("HIPÓTESE 1: PROPORÇÃO DE APARTAMENTOS")
print("=" * 80)

H1_label = "Proporção de Apartamentos"
H1_p0 = 0.40  # Valor que estamos testando

print(f"\nH₀ (Hipótese Nula):     p = {H1_p0} (40% são apartamentos)")
print(f"H₁ (Hipótese Alternativa): p ≠ {H1_p0}")

# Limpar dados (remover NaN)
dados_h1_pop = df_populacao['des_finalidade'].dropna()
dados_h1_amostra = df_amostra['des_finalidade'].dropna()

# Contar apartamentos
n_pop_h1 = len(dados_h1_pop)
x_pop_h1 = (dados_h1_pop == 'Apartamento').sum()
p_pop_h1 = x_pop_h1 / n_pop_h1

n_amostra_h1 = len(dados_h1_amostra)
x_amostra_h1 = (dados_h1_amostra == 'Apartamento').sum()
p_amostra_h1 = x_amostra_h1 / n_amostra_h1

print(f"\nPOPULAÇÃO:")
print(f"  N válido: {n_pop_h1:,}")
print(f"  Apartamentos: {x_pop_h1:,}")
print(f"  Proporção: {p_pop_h1:.4f} ({100*p_pop_h1:.2f}%)")

print(f"\nAMOSTRA:")
print(f"  n válido: {n_amostra_h1:,}")
print(f"  Apartamentos: {x_amostra_h1:,}")
print(f"  Proporção: {p_amostra_h1:.4f} ({100*p_amostra_h1:.2f}%)")

# Teste Z para proporção
# Usar a amostra para testar a hipótese
z_h1 = (p_amostra_h1 - H1_p0) / np.sqrt(H1_p0 * (1 - H1_p0) / n_amostra_h1)
p_value_h1 = 2 * (1 - stats.norm.cdf(abs(z_h1)))  # Bilateral

# Intervalo de confiança 95% para proporção
se_h1 = np.sqrt(p_amostra_h1 * (1 - p_amostra_h1) / n_amostra_h1)
ic_lower_h1 = p_amostra_h1 - 1.96 * se_h1
ic_upper_h1 = p_amostra_h1 + 1.96 * se_h1

print(f"\nTESTE Z PARA PROPORÇÃO:")
print(f"  Estatística Z: {z_h1:.4f}")
print(f"  Valor-p (bilateral): {p_value_h1:.6f}")
print(f"  Significância: {'***' if p_value_h1 < 0.001 else '**' if p_value_h1 < 0.01 else '*' if p_value_h1 < 0.05 else 'ns'}")

print(f"\nINTERVALO DE CONFIANÇA 95%:")
print(f"  [{ic_lower_h1:.4f}, {ic_upper_h1:.4f}]")
print(f"  [{100*ic_lower_h1:.2f}%, {100*ic_upper_h1:.2f}%]")

print(f"\nCONCLUSÃO:")
if p_value_h1 < alpha:
    print(f"  ✓ Valor-p ({p_value_h1:.6f}) < α ({alpha})")
    print(f"  → Rejeitar H₀")
    print(f"  → A proporção de apartamentos É SIGNIFICATIVAMENTE DIFERENTE de {100*H1_p0:.0f}%")
else:
    print(f"  ✗ Valor-p ({p_value_h1:.6f}) ≥ α ({alpha})")
    print(f"  → Não rejeitar H₀")
    print(f"  → Não há evidência de que a proporção seja diferente de {100*H1_p0:.0f}%")

# ============================================================================
# SEÇÃO 4: HIPÓTESE 2 - PROPORÇÃO DE USO RESIDENCIAL
# ============================================================================
print("\n" + "=" * 80)
print("HIPÓTESE 2: PROPORÇÃO DE USO RESIDENCIAL")
print("=" * 80)

H2_label = "Proporção de Uso Residencial"
H2_p0 = 0.85  # 85%

print(f"\nH₀ (Hipótese Nula):     p = {H2_p0} (85% uso residencial)")
print(f"H₁ (Hipótese Alternativa): p ≠ {H2_p0}")

# Limpar dados
dados_h2_pop = df_populacao['des_uso'].dropna()
dados_h2_amostra = df_amostra['des_uso'].dropna()

# Contar residencial
n_pop_h2 = len(dados_h2_pop)
x_pop_h2 = (dados_h2_pop == 'Residencial').sum()
p_pop_h2 = x_pop_h2 / n_pop_h2

n_amostra_h2 = len(dados_h2_amostra)
x_amostra_h2 = (dados_h2_amostra == 'Residencial').sum()
p_amostra_h2 = x_amostra_h2 / n_amostra_h2

print(f"\nPOPULAÇÃO:")
print(f"  N válido: {n_pop_h2:,}")
print(f"  Residencial: {x_pop_h2:,}")
print(f"  Proporção: {p_pop_h2:.4f} ({100*p_pop_h2:.2f}%)")

print(f"\nAMOSTRA:")
print(f"  n válido: {n_amostra_h2:,}")
print(f"  Residencial: {x_amostra_h2:,}")
print(f"  Proporção: {p_amostra_h2:.4f} ({100*p_amostra_h2:.2f}%)")

# Teste Z para proporção
z_h2 = (p_amostra_h2 - H2_p0) / np.sqrt(H2_p0 * (1 - H2_p0) / n_amostra_h2)
p_value_h2 = 2 * (1 - stats.norm.cdf(abs(z_h2)))  # Bilateral

# Intervalo de confiança 95%
se_h2 = np.sqrt(p_amostra_h2 * (1 - p_amostra_h2) / n_amostra_h2)
ic_lower_h2 = p_amostra_h2 - 1.96 * se_h2
ic_upper_h2 = p_amostra_h2 + 1.96 * se_h2

print(f"\nTESTE Z PARA PROPORÇÃO:")
print(f"  Estatística Z: {z_h2:.4f}")
print(f"  Valor-p (bilateral): {p_value_h2:.6f}")

print(f"\nINTERVALO DE CONFIANÇA 95%:")
print(f"  [{100*ic_lower_h2:.2f}%, {100*ic_upper_h2:.2f}%]")

print(f"\nCONCLUSÃO:")
if p_value_h2 < alpha:
    print(f"  → Rejeitar H₀")
    print(f"  → Proporção de uso residencial É SIGNIFICATIVAMENTE DIFERENTE de {100*H2_p0:.0f}%")
else:
    print(f"  → Não rejeitar H₀")
    print(f"  → Não há evidência de diferença de {100*H2_p0:.0f}%")

# ============================================================================
# SEÇÃO 5: HIPÓTESE 3 - MÉDIA DO VALOR VENAL
# ============================================================================
print("\n" + "=" * 80)
print("HIPÓTESE 3: MÉDIA DO VALOR VENAL DO IMÓVEL")
print("=" * 80)

H3_label = "Média do Valor Venal"
H3_mu0 = 400000  # R$ 400.000

print(f"\nH₀ (Hipótese Nula):     μ = R$ {H3_mu0:,.0f}")
print(f"H₁ (Hipótese Alternativa): μ ≠ R$ {H3_mu0:,.0f}")

# Limpar dados
dados_h3_pop = df_populacao['vlr_venal_imovel'].dropna()
dados_h3_amostra = df_amostra['vlr_venal_imovel'].dropna()

n_pop_h3 = len(dados_h3_pop)
mean_pop_h3 = dados_h3_pop.mean()
std_pop_h3 = dados_h3_pop.std()

n_amostra_h3 = len(dados_h3_amostra)
mean_amostra_h3 = dados_h3_amostra.mean()
std_amostra_h3 = dados_h3_amostra.std()
se_h3 = std_amostra_h3 / np.sqrt(n_amostra_h3)

print(f"\nPOPULAÇÃO:")
print(f"  N válido: {n_pop_h3:,}")
print(f"  Média: R$ {mean_pop_h3:,.2f}")
print(f"  Desvio-padrão: R$ {std_pop_h3:,.2f}")
print(f"  CV: {100*std_pop_h3/mean_pop_h3:.2f}%")

print(f"\nAMOSTRA:")
print(f"  n válido: {n_amostra_h3:,}")
print(f"  Média: R$ {mean_amostra_h3:,.2f}")
print(f"  Desvio-padrão: R$ {std_amostra_h3:,.2f}")
print(f"  Erro padrão: R$ {se_h3:,.2f}")

# Teste t para média
t_h3 = (mean_amostra_h3 - H3_mu0) / se_h3
p_value_h3 = 2 * (1 - stats.t.cdf(abs(t_h3), df=n_amostra_h3-1))  # Bilateral

# Intervalo de confiança 95%
t_critical = stats.t.ppf(1 - alpha/2, df=n_amostra_h3-1)
ic_lower_h3 = mean_amostra_h3 - t_critical * se_h3
ic_upper_h3 = mean_amostra_h3 + t_critical * se_h3

print(f"\nTESTE T PARA MÉDIA:")
print(f"  Estatística t: {t_h3:.4f}")
print(f"  Graus de liberdade: {n_amostra_h3-1}")
print(f"  Valor-p (bilateral): {p_value_h3:.6f}")

print(f"\nINTERVALO DE CONFIANÇA 95%:")
print(f"  [R$ {ic_lower_h3:,.2f}, R$ {ic_upper_h3:,.2f}]")

print(f"\nCONCLUSÃO:")
if p_value_h3 < alpha:
    print(f"  → Rejeitar H₀")
    print(f"  → A média É SIGNIFICATIVAMENTE DIFERENTE de R$ {H3_mu0:,.0f}")
else:
    print(f"  → Não rejeitar H₀")
    print(f"  → Não há evidência de diferença de R$ {H3_mu0:,.0f}")

# ============================================================================
# SEÇÃO 6: HIPÓTESE 4 - MÉDIA DA ÁREA CONSTRUÍDA
# ============================================================================
print("\n" + "=" * 80)
print("HIPÓTESE 4: MÉDIA DA ÁREA CONSTRUÍDA")
print("=" * 80)

H4_label = "Média da Área Construída"
H4_mu0 = 100  # 100 m²

print(f"\nH₀ (Hipótese Nula):     μ = {H4_mu0} m²")
print(f"H₁ (Hipótese Alternativa): μ ≠ {H4_mu0} m²")

# Limpar dados
dados_h4_pop = df_populacao['mtr_area_construida_total'].dropna()
dados_h4_amostra = df_amostra['mtr_area_construida_total'].dropna()

n_pop_h4 = len(dados_h4_pop)
mean_pop_h4 = dados_h4_pop.mean()
std_pop_h4 = dados_h4_pop.std()

n_amostra_h4 = len(dados_h4_amostra)
mean_amostra_h4 = dados_h4_amostra.mean()
std_amostra_h4 = dados_h4_amostra.std()
se_h4 = std_amostra_h4 / np.sqrt(n_amostra_h4)

print(f"\nPOPULAÇÃO:")
print(f"  N válido: {n_pop_h4:,}")
print(f"  Média: {mean_pop_h4:.2f} m²")
print(f"  Desvio-padrão: {std_pop_h4:.2f} m²")

print(f"\nAMOSTRA:")
print(f"  n válido: {n_amostra_h4:,}")
print(f"  Média: {mean_amostra_h4:.2f} m²")
print(f"  Desvio-padrão: {std_amostra_h4:.2f} m²")
print(f"  Erro padrão: {se_h4:.2f} m²")

# Teste t para média
t_h4 = (mean_amostra_h4 - H4_mu0) / se_h4
p_value_h4 = 2 * (1 - stats.t.cdf(abs(t_h4), df=n_amostra_h4-1))  # Bilateral

# Intervalo de confiança 95%
t_critical = stats.t.ppf(1 - alpha/2, df=n_amostra_h4-1)
ic_lower_h4 = mean_amostra_h4 - t_critical * se_h4
ic_upper_h4 = mean_amostra_h4 + t_critical * se_h4

print(f"\nTESTE T PARA MÉDIA:")
print(f"  Estatística t: {t_h4:.4f}")
print(f"  Graus de liberdade: {n_amostra_h4-1}")
print(f"  Valor-p (bilateral): {p_value_h4:.6f}")

print(f"\nINTERVALO DE CONFIANÇA 95%:")
print(f"  [{ic_lower_h4:.2f}, {ic_upper_h4:.2f}] m²")

print(f"\nCONCLUSÃO:")
if p_value_h4 < alpha:
    print(f"  → Rejeitar H₀")
    print(f"  → A média É SIGNIFICATIVAMENTE DIFERENTE de {H4_mu0} m²")
else:
    print(f"  → Não rejeitar H₀")
    print(f"  → Não há evidência de diferença de {H4_mu0} m²")

# ============================================================================
# SEÇÃO 7: TABELA RESUMIDA DOS RESULTADOS
# ============================================================================
print("\n" + "=" * 80)
print("SEÇÃO 7: RESUMO DOS TESTES DE HIPÓTESES")
print("=" * 80)

resultados_testes = pd.DataFrame({
    'Hipótese': [
        'H1: p_Apartamento = 0,40',
        'H2: p_Residencial = 0,85',
        'H3: μ_Valor = 400k',
        'H4: μ_Área = 100'
    ],
    'Estatística': [
        f'{z_h1:.4f}',
        f'{z_h2:.4f}',
        f'{t_h3:.4f}',
        f'{t_h4:.4f}'
    ],
    'Valor-p': [
        f'{p_value_h1:.6f}',
        f'{p_value_h2:.6f}',
        f'{p_value_h3:.6f}',
        f'{p_value_h4:.6f}'
    ],
    'Decisão': [
        'Rejeitar H₀' if p_value_h1 < alpha else 'Não rejeitar H₀',
        'Rejeitar H₀' if p_value_h2 < alpha else 'Não rejeitar H₀',
        'Rejeitar H₀' if p_value_h3 < alpha else 'Não rejeitar H₀',
        'Rejeitar H₀' if p_value_h4 < alpha else 'Não rejeitar H₀'
    ]
})

print("\n")
print(resultados_testes.to_string(index=False))

# ============================================================================
# SEÇÃO 8: SALVAR RESULTADOS
# ============================================================================
print("\n" + "=" * 80)
print("SEÇÃO 8: SALVANDO RESULTADOS")
print("=" * 80)

saidas_dir = BASE_DIR / "saidas"
saidas_dir.mkdir(exist_ok=True)

# Salvar tabela resumida
arquivo_resumo = saidas_dir / "testes_hipoteses.csv"
resultados_testes.to_csv(arquivo_resumo, index=False, encoding='utf-8')
print(f"✓ Resumo salvo em: {arquivo_resumo.name}")

# ============================================================================
# SCRIPT FINALIZADO
# ============================================================================
print("\n" + "=" * 80)
print("🎉 INFERÊNCIA ESTATÍSTICA CONCLUÍDA COM SUCESSO!")
print("=" * 80)
print(f"""
O QUE FOI FEITO:
  ✓ 4 testes de hipóteses realizados
  ✓ Intervalos de confiança calculados
  ✓ Conclusões tiradas para cada hipótese
  ✓ Resultados salvos em arquivo CSV

HIPÓTESES TESTADAS:
  1. Proporção de Apartamentos = 40%
  2. Proporção de Uso Residencial = 85%
  3. Média do Valor Venal = R$ 400.000
  4. Média da Área Construída = 100 m²

INTERPRETAÇÃO DOS RESULTADOS:
  • valor-p < 0,05 → Rejeitar H₀ (resultado SIGNIFICATIVO)
  • valor-p ≥ 0,05 → Não rejeitar H₀ (resultado NÃO significativo)

PRÓXIMOS PASSOS:
  1. Criar painéis interativos com Streamlit
  2. Visualizar resultados em gráficos
  3. Gravar vídeo explicativo
  4. Publicar links finais

IMPORTANTE:
  Os testes assumem que a amostra foi selecionada corretamente!
  Verifique se as suposições foram atendidas (normalidade, etc).

""")
print("=" * 80)
