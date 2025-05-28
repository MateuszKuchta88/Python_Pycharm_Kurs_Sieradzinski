# PD6 2 - test budget

# Import libraries
from finances.budget import calculate_expences

# Declare function(s)

# Prepare tests
def test_calculate_expences():
    assert calculate_expences(["glass", "fan", "plate"]) == 12.7
    assert calculate_expences([]) == 0
    assert calculate_expences(["plate"]) == 4.35
    assert calculate_expences(["plate", "fan", "plate"]) == 14.9
    assert calculate_expences(["flowers"]) == "There is sth wrong in your basket. We don't have flowers in our store"
    assert calculate_expences(["glass", "glass", "duck"]) == "There is sth wrong in your basket. We don't have duck in our store"
