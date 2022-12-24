class Solution:
    def fizzBuzz(self, n):
        ls=[]
        for n in range(1,n+1):
            if n%3==0:
                ls.append('Fizz')
                # print('Fizz')
                continue
            elif n%5==0:
                # print('Buzz')
                ls.append('Buzz')
                continue
            elif n%3 and n%5==0:
                # print('FizzBuzz')
                ls.append('FizzBuzz')
                continue
            else:
                print(n)
                ls.append(n)
                continue
        return ls
sl=Solution()
sl.fizzBuzz(5)
