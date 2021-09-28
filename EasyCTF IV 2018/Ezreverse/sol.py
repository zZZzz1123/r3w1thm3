from z3 import *
  

flag = []
s = Solver() # Khoi tao solver
f0 = BitVec('f0',8) # Khoi tao cac bien cho solver ung voi voi ki tu trong flag
f1 = BitVec('f1',8)
f2 = BitVec('f2',8)
f3 = BitVec('f3',8)
f4 = BitVec('f4',8)

flag.append(f0) # Them cac bien nay vo mang de goi ra
flag.append(f1)
flag.append(f2)
flag.append(f3)
flag.append(f4)

s.add(f1 + 2 == 53) # v5 = 53
s.add(f0 + 1 == f4 + 5 - 10) # v4 = v7 - 10
s.add(f4 + 5 == 0x6f + 3) # HI(v6) =  f8[4] + 5
s.add(f2 + 3 == 0x7D) # LODWORD(v6) = v8[2] + 3
s.add(f3 + 4 == 0x6f) #HIDWORD(v6) = v8[3] + 4
if(s.check()): # Kiem tra dieu kien
    results = s.model() # Tim kiem cac gia tri
    print(results)
    string_flag = ''
    for i in flag:
        string_flag += chr(results.evaluate(i).as_long())
    print(string_flag)
