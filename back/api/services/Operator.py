from api.services import calculate

operations = {
    '+': calculate.add,
    '*': calculate.multiply,
    '-': calculate.subtract,
    '/': calculate.divide,
}


def parseFloat(numbers):
    try:
        return [float(numbers[0]), float(numbers[1])]
    except ValueError:
        raise Exception('Введите цифры')


class Operator:
    def __init__(self, operation):
        try:
            self.operation = operations[operation]
        except KeyError:
            raise Exception('Неправильный оператор')

    def calc(self, numbers):
        return self.operation(parseFloat(numbers))
