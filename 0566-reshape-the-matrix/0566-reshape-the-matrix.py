import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat
                
        a = np.array(mat)

        a = a.reshape(r,c)


        return a.tolist()