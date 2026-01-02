import sys

def calculate_final_price(price, discount):
    return price - (price * discount / 100)


def classify_product(final_price):
    if final_price > 10000:
        return "Premium"
    elif 5000 <= final_price <= 9999:
        return "Standard"
    elif 2000 <= final_price <= 4999:
        return "Budget"
    else:
        return "Economy"


def main():
    # Command-line arguments
    product_id = sys.argv[1]
    product_name = sys.argv[2]
    category = sys.argv[3]
    price = float(sys.argv[4])
    discount = float(sys.argv[5])

    final_price = calculate_final_price(price, discount)
    classification = classify_product(final_price)

    print("\n--- Product Details ---")
    print("Product ID:", product_id)
    print("Product Name:", product_name)
    print("Category:", category)
    print("Final Price: ₹", final_price)
    print("Classification:", classification)


if __name__ == "__main__":
    main()
