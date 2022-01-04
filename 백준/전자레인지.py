A = int(300)
B = int(60)
C = int(10)

minute = int(input())
A_number = 0
B_number = 0
C_number = 0

if minute > 10000:
    print(-1)
else:
    if A<= minute:
        A_number = minute//A
        minute = minute%A
    if B<= minute:
        B_number = minute//B
        minute = minute%B
    if C<= minute:
        C_number = minute//C
        minute = minute%C
    if minute == 0:
        print(A_number, B_number, C_number)
    else:
        print(-1)