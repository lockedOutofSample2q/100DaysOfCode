def add(n1,n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,   
    "/": div
}



def calc(do_continue):
   
    while do_continue == 'y':
        if num1== None:
            num1 = float(input("Enter the first number: "))
       
        op= input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        print(f"{num1} {op} {num2} = {operations[op](num1,num2)}")
        num1 = operations[op](num1,num2)
        do_continue = input(f"Do you want to continue with {num1}  (y/n): ").lower()
        if do_continue == 'n':
            do_continue = 'y'
            calc(do_continue)
do_continue='y'
calc(do_continue)