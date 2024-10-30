import tkinter as tk
from tkinter import Tk, messagebox

class TIcTacToe :
    def __init__(self) :
        #assuming that the first player is  "x".
        self.current_player = "X"

#step-1 :- creating a board with 9 cells        
        #declaring how many rows and how many columns are present in the board by creationg the board.
        self.board = [["","",""],["","",""],["","",""]]

#step-2 :- creating a new window for our game and giving the name.
        #to create a new window.
        self.window = tk.Tk()

        #naming the title of the window.
        self.window.title("Tic Tac Toe")


#step-3 :- Transforming the 9 cells into the buttons
        #to set board elements as a buttons
        self.buttonsGrid = []

        #3.1 :- creating the cell's.
        #3.2 :- converting the 3 cells as a Row 
        #3.3 :- converting three rows into the a single grid.
        for i in range(3) :
            row = []
            for j in range(3) :
                button = tk.Button(self.window, text = "",width = 20,height = 10,command= lambda i=i,j=j : self.make_move(i,j))#sending the i,j values to the function make_move as (row,col) by using the command from the user.
                button.grid(row = i,column = j)#converting the (i,j) column as the button
                row.append(button)#add (i,j)cell to the row after converting the (i,j) column as the button
            self.buttonsGrid.append(row)#add i row to the row to the buttonsGrid variable.


    def make_move(self,row,col):#receiveing the (row,col) values as a (i,j).
        if self.board[row][col] == "" : #checking the board if [eg:- (0,0)] cell is empty ,if empty the block of code is will be executed,if not empty the value in the cell will remains the same.
            self.board[row][col] = self.current_player #if board eg:- (0,0) cell is empty ,then board value becomes the current[layer value i.e,. "X"/"O"
            self.buttonsGrid[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player) :
                messagebox.showinfo("Game Over "," the Winner is "+self.current_player)
                self.window.quit()
            elif self.is_draw():
                messagebox.showinfo("Game Over ","Oh,its Draw!")
                self.window.quit()
            self.current_player = "O" if self.current_player == "X" else "X" #giving chance to another player i.e., "O".


    def check_winner(self,player) :
        for i in range (3) :
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2] :
                return True
            if player == self.board[0][i] == self.board[1][i] == self.board[2][i] :
                return True
            if player == self.board[0][0] == self.board[1][1] == self.board[2][2] :
                return True
            if player == self.board[0][2] == self.board[1][1] == self.board[2][0] :
                return True
            return False
        
    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False
            return True


    def run(self):
        self.window.mainloop()#mainloop is a built-in tkinter function which is is used to run the program 

game = TIcTacToe()
game.run()