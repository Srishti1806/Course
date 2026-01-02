from app import calculate_final_price, classify_product
def test_final_price():
    assert calculate_final_price(10000, 10) == 9000.0


def test_classification():
    assert classify_product(12000) == "Premium"
    assert classify_product(7000) == "Standard"
    assert classify_product(3000) == "Budget"
    assert classify_product(1500) == "Economy"
