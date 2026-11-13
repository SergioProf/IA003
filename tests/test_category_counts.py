import unittest

import pandas as pd

from app import category_counts


class CategoryCountsTests(unittest.TestCase):
    def test_all_categories_are_counted_without_grouping(self):
        values = pd.Series(["Residencial", None, "Agrícola", "Residencial"])
        categories = ["Residencial", "(Ausente)", "Agrícola"]

        self.assertEqual(category_counts(values, categories, False), [2, 1, 1])

    def test_grouped_categories_include_all_remaining_values(self):
        values = pd.Series(["Residencial", None, "Agrícola", "Comercial"])
        categories = ["Residencial", "(Ausente)"]

        self.assertEqual(category_counts(values, categories, True), [1, 1, 2])

    def test_sample_can_lack_a_population_category(self):
        values = pd.Series(["Residencial", None])
        categories = ["Residencial", "(Ausente)", "Agrícola"]

        self.assertEqual(category_counts(values, categories, False), [1, 1, 0])


if __name__ == "__main__":
    unittest.main()
