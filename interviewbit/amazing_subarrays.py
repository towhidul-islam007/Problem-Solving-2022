class Solution:
    # @param A : string
    # @return an integer
    vowels = set(
        [
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U' 
        ]
    )

    def solve(self, A):
        cnt, MOD = 0, 10003
        for index, ch in enumerate(A):
            if ch in self.vowels:
                cnt = (cnt + len(A) - index) % MOD

        return cnt


A = 'ABEC'
print(Solution().solve(A))
