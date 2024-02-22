 # solution copied from GeeksForGeeks. I will find time to understand and modify it

# Python3 program to solve N Queen
# Problem using backtracking

global N	# number of queens, also dimension of chessboard
N = 4

def printSolution(board):	#this is simply printing the solution in a nicer way
	for i in range(N):
		for j in range(N):
			if board[i][j] == 1:
				print("Q",end=" ")
			else:
				print(".",end=" ")
		print()


# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def isSafe(board, row, col):

	# Check this row on left side
	for i in range(col):
		if board[row][i] == 1:
			return False

	# Check one diagonal
	for i, j in zip(range(row, -1, -1),
					range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	# Check the other diagonal
	for i, j in zip(range(row, N, 1),
					range(col, -1, -1)):
		if board[i][j] == 1:
			return False
	return True


def solveNQUtil(board, col):

	# Base case: If all queens are placed
	# then return true
	if col >= N:
		return True

	# Consider this column and try placing
	# this queen in all rows one by one
	for i in range(N):

		if isSafe(board, i, col):

			# Place this queen in board[i][col]
			board[i][col] = 1

			# Recur to place rest of the queens
			if solveNQUtil(board, col + 1) == True:
				return True

			# If placing queen in board[i][col
			# doesn't lead to a solution, then
			# queen from board[i][col]
			board[i][col] = 0

	# If the queen can not be placed in any row in
	# this column col then return false
	return False


# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solutions, this function prints one of the
# feasible solutions.
def solveNQ():

	board =[[0 for i in range(N)] for i in range(N)]

	if solveNQUtil(board, 0) == False:
		print("Solution does not exist")
		return False

	printSolution(board)
	return True




###################################################################

def solveNQueens(n: int) -> list[list[str]]:
	# Initialize sets to keep track of occupied columns and diagonals
	col = set()		#btw set is cheaper than python
	posDiagonal = set()  # (r + c)
	negDiagonal = set()  # (r - c)
	legalStates = [0]
	eachState = [0 for i in range(n)]

	result = []
	board = [["."] * n for i in range(n)]

	def backtrack(r,legalStates, eachState):
		# Base case: If all queens are placed (reached last row), append the current board configuration to the result
		if r == n:
			copy = ["".join(row) for row in board]
			result.append(copy)
			return

		# Iterate through each column
		for c in range(n):
			# Check if placing a queen at position (r, c) violates any constraints
			if c in col or (r + c) in posDiagonal or (r - c) in negDiagonal:
				continue

			# Update occupied columns and diagonals
			col.add(c)
			posDiagonal.add(r + c)
			negDiagonal.add(r - c)
			board[r][c] = "Q"  # Place the queen
			legalStates[0]+=1
			eachState[r] += 1
			# Recursive call to place queens in the next row
			backtrack(r + 1, legalStates, eachState)


			# Backtrack: Remove the queen and reset states of occupied columns and diagonals
			col.remove(c)
			posDiagonal.remove(r + c)
			negDiagonal.remove(r - c)
			board[r][c] = "."

	backtrack(0,legalStates, eachState)  # Start backtracking from the first row
	print("total legal states, not counting initial one(1): ",legalStates[0])
	print("broken to each level: ",eachState)
	return result

# Driver Code
if __name__ == '__main__':
	#solveNQ()
	res = solveNQueens(8)
	count = len(res)
	print("total solutions: ",count)

	'''
	code below can be used to show all solutions, the actual graphical representation
	'''
	# for i in res:
	# 	for j in i:
	# 		print(j, end='\n')
	# 	print()
