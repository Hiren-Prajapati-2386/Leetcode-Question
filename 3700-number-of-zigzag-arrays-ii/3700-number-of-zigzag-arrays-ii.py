class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        # Base edge-cases
        if n <= 0 or k <= 0:
            return 0
        if n == 1:
            return k % MOD
            
        
        initial_state = [j for j in range(k)] + [(k - 1 - j) for j in range(k)]
        
        dim = 2 * k
        
        
        def multiply(A, B):
            C = [[0] * dim for _ in range(dim)]
            for i in range(dim):
                for mid in range(dim):
                    if A[i][mid] == 0: 
                        continue
                    for j in range(dim):
                        C[i][j] = (C[i][j] + A[i][mid] * B[mid][j]) % MOD
            return C

        
        def power(matrix, p):
            res = [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
            base = matrix
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

      
        M = [[0] * dim for _ in range(dim)]
        
        for i in range(k):
            for j in range(i):
                M[i][k + j] = 1  
                
        for i in range(k):
            for j in range(i + 1, k):
                M[k + i][j] = 1  
                
        
        if n > 2:
            M_pow = power(M, n - 2)
            final_state = [0] * dim
            for i in range(dim):
                s = 0
                for j in range(dim):
                    s = (s + M_pow[i][j] * initial_state[j]) % MOD
                final_state[i] = s
        else:
            final_state = initial_state
            
        return sum(final_state) % MOD
