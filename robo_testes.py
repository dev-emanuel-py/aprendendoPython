import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megamen = Robo('Mega Man', bateria=50)
        print('setUp sendo executado.....')

    def test_carregar(self):
        """Testando se o robo esta carregando"""
        self.megamen.carregar()
        self.assertEqual(self.megamen.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megamen.dizer_nome(), 'BEEP BOOP BEEP, EU SOU MEGA MAN')
        self.assertEqual(self.megamen.bateria, 49, 'A bateria deveria esta em 49%')
        self.assertIsInstance(self.megamen, Robo)  # Teste da IsInstance

    def tearDown(self):
        print('tearDown() sendo executado....')


if __name__ == '__main__':
    unittest.main()


