board = [""] + [str(i) for i in range(1,10)] #Game Inputs

# TTT BOARD
def sos_board():
    print(f"""
            =============
            | {board[1]} | {board[2]} | {board[3]} |
            -------------
            | {board[4]} | {board[5]} | {board[6]} |
            -------------
            | {board[7]} | {board[8]} | {board[9]} |
            =============
          """)
    

def win_check(player): #Checks if a players wins
    wins = [(1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9),
            (1,5,9), (7,5,3)
            ]
    
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

    
def if_draw(): #Checks if all the position is occupied f
    return all(cell in ('X','O') for cell in board[1:])




def start_game():

    print("\nLet the game begin!\n")

    while True:
            start = input("Select 'Y' to proceed and 'X' to exit: ").upper()
            if start == "X":
                print("\nThanks for playing!")
                break
            elif start != "Y":
                print("Invalid Input.") 
                continue


            player_1 = input("\nPlayer 1 choose side 'X' or 'O': ").upper()

            if player_1 not in ("X", "O"):
                 print("\nInvalid Input, Choose \"X\" or \"O\"")
                 continue
            
            player_2 = "X" if player_1 == "O" else "O"

            current_player = player_1

            #Resets the board every game
            for i in range(1,10):
                 board[i] = str(i)

            while True:
                sos_board()
                try: 
                    pos = int(input(f"{current_player} Select position (1-9): "))

                    if pos < 1 or pos > 9:
                        print("Invalid Input, Try again.")
                        continue

                    if board[pos] in ("X", "O"):
                        print("Position is already taken, please select another position.")
                        continue

                    board[pos] = current_player
                
                except ValueError:
                     print("Invalid Input. Try again.")

                if win_check(current_player):
                    print(f"Player {current_player} wins!")
                    break

                if if_draw():
                    print("Its Draw! Play again.")
                    break

                #switches players
                current_player = player_2 if current_player == player_1 else player_1
            


start_game()
    






        


        










