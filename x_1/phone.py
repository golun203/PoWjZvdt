class phone:
    def __init__(self, p = 0, c = 0, s = 0):
        self.p = p
        self.c = c
        self.s = s


class Google_phone(phone):
    lst = list()
    lst_i = list()
    lst_a = 0
    def __init__(self):
        self.p = 10
        self.c = 3
        self.s = 5
        print('Phone specifications :')
        print('price:', self.p)
        print('camera_count:', self.c)
        print('screen_size:', self.s)
    def special_freature(self):
        self.lst_i = input('Enter a list of integar numbers separated by space: ')
        l = self.lst_i.split()
        for i in l:
            try:
                self.lst_a = int(i)
            except:
                print('not a number or integar')
                quit()

            if self.lst_a%2 == 0 and self.lst_a > 10:
                self.lst.append(self.lst_a)

        ans = sorted(self.lst, reverse = True)
        print(ans)

class Taiwan_phone(phone):
    n = 0
    a = 0
    def __init__(self):
        self.p = 20
        self.c = 1
        self.s = 3
        print('Phone specifications :')
        print('price:', self.p)
        print('camera_count:', self.c)
        print('screen_size:', self.s)
    def special_freature(self):
        try:
            self.n = int(input('Enter a integar number: '))
        except:
            print('not a integar')

        def fibo(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fibo(n-1) + fibo(n-2)
        a = str(fibo(self.n))

        from math import factorial
        def calc_arrangement(x,y):
            print(factorial(x) / factorial(x - y))

        x = int(a[(len(a)-2)])
        y = int(a[(len(a)-1)])
        if x > y :
            calc_arrangement(x,y)
        else:
            print('cant caculate')

test = phone()
test1 = Google_phone()
test1.special_freature()
test2 = Taiwan_phone()
test2.special_freature()
