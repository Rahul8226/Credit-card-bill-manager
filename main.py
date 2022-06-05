months = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}

# Empty List for Transactions
transactions = []
bill_pay = []
fix_amount = 0


def paid_amount():
    if transactions[len(transactions)-1]["dues"] < fix_amount:
        amt = transactions[len(transactions)-1]["dues"]
        print("Amount paid.. \u20b9", transactions[len(transactions)-1]["dues"])
    else:
        amt = fix_amount
        print("Amount paid.. \u20b9", fix_amount)
    
    transactions[len(transactions)-1]["paid"] = amt + transactions[len(transactions)-1]["paid"]
    if transactions[len(transactions)-1]["dues"] >= fix_amount:
        transactions[len(transactions)-1]["dues"] = transactions[len(transactions)-1]["dues"] - fix_amount
    else:
        transactions[len(transactions)-1]["dues"] = 0
    
    print("Remaining Bill \u20b9", transactions[len(transactions)-1]["dues"])


def transact_amount(amount):
    if len(transactions) == 0:
        transaction_record = {
            "month": 0,
            "amount": amount,
            "charges": amount * 0.10,
            "total": amount + amount * 0.10,
            "paid": 0,
            "dues": amount + amount * 0.10,
        }
        transactions.append(transaction_record)
    else:
        transaction_record = {
            "month": transactions[len(transactions)-1]["month"]+1,
            "amount": amount,
            "charges": amount * 0.10,
            "total": amount + amount * 0.10,
            "paid": 0,
            "dues": (amount + amount * 0.10) + transactions[len(transactions)-1]["dues"],
        }
        transactions.append(transaction_record)

    print("Amount Transacted \u20b9", amount)


def show_transaction_history():
    for transaction in transactions:
        print("-"*30)
        print("Month: {}".format(months[transaction["month"]]))
        print("Transacted Amount: \u20b9{amount}"
              "\nBilling Amount: \u20b9{total}\nBill Paid: \u20b9{paid}\nTotal Dues: \u20b9{dues}".format_map(transaction))
        print("-" * 30)
        print()


def set_fix_amount(amount):
    global fix_amount
    fix_amount = amount
    print("We have Set a Fix Amount of \u20b9", fix_amount)


def payment():
    if len(transactions) == 0:
        print("Bill amount: \u20b9 0")
    else:
        payment_record = {
            "month": transactions[len(transactions)-1]["month"],
            "bill": transactions[len(transactions)-1]["dues"],
            "payment": fix_amount,
            "dues": transactions[len(transactions)-1]["dues"] - fix_amount,
        }
        bill_pay.append(payment_record)
    
    paid_amount()

    


def time_taken():
    # print(exp)
    if transactions[len(transactions)-1]["dues"] == 0:
        print("All Dues Cleared.")
    elif ((transactions[len(transactions)-1]["dues"]/fix_amount)-(transactions[len(transactions)-1]["dues"]//fix_amount))==0:
        print("Remaining Bill will be cleared in next {} months.".format(int(transactions[len(transactions)-1]["dues"]//fix_amount)))
    else:
        print("Remaining Bill will be cleared in next {} months.".format(int(transactions[len(transactions)-1]["dues"]//fix_amount)+1))



def show_welcome_message():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to CredManager")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please Read the Instruction Menu and Enter Your Choice")
    print("[1] Enter Fixed Minimum Amount Payable Every Month")
    print("[2] Transact Any Amount")
    print("[3] Make a Payment. (Fixed Amount will be deducted automatically)")
    print("[4] Transaction History")
    print("[5] Quit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def make_choice():
    while(1):
        while(1):
            choice = int(input("Enter Your Choice[1-5]: "))
            if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
                break
        if choice == 1:
            amount = int(input("Enter a Fix Amount to be paid every month: "))
            set_fix_amount(amount)
        elif choice == 2:
            amount = int(input("Enter Transaction Amount: "))
            transact_amount(amount)
            payment()
            time_taken()
        elif choice == 3:
            # amount = 3000
            payment()
            time_taken()
        elif choice == 4:
            show_transaction_history()
        else:
            exit(0)



if __name__ == '__main__':
    amount = int(input("Enter a Fix Amount to be paid every month: "))
    set_fix_amount(amount)
    show_welcome_message()
    make_choice()
