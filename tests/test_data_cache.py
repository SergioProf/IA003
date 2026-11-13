import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

import app


class DataCacheTests(unittest.TestCase):
    def tearDown(self):
        app.load_data_cached.clear()

    def test_reloads_data_when_file_changes_at_same_path(self):
        row = {column: "1" for column in app.REQUIRED_COLUMNS}
        row["des_uso"] = "Residencial"
        row["em_amostra"] = "True"

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "dados.csv"
            pd.DataFrame([row]).to_csv(path, sep=";", index=False)
            with patch.object(app, "DATA_FILE", path):
                first = app.load_data()
                row["des_uso"] = "Exclusivamente Residencial"
                pd.DataFrame([row]).to_csv(path, sep=";", index=False)
                second = app.load_data()

        self.assertEqual(first["des_uso"].iloc[0], "Residencial")
        self.assertEqual(second["des_uso"].iloc[0], "Exclusivamente Residencial")

    def test_reloads_when_same_size_file_is_updated(self):
        row = {column: "1" for column in app.REQUIRED_COLUMNS}
        row["des_uso"] = "Casa"
        row["em_amostra"] = "True"

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "dados.csv"
            pd.DataFrame([row]).to_csv(path, sep=";", index=False)
            initial_stat = path.stat()
            with patch.object(app, "DATA_FILE", path):
                app.load_data()
                row["des_uso"] = "Loja"
                pd.DataFrame([row]).to_csv(path, sep=";", index=False)
                os.utime(
                    path,
                    ns=(initial_stat.st_atime_ns, initial_stat.st_mtime_ns + 1_000_000_000),
                )
                self.assertEqual(path.stat().st_size, initial_stat.st_size)
                second = app.load_data()

        self.assertEqual(second["des_uso"].iloc[0], "Loja")


if __name__ == "__main__":
    unittest.main()
