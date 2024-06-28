import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
digits = "0123456789"
symbols = "()[]{},:;\|.-_/#@*"

upper, lower, nums, syms = True, True, True, True

all=""

if upper:
    all += uppercase
if lower:
    all += lowercase
if nums:
    all += digits
if syms:
    all += symbols

length=int(input("Length:"))
amount= int(input("Amount:"))

for x in range (amount):
    password = "".join(random.sample(all, length))
    print(password)


