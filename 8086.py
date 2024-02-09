class Stack:

    def __init__(self, size):
        self._stack = RAM(size)
        self._sp = 0

    def pop(self):
        self._sp += 2
        return self._stack.read(self._sp -2, 8)

    def push(self, item):
        self._sp -= 2
        self._stack.append(item)


class RAM:
    def __init__(self, size):
        self._memory = [0] * size

    def read(self, address, length):
        return self._memory[address:address + length]

    def read_b(self, address):
        return self._memory[address]

    def write(self, address, value):
        for e in range(address,address + len(value)):
            self._memory[e] = value[e]

    def write_b(self, address, byte):
        self._memory[address] = byte

r = RAM(128)
r.write_b(0, 0x01)
r.write_b(1, 0x0)
r.write_b(2, 0x20)

d = r.read(0,3)
print(d)




