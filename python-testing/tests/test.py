def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

def test_calculate_total_with_empty_list():
    print("Testing with empty list")
    assert calculate_total([]) == 0, "Expected total to be 0 for empty list"
    
def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook",
            "price": 5
        }
    ]
    assert calculate_total(products) == 5, "Expected total to be 5 for single product"
    
def test_calculate_total_with_multiple_products():
    products = [
        {
            "name": "Notebook",
            "price": 5
        },
        {
            "name": "Pen",
            "price": 2
        }
    ]
    assert calculate_total(products) == 7, "Expected total to be 7 for multiple products"
    
if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_products()
    print("All tests passed!")

    print("Test passed!")