import operator
ops = { "+": operator.add, "-": operator.sub,  '*' : operator.mul,
        "/" : operator.div,
        '%' : operator.mod,
        '^' : operator.xor, }

s = []

A = ["1","3","+","3","*"]
for i in A:
	if i.isdigit():
	    s.append(i)
	elif len(s) >1:
	    temp = ops[i](int(s.pop()),int(s.pop()))
	    s.append(str(temp))
            
print s.pop()
