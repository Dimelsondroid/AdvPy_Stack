
class Stacker:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def checker(string):

    if len(string) % 2 != 0 or string[0] in ')]}' or string[-1] in '([{':
        return 'Unballanced by parity'

    openings = set('([{')
    match = {('(', ')'), ('[', ']'), ('{', '}')}

    for item in string:
        if item in openings:
            balancer.push(item)
        else:
            latest_item = balancer.pop()
            if (latest_item, item) not in match:
                return 'Unballanced by Match'

    return balancer.is_empty()


if __name__ == '__main__':
    parentheses = '[[{())}]'
    balancer = Stacker()
    res = checker(parentheses)
    if res == True:
        print('Ballanced')
    else:
        print(res)
