from app.mini_calc import Mini_Calc


class TestMiniCalcImpartire():
    def setup_method(self):
        print("INMULTIRE - Instructiune executata la inceput!")
        self.calc = Mini_Calc()
        # daca punem self aici, noi facem din variabila `calc` un atribut de clasa
        # daca nu punem self aici, atunci `calc` e vizibil doar in  cadrul metodei setup_method()

    def teardown_method(self):
        print("INMULTIRE - Instructiune executata la final!")

    # !!!!!ATENTIE, toate metodele de test trebuie sa inceapa cu test_
    def test_impartire(self):
        assert self.calc.impartire(6, 3) == 2, 'Eroare...Nu functioneaza cum trebuie!'

    def test_impartire1(self):
        assert self.calc.impartire(-6, 3) == -2, 'Eroare...Nu functioneaza cum trebuie!'

    def test_impartire2(self):
        assert self.calc.impartire(-6, -3) == 2, 'Eroare...Nu functioneaza cum trebuie!'

    def test_impartire3(self):
        assert self.calc.impartire(6, -3) == -2, 'Eroare...Nu functioneaza cum trebuie!'
