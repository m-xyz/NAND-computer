#!/usr/bin/env python

class Gate(object):

    def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    def xor_gate(self):

        b = 0
        for bit in self.__dict__.values():
            if(bit): b += 1
            if(b > 1): return 0

        return b

    def and_gate(self):

        for i in self.__dict__.values():
            if not i: return 0

        return 1

    def or_gate(self):
        
        for i in self.__dict__.values():
            if i: return 1

        return 0

    def not_gate(self, r): return not r

    def nand_gate(self): return self.not_gate(self.and_gate())


a = 0
b = 0
c = 0
d = 0
e = 1
x = 0
y = 0
z = 0



g = Gate(a=a,b=b,c=c,d=d,e=e,x=x,y=y,z=z)
nand = Gate(a=a,b=b,c=c,d=d,e=e,x=x,y=y,z=z).nand_gate()


fake_and = Gate(a=nand,b=nand,c=nand,d=nand,e=nand,x=nand,y=nand,z=nand).nand_gate()
fake_or = Gate(a=Gate(a=a).nand_gate(), b=Gate(b=b).nand_gate(), c=Gate(c=c).nand_gate(), d=Gate(d=d).nand_gate(), e=Gate(e=e).nand_gate(), x=Gate(x=x).nand_gate(), y=Gate(y=y).nand_gate(), z=Gate(z=z).nand_gate()).nand_gate()

print('\nReal AND:',g.and_gate(),'\nFake AND:', int(fake_and),'\n----------------')
print('Real OR:',g.or_gate(),'\nFake OR:', int(fake_or),'\n----------------')
print('\t[',(g.and_gate() == fake_and) and (g.or_gate() == fake_or),']')

for k, v in g.__dict__.items(): print(k,v)


