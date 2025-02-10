#Khoa Duong
#Assignment 3
#Write a program ask for user expenses and the catagory then print out calculated of the expenses.
#1. Import function tool "reduce" because it is a bult-in function in python and get expenses.
#2. Write a main funcion to calculate expenses using lambda funtion with reduce().
#3. print out result.

#Import reeduce because it is not bult in of python.
from functools import reduce

#Write a function to get expenses.
def get_expenses():
    #store expenses as a list.
    expenses = []
    while True:
        expenses_type = input ("Enter your expenses catagory or (done) when finish:")
        if expenses_type.lower()== 'done':
            break
        #Get the expenses amount.
        try:
            amount = float(input(f'Enter the amount for {expenses_type}:'))
            #Add amount and expenses cat to the list.
            expenses.append((expenses_type, amount))
        except ValueError:
            print('Please enter valid input amount.')
    return expenses

#Write the main function.
def main():
    #store the returned list.
    expenses = get_expenses()

    if not expenses:
        print ('No expenses entered.')
        return

    #Lambda function using reduce().
    total_expenses = reduce(lambda acc, item: acc + item[1], expenses, 0)
    highest_expenses = reduce(lambda a,b: a if a[1] > b[1] else b, expenses)
    lowest_expenses = reduce(lambda a,b: a if a[1] < b[1] else b, expenses)

    #Print out the result.
    print(f'Your total expenses is ${total_expenses}.')
    print(f'Your highest expenses is {highest_expenses[0]}: ${highest_expenses[1]:.2f}')
    print(f'Your lowest expenses is {lowest_expenses[0]}: ${lowest_expenses[1]:.2f}')

#call the main function.
if __name__== '__main__':
    main()
