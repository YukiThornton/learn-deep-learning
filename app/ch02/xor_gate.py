from . import and_gate, or_gate, nand_gate

def XOR(x1, x2):
    s1 = nand_gate.NAND(x1, x2)
    s2 = or_gate.OR(x1, x2)
    y = and_gate.AND(s1, s2)
    return y

def print_xor():
    print("XOR(0, 0): " + str(XOR(0, 0)))
    print("XOR(0, 1): " + str(XOR(0, 1)))
    print("XOR(1, 0): " + str(XOR(1, 0)))
    print("XOR(1, 1): " + str(XOR(1, 1)))
