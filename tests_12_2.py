import runner_and_tournament as r_and_t
import unittest as ut


class TournamentTest(ut.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = r_and_t.Runner("Усэйн", 10)
        self.runner2 = r_and_t.Runner("Андрей", 9)
        self.runner3 = r_and_t.Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls):
        result = {}
        for key, value in cls.all_result.items():
            result[key] = value



    def test_tour1(self):
        tour1 = r_and_t.Tournament(90, self.runner1, self.runner3)
        self.all_result = tour1.start()
        self.assertTrue(self.all_result[2] == 'Ник')

    def test_tour2(self):
        tour1 = r_and_t.Tournament(90, self.runner2, self.runner3)
        self.all_result = tour1.start()
        self.assertTrue(self.all_result[2] == 'Ник')


    def test_tour3(self):
        tour1 = r_and_t.Tournament(90, self.runner1,self.runner2, self.runner3)
        self.all_result = tour1.start()
        self.assertTrue(self.all_result[3] == 'Ник')