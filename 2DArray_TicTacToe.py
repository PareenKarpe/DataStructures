class Solution(object):

    #
    def diagonal2(self, turn, P, b):
        win = True
        n = len(b)

        for x in range(n):

            if b[x][n - 1 - x] != turn:
                win = False
        return win

    def diagonal(self, turn, P, b):
        win = True

        n = len(b)

        for x in range(n):

            if b[x][x] != turn:
                win = False

        return win

    def horizontal(self, turn, P, b):
        print("**")
        win = True
        n = len(b)
        print(b)

        for x in range(0, n):
            win = True
            for y in range(0, n):
                print(b[x, y])

                if b[x, y] != turn:
                    win = False
            if win == True:
                return win

        return win

    def vertical(self, turn, P, b):
        win = True
        n = len(b)
        for x in range(n):
            win = True
            for y in range(n):
                if b[y][x] != turn:
                    win = False
            if win == True:
                return win
        return win

    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str

        """
        """
        012
        345
        678
        """

        import numpy as np
        b = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
        # moves=[[2,2],[0,2],[1,0],[0,1],[2,0],[0,0]]

        n = len(moves)

        turn = ""
        P = ""
        for i in range(n):
            win = ""
            if i % 2 == 0:
                l = moves[i][0]
                h = moves[i][1]
                b[l][h] = 1
                turn = 1
                P = "A"

            else:

                l = moves[i][0]
                h = moves[i][1]
                b[l][h] = 0
                turn = 0
                P = "B"

            win = self.diagonal(turn, P, b)

            if win == True:
                return P
            win = self.diagonal2(turn, P, b)

            if win == True:
                return P

            win = self.horizontal(turn, P, b)
            if win == True:
                return P
            win = self.vertical(turn, P, b)
            if win == True:
                return P
            continue

        for i in range(len(b)):
            for j in range(len(b)):
                if b[i][j] > 1:
                    return "Pending"
        return "Draw"

# self.vertical()
#         self.horizontal()
#         self.result()





