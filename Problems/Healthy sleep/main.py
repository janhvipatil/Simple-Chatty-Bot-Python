A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
    print("Normal")
else:
    if H > B:
        print("Excess")
    else:
        print("Deficiency")
