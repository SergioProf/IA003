import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

import app


SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "06_exportar_dados_painel.py"
spec = importlib.util.spec_from_file_location("exportar_dados_painel", SCRIPT)
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)


class ExportarDadosPainelTests(unittest.TestCase):
    def test_export_preserves_records_and_omits_unused_columns(self):
        source_data = pd.DataFrame(
            {
                "vlr_venal_imovel": ["100,50", "200,00"],
                "mtr_area_construida_total": ["50", "75"],
                "vlr_imposto": ["1,00", "2,00"],
                "vlr_aliquota": ["0,1", "0,2"],
                "des_finalidade": ["Residencial", "Comercial"],
                "des_uso": ["Casa", "Loja"],
                "nme_endloc_bairro_cdl": ["Centro", "Centro"],
                "num_divisao_fiscal": ["01", "02"],
                "em_amostra": ["False", "True"],
                "nme_endloc_logradouro": ["Não publicar", "Não publicar"],
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "origem.csv"
            destination = Path(directory) / "painel" / "dados.csv.gz"
            source_data.to_csv(source, sep=";", index=False)
            with patch.object(exporter, "SOURCE", source), patch.object(
                exporter, "DESTINATION", destination
            ):
                exporter.main()
            result = pd.read_csv(destination, sep=";", dtype="string")

        self.assertEqual(set(result.columns), set(app.REQUIRED_COLUMNS))
        pd.testing.assert_frame_equal(
            result, source_data[result.columns].astype("string")
        )


if __name__ == "__main__":
    unittest.main()
