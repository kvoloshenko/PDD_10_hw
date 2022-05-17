from loto_game.player import Player

class TestPlayer:

    def test_card(self):
        p = Player()
        c = p.get_card()
        assert str(type(c)) == "<class 'loto_game.Card.Card'>"

    def test_default_type(self):
        p = Player()
        assert p.get_type() == 'Human'

    def test_set_type(self):
        p = Player()
        type = 'Test_type'
        p.set_type(type)
        assert p.get_type() == type

    def test_name(self):
        p = Player()
        name = 'Test_name'
        p.set_name(name)
        assert p.get_name() == name