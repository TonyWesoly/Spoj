def gray(n,tab,k,direction):
    if n == k:
        print("".join(tab))
        return
    if direction==1:
        gray(n,tab+['0'],k+1,1)
        gray(n,tab+['1'],k+1,0)
    else:
        gray(n,tab+['1'],k+1,1)
        gray(n,tab+['0'],k+1,0)

number_of_tests = int(input())
for i in range(number_of_tests):
    test = int(input())
    gray(test,[],0,1)