from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1 - teste:
def test_ingredient():
    "Verifica se retorna hashes iguais para ingredientes iguais"
    ingrediente1 = Ingredient("tomate")
    ingrediente2 = Ingredient("farinha")
    ingrediente3 = Ingredient("tomate")
    ingrediente2_restrictions = {Restriction.GLUTEN}

    assert ingrediente1 == ingrediente3
    assert ingrediente1.__hash__() == ingrediente3.__hash__()

    "Verifica se retorna hashes diferentes para ingredientes diferentes"
    assert ingrediente1.__hash__() != ingrediente2.__hash__()

    "Verifica se retorna True para comparação de dois ingredientes iguais"
    assert ingrediente1.__repr__() == ingrediente3.__repr__()

    "Verifica se retorna False para comparação de dois ingredientes diferentes"
    assert ingrediente1.__repr__() != ingrediente2.__repr__()

    "Verifica se retorna o valor correto ao acessar o método __repr__"
    assert ingrediente1.__repr__() == "Ingredient('tomate')"

    "Verifica se o atributo name retorna o nome correto"
    assert ingrediente1.name == 'tomate'

    "Verifica se o atributo restrictions retorna os valores corretos"
    assert ingrediente2.restrictions == ingrediente2_restrictions
