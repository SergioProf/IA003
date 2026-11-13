import unittest

from streamlit.testing.v1 import AppTest


def inference_panel():
    import pandas as pd

    from app import render_inference_panel

    data = pd.DataFrame(
        {
            "des_finalidade": ["Apartamento", "Casa", "Casa", "Apartamento"],
            "des_uso": [
                "Exclusivamente Residencial",
                "Não Exclusivamente Residencial",
                "Exclusivamente Residencial",
                "Exclusivamente Residencial",
            ],
            "vlr_venal_imovel": [100000, 200000, 300000, 400000],
            "mtr_area_construida_total": [50, 80, 120, 150],
        }
    )
    render_inference_panel(data, data)


class InferenceQuestionsTests(unittest.TestCase):
    def test_questions_appear_before_the_corresponding_tests(self):
        panel = AppTest.from_function(inference_panel, default_timeout=20).run()
        self.assertFalse(panel.exception)
        elements = [
            (element.type, getattr(element, "value", None))
            for element in panel.main
            if element.type in ("markdown", "expander")
        ]
        questions = [
            "A proporção de apartamentos é diferente de 40%?",
            "A proporção de imóveis de uso exclusivamente residencial é diferente de 85%?",
            "O valor venal médio é diferente de R$ 400 mil?",
            "A área construída média é diferente de 100 m²?",
        ]
        expander_labels = [
            "Proporção de apartamentos",
            "Proporção de uso exclusivamente residencial",
            "Média do valor venal",
            "Média da área construída",
        ]
        for question in questions:
            position = elements.index(("markdown", f"**{question}**"))
            self.assertEqual(elements[position + 1][0], "expander")
        self.assertEqual([item.label for item in panel.expander], expander_labels)
        row = panel.dataframe[0].value.iloc[1]
        self.assertEqual(row["Parâmetro populacional"], "75,00%")
        self.assertEqual(row["Estimativa amostral"], "75,00%")


if __name__ == "__main__":
    unittest.main()
