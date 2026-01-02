def calculate_final_price(price, discount):
    final_price = price - (price * discount / 100)
    return final_price


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
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    discount = float(input("Enter Discount (%): "))

    final_price = calculate_final_price(price, discount)
    classification = classify_product(final_price)

    print("\n--- Product Details ---")
    print("Product ID:", product_id)
    print("Name:", product_name)
    print("Category:", category)
    print("Final Price: ₹", final_price)
    print("Classification:", classification)


if __name__ == "__main__":
    main()
