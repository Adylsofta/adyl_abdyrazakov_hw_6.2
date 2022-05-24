def say_hello(): return 'Hello'


def say_bye(): return 'Bye'


message = say_hello()
# вызов функции say_hello  присваивание результата переменной
message = say_hello
# присваивание функции say_hello к переменной
message = say_bye

print(message)
print(say_hello())


def sum(num1, num2): return num1 + num2


def multiply(num1, num2): return num1 * num2


def divide(num1, num2): return num1 / num2


def subract(num1, num2): return num1 - num2


def difficult_func(num1, num2):
    num1 = num1 * 2
    num2 = num2 / 2
    return num1 + num2


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f'Result: {result}')


do_operation(2, 4, sum)
do_operation(2, 4, multiply)


def select_operation(choice):
    if choice == 1:  # "1" == 1
        return sum
    elif choice == 2:
        return multiply
    else:
        return divide
