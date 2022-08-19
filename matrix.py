'''
pass
'''

class Matrix:
    '''
    pass
    '''
    def __init__(self, matrix_string):
        '''
        pass
        '''
        self.matrix = matrix_string
        print(matrix_string + '\n')

    def row(self, index = int):
        '''
        pass
        '''
        index -= 1
        ints_row = []
        matrix_separate = self.matrix.split('\n')
        matrix_row = matrix_separate[index].split(' ')
        for num in matrix_row:
            ints_row.append(int(num))
        return ints_row

    def column(self, index = int):
        '''
        pass
        '''
        index -= 1
        matrix_column = []
        matrix_separate = self.matrix.split('\n')
        column_count = self.matrix.count('\n') + 1
        i = 0
        while i < column_count:
            matrix_column.append(int(matrix_separate[i].split(' ')[index]))
            i += 1
        return matrix_column

caioba = Matrix('1 2 3 5 1 1 1\n4 5 6 1 1 1 1\n7 8 9 10 9 8 7\n1 2 3 4 5 6 7')
print(caioba.column(1))
print(caioba.row(2))
