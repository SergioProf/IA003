import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd


class PreparacaoUsoTests(unittest.TestCase):
    def test_preparacao_preserva_categorias_de_uso_distintas(self):
        labels = [
            "Exclusivamente Residencial",
            "Não Exclusivamente Residencial",
            "Agrícola",
            None,
        ]
        data = pd.DataFrame(
            {
                "des_uso": labels,
                "des_finalidade": ["Apartamento", "Loja", "Terreno", "Casa"],
                "vlr_venal_imovel": [10, 20, 30, 40],
                "mtr_area_construida_total": [1, 2, 3, 4],
                "nme_endloc_bairro_cdl": ["Centro"] * 4,
            }
        )
        script = Path(__file__).resolve().parent.parent / "scripts" / "02_preparacao_dados.py"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            shutil.copy2(script, root / "scripts" / script.name)
            data.to_csv(root / "iptu_2026.csv", sep=";", index=False)
            env = dict(os.environ, PYTHONUTF8="1")
            subprocess.run(
                [sys.executable, str(root / "scripts" / script.name)],
                check=True, capture_output=True, text=True, encoding="utf-8", env=env,
            )
            result = pd.read_csv(
                root / "dados_processados" / "dados_limpos.csv",
                sep=";", dtype="string",
            )
        self.assertEqual(result["des_uso"].fillna("(ausente)").tolist(), [
            "Exclusivamente Residencial",
            "Não Exclusivamente Residencial",
            "Agrícola",
            "(ausente)",
        ])


if __name__ == "__main__":
    unittest.main()
