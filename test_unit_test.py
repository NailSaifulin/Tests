#####################################ТЕСТ_ЗАДАЧА-1###################################################

import unittest, requests
from main import create_list, unique_numbers, maximum_volume
from parameterized import parameterized, parameterized_class

FIXTURE = [
    ({'facebook': 55, 'yandex': 120, 'vk': 115}, 'yandex'),
    ({'google': 99, 'email': 42, 'ok': 98}, 'google'),
    ({'vk': 115, 'google': 99, 'email': 42}, 'vk')
]


class TestFunc(unittest.TestCase):

    def test_create_list(self):
        list_test = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']}
        ]
        etalon = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}]
        result = create_list(list_test)
        self.assertEqual(result, etalon)

    def test_unique_numbers(self):
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}
        etalon = [213, 15, 54, 119, 98, 35]
        result = unique_numbers(ids)
        self.assertEqual(result, etalon)


    @parameterized.expand(FIXTURE)
    def test_maximum_volume(self, stats, etalon):
        result = maximum_volume(stats)
        self.assertEqual(result, etalon)





