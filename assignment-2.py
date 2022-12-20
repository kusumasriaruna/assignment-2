import pandas as pd

Series1 = pd.Series([1, 2, 3, 4, 5])
Series2 = pd.Series([6, 7, 8, 9, 10])

print(Series1)
print(Series2)
s1 = Series1 + Series2

print(s1)

s2 = Series1 - Series2
print(s2)

s3 = Series1 * Series2
print(s3)

s4 = Series1 / Series2
print(s4)

print("Addition is:",s1)
print("Subtraction is:",s2)
print("Multiplication is:",s3)
print("Division is:",s4)