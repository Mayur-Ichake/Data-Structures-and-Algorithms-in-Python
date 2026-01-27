
'''count = 0
def func(n, count):

    if n == 0:
        return
    
    count += 1
    print(count)
    func(n-1,count)

func(9 , count)'''

def func(n):

    if n == 0:
        return 
    
    print(n)
    func(n-1)

func(10)