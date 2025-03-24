class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [-1]*n
        for i in range(n):
            divisibleBy3 = (i+1)%3==0
            divisibleBy5 = (i+1)%5==0
            elem = ""
            if divisibleBy3:
                elem = elem + "Fizz"
            if divisibleBy5:
                elem = elem + "Buzz"
            if elem=="":
                elem = f"{i+1}"
            arr[i] = elem
        return arr
