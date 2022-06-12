from django.test import TestCase, RequestFactory
from animal.models import Animal

class AnimalModelsTestCase(TestCase):

    def setUp(self):

        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

    def test_animal_cadastrado_com_caracteristicas(self):
        """Teste que verifica se o animal esta cadastrado com suas respectivas caracteristicas"""

        self.assertEqual(self.animal.nome_animal, 'Leão')