import unittest

from app import display_value


class DisplayFormattingTests(unittest.TestCase):
    def test_currency_uses_brazilian_real_format(self):
        self.assertEqual(
            display_value(1234567.89, "vlr_venal_imovel"),
            "R$ 1.234.567,89",
        )

    def test_currency_can_be_rounded_for_chart_axis(self):
        self.assertEqual(
            display_value(1234567.89, "vlr_venal_imovel", decimals=0),
            "R$ 1.234.568",
        )

    def test_missing_currency_value_is_displayed_as_dash(self):
        self.assertEqual(display_value(float("nan"), "vlr_venal_imovel"), "R$ —")


if __name__ == "__main__":
    unittest.main()
