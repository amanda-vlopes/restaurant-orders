from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish('mac and cheese', 10.5)
    dish2 = Dish('risotto', 15.0)
    dish3 = Dish('mac and cheese', 10.5)

    ingredient_dish1 = Ingredient('queijo parmesão')
    ingredient_dish1_restrictions = {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE}

    "Verifica se o atributo name de um prato é igual ao passado ao construtor"
    assert dish1.name == 'mac and cheese'

    "Verifica se os hashes de dois pratos iguais são iguais"
    assert dish1.__hash__() == dish3.__hash__()

    "Verifica se os hashes de dois pratos diferentes são diferentes"
    assert dish1.__hash__() != dish2.__hash__()

    "Verifica a igualdade de dois pratos iguais"
    assert dish1 == dish3

    "Verifica a diferença entre dois pratos diferentes"
    assert dish1 != dish2

    "Verifica se o retorno do método __repr__ está correto"
    assert dish1.__repr__() == "Dish('mac and cheese', R$10.50)"

    "Verifica se é lançado TypeError ao criar um prato com um tipo inválido"
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('pasta', '5')

    "Verifica se é lançado ValueError ao criar um prato com um valor inválido"
    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish('pasta', 0)

    "Verifica se o retorno do acesso do atributo recipe está correto"
    dish1.add_ingredient_dependency(ingredient_dish1, 2)
    assert dish1.recipe.get(ingredient_dish1) == 2

    "Verifica se o retorno do método get_restrictions está correto"
    assert dish1.get_restrictions() == ingredient_dish1_restrictions

    "Verifica se o retorno do método get_ingredients está correto"
    assert dish1.get_ingredients() == {Ingredient('queijo parmesão')}
