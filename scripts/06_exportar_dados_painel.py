"""Exporta somente as colunas utilizadas pelo painel para publicação."""

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE = BASE_DIR / "dados_processados" / "dados_com_indicador_amostra.csv"
DESTINATION = BASE_DIR / "dados_painel" / "dados_painel.csv.gz"
COLUMNS = [
    "vlr_venal_imovel",
    "mtr_area_construida_total",
    "vlr_imposto",
    "vlr_aliquota",
    "des_finalidade",
    "des_uso",
    "nme_endloc_bairro_cdl",
    "num_divisao_fiscal",
    "em_amostra",
]


def main():
    print(f"Lendo dados de {SOURCE}")
    data = pd.read_csv(
        SOURCE, sep=";", encoding="utf-8", usecols=COLUMNS, dtype="string"
    )
    DESTINATION.parent.mkdir(exist_ok=True)
    data.to_csv(
        DESTINATION, sep=";", encoding="utf-8", index=False,
        compression={"method": "gzip", "mtime": 1},
    )
    print(f"Dados do painel exportados: {len(data):,} registros em {DESTINATION}")


if __name__ == "__main__":
    main()
