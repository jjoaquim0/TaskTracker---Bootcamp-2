"""Testes das regras do TaskTracker. Executar com: python3 -m unittest discover tests"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import (  # noqa: E402
    buscar_tarefa,
    contar_por_status,
    criar_tarefa,
    data_valida,
    normalizar_prioridade,
    titulo_valido,
)


class TestRegras(unittest.TestCase):
    def test_titulo_vazio_ou_so_espacos_e_rejeitado(self):
        self.assertFalse(titulo_valido(""))
        self.assertFalse(titulo_valido("   "))
        self.assertTrue(titulo_valido("Estudar Git"))

    def test_prioridade_aceita_apenas_alta_media_baixa(self):
        self.assertEqual(normalizar_prioridade("alta"), "Alta")
        self.assertEqual(normalizar_prioridade("Média"), "Média")
        self.assertEqual(normalizar_prioridade("media"), "Média")
        self.assertEqual(normalizar_prioridade(" BAIXA "), "Baixa")
        self.assertIsNone(normalizar_prioridade("urgente"))
        self.assertIsNone(normalizar_prioridade(""))

    def test_data_deve_existir_no_formato_dd_mm_aaaa(self):
        self.assertTrue(data_valida("20/10/2026"))
        self.assertFalse(data_valida("31/02/2026"))
        self.assertFalse(data_valida("2026-10-20"))
        self.assertFalse(data_valida(""))

    def test_nova_tarefa_comeca_pendente(self):
        tarefa = criar_tarefa(1, "Estudar", "", "Alta", "20/10/2026")
        self.assertEqual(tarefa["status"], "Pendente")
        self.assertEqual(tarefa["id"], 1)

    def test_busca_e_resumo_por_status(self):
        tarefas = [
            criar_tarefa(1, "A", "", "Alta", "20/10/2026"),
            criar_tarefa(2, "B", "", "Baixa", "21/10/2026"),
        ]
        tarefas[1]["status"] = "Concluída"
        self.assertIs(buscar_tarefa(tarefas, 2), tarefas[1])
        self.assertIsNone(buscar_tarefa(tarefas, 99))
        self.assertEqual(contar_por_status(tarefas), (1, 1))


if __name__ == "__main__":
    unittest.main()
