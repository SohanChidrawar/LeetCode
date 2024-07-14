class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def winner(n):
            if(n==1):
                return 0
            else:
                return (winner(n-1)+k)%n
        return winner(n)+1
