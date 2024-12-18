import re
import math

def format(puzzle):
    registers, instructions = puzzle.split("\n\n")

    i = re.findall('\d',instructions)
    a, b, c = [int(i) for i in re.findall(r'\d+',registers)]
    i = [int(i) for i in re.findall(r'\d',instructions)]
    return ((a,b,c),i)

class Device:
    def adv(self,op):
        numerator = self.a
        denominator = 2 ** self.combo[op]()
        self.a = math.trunc(numerator / denominator)

    def bxl(self,op):
        self.b = self.b ^ op 
    
    def bst(self,op):
        self.b = self.combo[op]() % 8

    def jnz(self,op):
        if self.a != 0:
            self.instruction_pointer = op

    def bxc(self,op):
        self.b = self.b ^ self.c

    def out(self,op):
        self.result.append(self.combo[op]() % 8)

    def bdv(self,op):
        numerator = self.a
        denominator = 2 ** self.combo[op]()
        self.b = math.trunc(numerator / denominator)

    def cdv(self,op):
        numerator = self.a
        denominator = 2 ** self.combo[op]()
        self.c = math.trunc(numerator / denominator)

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def crash(self):
        print(f"situation critical!")

    def __init__(self,a,b,c,instructions):
        #print(f"initializing device with: a={a}, b={b}, c={c}")
        self.a, self.b, self.c, = a, b, c
        self.instruction_pointer = 0
        self.instructions = instructions
        self.opcodes = {
                0: self.adv,
                1: self.bxl,
                2: self.bst,
                3: self.jnz,
                4: self.bxc,
                5: self.out,
                6: self.bdv,
                7: self.cdv
                }

        self.combo = {
                0: (lambda : 0),
                1: (lambda : 1),
                2: (lambda : 2),
                3: (lambda : 3),
                4: self.get_a,
                5: self.get_b,
                6: self.get_c,
                7: self.crash,
                }
        self.result = []

        while self.instruction_pointer < len(self.instructions) - 1:
            #print(f"instruction pointer: {self.instruction_pointer}:{self.instructions[self.instruction_pointer]}, operand: {self.instruction_pointer + 1}:{self.instructions[self.instruction_pointer + 1]}")
            last = self.instruction_pointer
            self.opcodes[self.instructions[self.instruction_pointer]](self.instructions[self.instruction_pointer +1])


            if self.instruction_pointer == last:
                self.instruction_pointer += 2
        print(self.result)

def part1(encoding):
    elf_device = Device(encoding[0][0],encoding[0][1],encoding[0][2],encoding[1])


if __name__ == "__main__":
    test_file = open("test1.txt",'r')
    test_data = test_file.read()
    test_file.close()

    print(f"part1 format: {format(test_data)}")

    print(f"part1 test: {part1(format(test_data))}")

    input_file = open("input1.txt",'r')
    input_data = input_file.read()
    input_file.close()

    print(f"part1 test: {part1(format(input_data))}")

