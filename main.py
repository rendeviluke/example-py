def sum(x: float, y: float) -> float:
    return x + y


def sub(x: float, y: float) -> float:
    return x - y


def mul(x: float, y: float) -> float:
    return x * y


def div(x: float, y: float) -> float:
    return x / y


number_one = input("Type a number: \n")
number_two = input("Type another number: \n")
operator = input("Choose one operator: [+] [-] [*] [/]\n")

try:
    number_one = float(number_one)  # type: ignore
    number_two = float(number_two)  # type: ignore
except Exception as error:
    print(f'Error: {error}')

match operator:
    case '+':
        result = sum(number_one, number_two)  # type: ignore
        print(f'{number_one} plus {number_two} equals {result}')

    case '-':
        result = sub(number_one, number_two)  # type: ignore
        print(f'{number_one} minus {number_two} equals {result}')

    case '*':
        result = mul(number_one, number_two)  # type: ignore
        print(f'{number_one} times {number_two} equals {result}')

    case '/':
        result = div(number_one, number_two)  # type: ignore
        print(f'{number_one} divided by {number_two} equals {result}')
