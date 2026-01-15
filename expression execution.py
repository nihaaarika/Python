# String $ numeric value can operate together with *
A,B=2,3
Txt=("@")
print(A*Txt*B)

# String and string can operate with +
A,B=("6",7)
Txt="@"
print((A+Txt)*B)

# Numerical value can operate with all arithmetic operator
A,B=9,6
C=4
print(A+B*C)

# Arithmetic expression with integer and float with result in float
A,B=5,4.8
C=A*B
print(C)

# Result of division operator with two integes will be float
A,B=7,3
C=(A/B)
print(C)

# Integer division with float and int will give int displayed as float
A,B=5,6.7
C=A//B
print(C,A/B)
