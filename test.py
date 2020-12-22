import unittest
from unittest.mock import patch
from main import search_by_number, shelf_search, all_doc, add_doc, del_doc, documents, directories


class TestMain(unittest.TestCase):

    def test_1_find_people(self):
        print('\n' + 'Проверка search_by_number')
        self.assertEqual(search_by_number(documents, '11-2'), 'Геннадий Покемонов')

    def test_2_find_shelf(self):
        print('\n' + 'Проверка shelf_search')
        self.assertEqual(shelf_search(directories, '10006'), '2')

    def test_3_list_docs(self):
        print('\n' + 'Проверка all_docs')
        self.assertIn({"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}, all_doc(documents))

    @patch('builtins.input')
    def test_4_add_doc(self, m_input):
        print('\n' + 'Проверка add_doc')
        m_input.side_effect = ["invoice", "11-23", "Василий Пупкин", '2']
        self.assertTrue(add_doc(documents, directories))

    @patch('builtins.input')
    def test_5_del_doc(self, m_input):
        print('\n' + 'Проверка del_doc')
        m_input.side_effect = ['11-2']
        self.assertTrue(del_doc(documents, directories))
