class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n=str(n)
        if len(n) == 1:
            return n
        return self.reverseBits(n[1:])+n[0]
my_solution=Solution()
print(my_solution.reverseBits('00000010100101000001111010011100'))