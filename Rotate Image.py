class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    
    def swap(self, matrix , p1 , p2):
        si = p1[0]
        sj = p1[1]
        ei = p2[0]
        ej = p2[1]
        tmp = matrix[si][sj]
        matrix[si][sj] = matrix[ei][ej]
        matrix[ei][ej] = tmp
    
    def rotate(self, matrix):
        r = len(matrix)
        if r <= 1:
            return matrix
        offset = 0
        for l in range(r , 1 , -2):
            for i in range(0 , l - 1):
                p1 = (offset + i , offset)
                p2 = (r - 1 - offset , offset + i)
                p3 = (r - 1 - offset - i , r - 1 - offset)
                p4 = (offset , r - 1 - offset - i)
                
                self.swap(matrix , p1 , p2)
                self.swap(matrix , p2 , p3)
                self.swap(matrix , p3 , p4)
            offset += 1
        return matrix