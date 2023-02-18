print("\nWelcome To My Tips Calculator\n")

bill = float(input("What is your total bill?\n$"))
percentage = float(input("What Percentage of Your Bill Would You Like to Give as Tip?\n$"))/100
people = int(input("How Many People To Split The Tips?\n"))

tips = (bill * percentage) / people

print(f'Per Person Should Pay\n${"{:.2f}".format(round(tips,2))}')