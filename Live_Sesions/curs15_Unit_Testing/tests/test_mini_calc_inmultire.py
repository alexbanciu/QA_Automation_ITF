from app.mini_calc import Mini_Calc


class TestMiniCalcInmultire():
    def setup_method(self):
        print("INMULTIRE - Instructiune executata la inceput!")
        self.calc = Mini_Calc()
        # daca punem self aici, noi facem din variabila `calc` un atribut de clasa
        # daca nu punem self aici, atunci `calc` e vizibil doar in  cadrul metodei setup_method()

    def teardown_method(self):
        print("INMULTIRE - Instructiune executata la final!")

    # !!!!!ATENTIE, toate metodele de test trebuie sa inceapa cu test_
    def test_inmultire(self):
        assert self.calc.inmultire(2, 3) == 6, 'Eroare...Nu functioneaza cum trebuie!'

    def test_inmultire1(self):
        assert self.calc.inmultire(-2, 3) == -6, 'Eroare...Nu functioneaza cum trebuie!'

    def test_inmultire2(self):
        assert self.calc.inmultire(-2, -3) == 6, 'Eroare...Nu functioneaza cum trebuie!'

    def test_inmultire3(self):
        assert self.calc.inmultire(2, 0) == 0, 'Eroare...Nu functioneaza cum trebuie!'

    def test_inmultire4(self):
        assert self.calc.inmultire(-2, 0) == 0, 'Eroare...Nu functioneaza cum trebuie!'