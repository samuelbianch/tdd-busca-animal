from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animal.models import Animal

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'cachorro',
            predador = 'Não',
            venenoso = 'Não',
            domestico = 'Sim'
        )

    def test_view_retorna_caracterista_do_animal(self):
        """Teste que verifica o retorno da caracteristica do animal"""
        response = self.client.get('/',
            {'buscar': 'cachorro'}
        )
        caracteristica_animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'cachorro')