
print("===== SMART CANTEEN =====")

# Taking bill amount from customer
try:
    bill_amount = float(input("Enter your total bill amount (Rs.): "))

    # Improvement 1: Check invalid bill
    if bill_amount <= 0:
        print("Invalid Bill! Please enter an amount greater than zero.")

    else:
        # Regular discount calculation
        if bill_amount >= 3000:
            discount_rate = 20
        elif bill_amount >= 2000:
            discount_rate = 10
        elif bill_amount >= 1000:
            discount_rate = 5
        else:
            discount_rate = 0

        # Improvement 2: Membership discount
        membership = input("Do you have a membership card? (Yes/No): ").strip().lower()

        # Improvement 3: Validate membership input
        while membership not in ["yes", "no"]:
            print("Invalid input! Please enter Yes or No.")
            membership = input("Do you have a membership card? (Yes/No): ").strip().lower()

        # Calculate discounts
        discount_amount = bill_amount * discount_rate / 100

        if membership == "yes":
            membership_discount = bill_amount * 5 / 100
        else:
            membership_discount = 0

        total_savings = discount_amount + membership_discount
        final_amount = bill_amount - total_savings

        # Display bill summary
        print("\n===== BILL SUMMARY =====")
        print(f"Original Bill: Rs. {bill_amount:.2f}")
        print(f"Regular Discount: {discount_rate}%")
        print(f"Regular Discount Amount: Rs. {discount_amount:.2f}")
        print(f"Membership Discount Amount: Rs. {membership_discount:.2f}")
        print(f"Total Savings: Rs. {total_savings:.2f}")
        print(f"Final Payable: Rs. {final_amount:.2f}")

        # Improvement 4: Savings message
        if total_savings > 0:
            print(f"\nCongratulations! You saved Rs. {total_savings:.2f}")
        else:
            print("\nNo discount applied. Thank you for shopping!")

except ValueError:
    print("Invalid input! Please enter a numeric bill amount.")
