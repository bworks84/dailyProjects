def main():
    print("This program converts USD to Pounds Sterling")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print("That is ", pounds, " pounds. ")


def convert_to_pounds(dollars): return dollars * 0.89


main()
