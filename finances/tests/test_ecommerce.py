# PD6 2 - test ecommerce

# Import libraries
from finances.ecommerce import calculate_rabat, calculate_brutto, calculate_netto

# Declare function(s)


# Prepare tests
def test_calculate_brutto():
    assert calculate_brutto(77) == 100
    assert calculate_brutto(0) == 0
    assert calculate_brutto(123, 1) == -1
    assert calculate_brutto(123, 5) == -1


def test_calculate_netto():
    assert calculate_netto(100) == 77
    assert calculate_netto(0) == 0
    assert calculate_netto(123, 1) == 0
    assert calculate_netto(123, 5) == -1


def test_calculate_rabat():
    assert calculate_rabat([0.1]) == 0.9
    assert calculate_rabat([0.1, 0.1]) == 0.81
    assert calculate_rabat([0, 0.5, 0.5]) == 0.25
    assert calculate_rabat([1, 0.5]) == 0
    assert calculate_rabat([]) == 1
    assert calculate_rabat([0.2, 2, 0.2]) == -1
