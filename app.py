from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from scipy import stats


BASE_DIR = Path(__file__).parent
LOCAL_DATA_FILE = BASE_DIR / "dados_processados" / "dados_com_indicador_amostra.csv"
PUBLIC_DATA_FILE = BASE_DIR / "dados_painel" / "dados_painel.csv.gz"
DATA_FILE = LOCAL_DATA_FILE if LOCAL_DATA_FILE.is_file() else PUBLIC_DATA_FILE
SAMPLE_COLUMN = "em_amostra"
ALPHA = 0.05

VARIABLES = {
    "vlr_venal_imovel": {
        "label": "Valor venal do imóvel",
        "kind": "numeric",
        "unit": "R$",
    },
    "mtr_area_construida_total": {
        "label": "Área construída total",
        "kind": "numeric",
        "unit": "m²",
    },
    "vlr_imposto": {"label": "Valor do IPTU", "kind": "numeric", "unit": "R$"},
    "vlr_aliquota": {"label": "Alíquota", "kind": "numeric", "unit": "%"},
    "des_finalidade": {
        "label": "Finalidade",
        "kind": "category",
        "unit": "",
    },
    "des_uso": {"label": "Uso", "kind": "category", "unit": ""},
    "nme_endloc_bairro_cdl": {
        "label": "Bairro",
        "kind": "category",
        "unit": "",
    },
    "num_divisao_fiscal": {
        "label": "Divisão fiscal",
        "kind": "category",
        "unit": "",
    },
}

NUMERIC_VARIABLES = [
    name for name, metadata in VARIABLES.items() if metadata["kind"] == "numeric"
]
REQUIRED_COLUMNS = list(VARIABLES) + [SAMPLE_COLUMN]


@st.cache_data(show_spinner="Carregando os dados preparados...")
def load_data():
    header = pd.read_csv(DATA_FILE, sep=";", encoding="utf-8", nrows=0)
    missing_columns = sorted(set(REQUIRED_COLUMNS) - set(header.columns))
    if missing_columns:
        raise ValueError(
            "O arquivo de dados não contém as colunas necessárias: "
            + ", ".join(missing_columns)
        )

    data = pd.read_csv(
        DATA_FILE,
        sep=";",
        encoding="utf-8",
        usecols=REQUIRED_COLUMNS,
        dtype="string",
        low_memory=False,
    )
    for column in NUMERIC_VARIABLES:
        values = data[column].str.replace(",", ".", regex=False)
        data[column] = pd.to_numeric(values, errors="coerce")

    sample_flags = data[SAMPLE_COLUMN].str.strip().str.lower()
    if not sample_flags.isin(["true", "false"]).all():
        raise ValueError(
            f"A coluna {SAMPLE_COLUMN} deve conter somente True ou False."
        )
    data[SAMPLE_COLUMN] = sample_flags.eq("true")
    return data


def format_number(value, decimals=2):
    if pd.isna(value):
        return "—"
    formatted = f"{value:,.{decimals}f}"
    return formatted.replace(",", "_").replace(".", ",").replace("_", ".")


def display_value(value, variable, decimals=2):
    unit = VARIABLES[variable]["unit"]
    number = format_number(value, decimals=decimals)
    if unit == "R$":
        return f"R$ {number}"
    if unit:
        return f"{number} {unit}"
    return number


def descriptive_statistics(series):
    values = series.dropna()
    if values.empty:
        return None
    return {
        "N válido": len(values),
        "Média": values.mean(),
        "Mediana": values.median(),
        "Desvio-padrão": values.std(),
        "Mínimo": values.min(),
        "Q1": values.quantile(0.25),
        "Q3": values.quantile(0.75),
        "Máximo": values.max(),
    }


def render_numeric_chart(variable, population, sample, compare, max_percentile):
    population_values = population[variable].dropna()
    sample_values = sample[variable].dropna()
    upper_bound = population_values.quantile(max_percentile / 100)
    lower_bound = population_values.min()
    if upper_bound <= lower_bound:
        upper_bound = lower_bound + 1

    bins = np.linspace(lower_bound, upper_bound, 41)
    figure = go.Figure()
    sources = [("População", population_values)]
    if compare:
        sources.append(("Amostra", sample_values))

    excluded = {}
    for label, values in sources:
        visible = values[(values >= lower_bound) & (values <= upper_bound)]
        counts, edges = np.histogram(visible, bins=bins)
        widths = np.diff(edges)
        density = counts / (counts.sum() * widths) if counts.sum() else counts
        centers = (edges[:-1] + edges[1:]) / 2
        is_currency = VARIABLES[variable]["unit"] == "R$"
        figure.add_trace(
            go.Scatter(
                x=centers,
                y=density,
                mode="lines",
                name=label,
                customdata=(
                    [display_value(value, variable) for value in centers]
                    if is_currency
                    else None
                ),
                hovertemplate=(
                    "%{customdata}"
                    if is_currency
                    else "%{x:,.2f}"
                )
                + "<br>Densidade: %{y:.6g}<extra>%{fullData.name}</extra>",
            )
        )
        excluded[label] = len(values) - len(visible)

    if VARIABLES[variable]["unit"] == "R$":
        tick_values = np.linspace(lower_bound, upper_bound, 6)
        figure.update_xaxes(
            tickmode="array",
            tickvals=tick_values,
            ticktext=[
                display_value(value, variable, decimals=0)
                for value in tick_values
            ],
        )

    figure.update_layout(
        title="Distribuição dos valores válidos",
        xaxis_title=f"{VARIABLES[variable]['label']} ({VARIABLES[variable]['unit']})",
        yaxis_title="Densidade",
        hovermode="x unified",
        legend_title="Conjunto",
    )
    st.plotly_chart(figure, use_container_width=True)
    exclusions = "; ".join(
        f"{label}: {count:,}" for label, count in excluded.items()
    )
    interval = (
        f"{display_value(lower_bound, variable)}–"
        f"{display_value(upper_bound, variable)}"
        if VARIABLES[variable]["unit"] == "R$"
        else f"{format_number(lower_bound)}–{format_number(upper_bound)}"
    )
    st.caption(
        f"O gráfico limita a exibição ao percentil {max_percentile:g} da população "
        f"(intervalo {interval}). "
        f"Valores fora do intervalo não aparecem — {exclusions}. "
        "As medidas descritivas acima usam todos os valores válidos."
    )


def category_counts(series, categories, group_rest):
    values = series.fillna("(Ausente)").astype(str)
    counts = values.value_counts()
    result = [int(counts.get(category, 0)) for category in categories]
    if group_rest:
        result.append(int(counts[~counts.index.isin(categories)].sum()))
    return result


def render_category_chart(variable, population, sample, compare, top_n):
    population_values = population[variable].fillna("(Ausente)").astype(str)
    population_counts = population_values.value_counts()
    categories = population_counts.head(top_n).index.tolist()
    group_rest = len(population_counts) > top_n
    labels = categories.copy()
    if group_rest:
        other_label = "Demais categorias"
        while other_label in labels:
            other_label += " (agrupadas)"
        labels.append(other_label)

    figure = go.Figure()
    sources = [("População", population)]
    if compare:
        sources.append(("Amostra", sample))
    for label, source in sources:
        counts = category_counts(source[variable], categories, group_rest)
        denominator = len(source)
        percentages = [100 * count / denominator for count in counts]
        figure.add_trace(
            go.Bar(
                x=labels,
                y=percentages,
                name=label,
                hovertemplate="%{x}<br>%{y:.2f}%<extra>%{fullData.name}</extra>",
            )
        )

    figure.update_layout(
        title=f"Frequência relativa — {VARIABLES[variable]['label']}",
        xaxis_title=VARIABLES[variable]["label"],
        yaxis_title="Participação nos registros (%)",
        barmode="group" if compare else "relative",
        legend_title="Conjunto",
    )
    st.plotly_chart(figure, use_container_width=True)

    table = pd.DataFrame({"Categoria": labels})
    for label, source in sources:
        counts = category_counts(source[variable], categories, group_rest)
        table[f"Registros — {label}"] = counts
        table[f"Proporção (%) — {label}"] = [
            100 * count / len(source) for count in counts
        ]
    st.dataframe(table, hide_index=True, use_container_width=True)


def render_descriptive_panel(page, population, sample):
    is_sample_panel = page == "Amostra"
    source = sample if is_sample_panel else population
    st.title(f"Análise descritiva — {page.lower()}")
    st.caption(
        "A população contém todos os registros preparados; a amostra usa "
        "exclusivamente os registros sorteados na AAS."
    )

    variable = st.selectbox(
        "Variável para explorar",
        list(VARIABLES),
        format_func=lambda name: VARIABLES[name]["label"],
    )
    values = source[variable]
    valid_count = int(values.notna().sum())
    metric_columns = st.columns(3)
    metric_columns[0].metric("Registros", f"{len(source):,}".replace(",", "."))
    metric_columns[1].metric(
        "Casos válidos", f"{valid_count:,}".replace(",", ".")
    )
    metric_columns[2].metric(
        "Ausências", f"{len(source) - valid_count:,}".replace(",", ".")
    )

    if VARIABLES[variable]["kind"] == "numeric":
        pop_stats = descriptive_statistics(population[variable])
        sample_stats = descriptive_statistics(sample[variable])
        current_stats = sample_stats if is_sample_panel else pop_stats
        if current_stats is None:
            st.warning("Não há valores válidos para esta variável.")
            return

        st.subheader("Medidas descritivas")
        stat_rows = [
            "N válido",
            "Média",
            "Mediana",
            "Desvio-padrão",
            "Mínimo",
            "Q1",
            "Q3",
            "Máximo",
        ]
        table = pd.DataFrame({"Medida": stat_rows})
        if is_sample_panel:
            if pop_stats is None:
                st.warning("A variável não tem valores válidos na população.")
                return
            table["População"] = [pop_stats[key] for key in stat_rows]
            table["Amostra"] = [sample_stats[key] for key in stat_rows]
        else:
            table["População"] = [pop_stats[key] for key in stat_rows]
        if VARIABLES[variable]["unit"] == "R$":
            for column in ("População", "Amostra"):
                if column in table:
                    table[column] = [
                        format_number(value, decimals=0)
                        if statistic == "N válido"
                        else display_value(value, variable)
                        for statistic, value in zip(
                            stat_rows, table[column]
                        )
                    ]
        st.dataframe(table, hide_index=True, use_container_width=True)

        percentile = st.slider(
            "Percentil máximo exibido no histograma",
            min_value=90.0,
            max_value=100.0,
            value=99.0,
            step=0.5,
            help="A limitação afeta somente o gráfico, não as medidas descritivas.",
        )
        render_numeric_chart(
            variable, population, sample, is_sample_panel, percentile
        )
    else:
        top_n = st.slider(
            "Número de categorias destacadas",
            min_value=5,
            max_value=30,
            value=10,
            step=1,
        )
        render_category_chart(
            variable, population, sample, is_sample_panel, top_n
        )


def proportion_test(population, sample, variable, event, null_value, label):
    population_values = population[variable].dropna()
    sample_values = sample[variable].dropna()
    if sample_values.empty or population_values.empty:
        raise ValueError(f"Não há casos válidos para o teste: {label}.")

    population_estimate = float((population_values == event).mean())
    sample_estimate = float((sample_values == event).mean())
    sample_size = len(sample_values)
    standard_error = np.sqrt(null_value * (1 - null_value) / sample_size)
    statistic = (sample_estimate - null_value) / standard_error
    p_value = 2 * stats.norm.sf(abs(statistic))
    confidence_error = 1.96 * np.sqrt(
        sample_estimate * (1 - sample_estimate) / sample_size
    )
    return {
        "label": label,
        "parameter": "Proporção",
        "population": population_estimate,
        "estimate": sample_estimate,
        "sample_size": sample_size,
        "null_value": null_value,
        "lower": sample_estimate - confidence_error,
        "upper": sample_estimate + confidence_error,
        "statistic": statistic,
        "p_value": p_value,
        "test_name": "Z",
        "event": event,
    }


def mean_test(population, sample, variable, null_value, label):
    population_values = population[variable].dropna()
    sample_values = sample[variable].dropna()
    if len(sample_values) < 2 or population_values.empty:
        raise ValueError(f"Não há casos válidos suficientes para o teste: {label}.")

    sample_mean = float(sample_values.mean())
    standard_error = float(sample_values.std(ddof=1) / np.sqrt(len(sample_values)))
    if standard_error == 0:
        raise ValueError(f"Erro-padrão igual a zero para o teste: {label}.")
    degrees_of_freedom = len(sample_values) - 1
    statistic = (sample_mean - null_value) / standard_error
    p_value = 2 * stats.t.sf(abs(statistic), df=degrees_of_freedom)
    critical_value = stats.t.ppf(1 - ALPHA / 2, df=degrees_of_freedom)
    confidence_error = critical_value * standard_error
    return {
        "label": label,
        "parameter": "Média",
        "population": float(population_values.mean()),
        "estimate": sample_mean,
        "sample_size": len(sample_values),
        "null_value": null_value,
        "lower": sample_mean - confidence_error,
        "upper": sample_mean + confidence_error,
        "statistic": statistic,
        "p_value": p_value,
        "test_name": "t",
        "event": None,
    }


def render_inference_panel(population, sample):
    st.title("Inferência estatística e comparação")
    st.caption(
        "Os parâmetros populacionais são calculados diretamente na população. "
        "Intervalos e testes usam somente os casos válidos da amostra."
    )
    try:
        results = [
            (
                "A proporção de apartamentos é diferente de 40%?",
                proportion_test(
                    population, sample, "des_finalidade", "Apartamento", 0.40,
                    "Proporção de apartamentos",
                ),
            ),
            (
                "A proporção de imóveis de uso exclusivamente residencial é diferente de 85%?",
                proportion_test(
                    population, sample, "des_uso", "Exclusivamente Residencial", 0.85,
                    "Proporção de uso exclusivamente residencial",
                ),
            ),
            (
                "O valor venal médio é diferente de R$ 400 mil?",
                mean_test(
                    population, sample, "vlr_venal_imovel", 400000,
                    "Média do valor venal",
                ),
            ),
            (
                "A área construída média é diferente de 100 m²?",
                mean_test(
                    population, sample, "mtr_area_construida_total", 100,
                    "Média da área construída",
                ),
            ),
        ]
    except ValueError as error:
        st.error(f"Não foi possível calcular os testes: {error}")
        return

    table_rows = []
    for _, result in results:
        unit = (
            "R$"
            if result["label"] == "Média do valor venal"
            else "m²"
            if result["label"] == "Média da área construída"
            else ""
        )
        formatter = lambda value: (
            f"R$ {format_number(value)}"
            if unit == "R$"
            else f"{format_number(value)} {unit}".strip()
            if unit
            else f"{format_number(value * 100)}%"
        )
        decision = (
            "Rejeitar H₀"
            if result["p_value"] < ALPHA
            else "Não rejeitar H₀"
        )
        table_rows.append(
            {
                "Hipótese": result["label"],
                "Parâmetro populacional": formatter(result["population"]),
                "Estimativa amostral": formatter(result["estimate"]),
                "IC 95% da amostra": (
                    f"[{formatter(result['lower'])}, "
                    f"{formatter(result['upper'])}]"
                ),
                "Estatística": (
                    f"{result['test_name']} = {result['statistic']:.4f}"
                ),
                "Valor-p": f"{result['p_value']:.6g}",
                "Decisão (α = 5%)": decision,
            }
        )

    st.subheader("Resumo dos quatro testes")
    st.dataframe(
        pd.DataFrame(table_rows),
        hide_index=True,
        use_container_width=True,
    )

    for question, result in results:
        st.markdown(f"**{question}**")
        with st.expander(result["label"]):
            if result["parameter"] == "Proporção":
                null_description = (
                    f"H₀: p = {result['null_value']:.0%}; "
                    f"H₁: p ≠ {result['null_value']:.0%}. "
                    f"Evento: {result['event']}."
                )
                interval_description = "IC de Wald de 95%."
            else:
                variable = (
                    "vlr_venal_imovel"
                    if result["label"] == "Média do valor venal"
                    else "mtr_area_construida_total"
                )
                null_value = display_value(result["null_value"], variable)
                null_description = (
                    f"H₀: μ = {null_value}; H₁: μ ≠ μ₀."
                )
                interval_description = "IC t de Student de 95%."
            st.write(null_description)
            st.write(
                f"N válido na amostra: {result['sample_size']:,}. "
                f"{interval_description} Valor-p: {result['p_value']:.6g}."
            )
            st.write(
                "Conclusão: "
                + (
                    "rejeitar H₀ ao nível de 5%."
                    if result["p_value"] < ALPHA
                    else "não rejeitar H₀ ao nível de 5%; isso não prova que H₀ seja verdadeira."
                )
            )

    st.info(
        "Limitações: o IC de proporção é de Wald e usa aproximação normal; "
        "o teste t pressupõe observações independentes. Há forte assimetria "
        "em valores monetários e registros de um mesmo lote podem não ser "
        "independentes. Categorias ausentes são excluídas de cada teste."
    )


def main():
    st.set_page_config(
        page_title="IPTU 2026 — Painéis estatísticos",
        page_icon="📊",
        layout="wide",
    )
    st.title("IPTU 2026 — Porto Alegre")
    st.caption(
        "Painéis interativos de estatística descritiva e inferencial. "
        "Dados do exercício 2026."
    )
    st.markdown(
        "Fonte: [IPTU — Dados Abertos de Porto Alegre]"
        "(https://dadosabertos.poa.br/dataset/iptu)"
    )

    if not DATA_FILE.is_file():
        st.error(
            "Arquivo de dados preparado ou reduzido não encontrado. Execute primeiro "
            "`python scripts/02_preparacao_dados.py` e "
            "`python scripts/03_amostragem.py`."
        )
        st.stop()

    try:
        data = load_data()
    except (ValueError, UnicodeDecodeError) as error:
        st.error(f"Não foi possível carregar os dados: {error}")
        st.stop()

    population = data
    sample = data[data[SAMPLE_COLUMN]].copy()
    if sample.empty:
        st.error(
            "A coluna `em_amostra` não contém registros sorteados. "
            "Execute novamente `python scripts/03_amostragem.py`."
        )
        st.stop()

    st.sidebar.header("Navegação")
    page = st.sidebar.radio(
        "Selecione um painel",
        ["População", "Amostra", "Inferência e comparação"],
    )
    st.sidebar.metric("Registros na população", f"{len(population):,}".replace(",", "."))
    st.sidebar.metric("Registros na amostra", f"{len(sample):,}".replace(",", "."))
    st.sidebar.caption("AAS sem reposição · semente 42")

    if page == "Inferência e comparação":
        render_inference_panel(population, sample)
    else:
        render_descriptive_panel(page, population, sample)


if __name__ == "__main__":
    main()
