from lib2to3.pgen2 import driver
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from animal.models import Animal

class AnimalTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(r'D:\Programação\Apps\tdd-busca-animal\chromedriver.exe')
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

    def tearDown(self):
        self.browser.quit()

    def test_buca_um_animal(self):
        """Teste da busca no menu"""

        # Vini, deseja encontrar um novo animal,
        # para adotar.

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome. 
        busca_animal = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(busca_animal.get_attribute('placeholder'), 'Exemplo: leão')

        # Ele pesquisa por Leão e clica no botão pesquisar.
        busca_animal.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, "form button").click()

        # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

        # Ele desiste de adotar um leão.


        pass