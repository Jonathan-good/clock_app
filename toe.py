from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
import random
'''
edit line 63 for actions after reaching the score limit
edit line 17 for changing the score limit
currently its quitting the app after reaching score limit
'''

class MainApp(MDApp):
    title = "Tic Tac Toe!"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('toe.kv')
    score_limit = 5  # Game ends after this score
    # Who's turn it is
    turn = "X"
    winner = False

    # Keep track of wins of O and X
    X_win = 0
    O_win = 0


    # Tie
    def no_winner(self):
        if self.winner == False and \
        self.root.ids.btn1.disabled == True and \
        self.root.ids.btn2.disabled == True and \
        self.root.ids.btn3.disabled == True and \
        self.root.ids.btn4.disabled == True and \
        self.root.ids.btn5.disabled == True and \
        self.root.ids.btn6.disabled == True and \
        self.root.ids.btn7.disabled == True and \
        self.root.ids.btn8.disabled == True and \
        self.root.ids.btn9.disabled == True:
            self.root.ids.score.text = "IT'S A TIE!!"

    # End The Game
    def end_game(self, a,b,c):
        self.winner = True
        a.color = "red"
        b.color = "red"
        c.color = "red"

        # Disable the buttons
        self.disable_all_buttons()

        # Set Label for winner
        self.root.ids.score.text = f"{a.text} Wins!"

        # Keep track of winners and loser
        if a.text == "X":
            self.X_win = self.X_win + 1	
        else:
            self.O_win = self.O_win + 1

        self.root.ids.game.text = f"X Wins: {self.X_win}  |  O Wins: {self.O_win}"
        # end game if reached the score limit
        if self.X_win == self.score_limit:
            self.stop()
            self.disable_all_buttons()
        else:
            self.root.ids.score.text = f"{a.text} Wins!"

    def disable_all_buttons(self):
        # Disable All Buttons when win/lose/tie
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    # check for win
    def win(self):
        # Across
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text == self.root.ids.btn3.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)

        if self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn6.text:
            self.end_game(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

        if self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)
        # Down
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)

        if self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn8.text:
            self.end_game(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

        # Diagonal 
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

        self.no_winner()
    
    def bot_move(self):
        # Get available buttons
        available_buttons = [
            self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3,
            self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6,
            self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9
        ]

        # Deleting not avaliable buttons
        available_buttons = [btn for btn in available_buttons if not btn.disabled]

        if available_buttons:
            # Choose a random available button
            bot_choice = random.choice(available_buttons)

            # Clicks the button after 0.2 seconds
            Clock.schedule_once(lambda dt: bot_choice.dispatch('on_release'), 0.2)

    def presser(self, btn):
        if self.turn == 'X':
            btn.text = "X"
            btn.disabled = True
            self.root.ids.score.text = "O's Turn!"
            self.turn = "O"

            # Check To See if "X" won
            self.win()
            
            # If the game is still ongoing, it's the bot's turn
            if not self.winner:
                self.bot_move()
        else:
            btn.text = "O"
            btn.disabled = True
            self.root.ids.score.text = "X's Turn!"
            self.turn = "X"

            # Check To See if "O" won
            self.win()

    def restart(self):
        # Reset Who's Turn It Is
        self.turn = "X"

        # Enable The Buttons
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        # Clear The Buttons
        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""

        # Reset The Button Colors
        self.root.ids.btn1.color = "green"
        self.root.ids.btn2.color = "green"
        self.root.ids.btn3.color = "green"
        self.root.ids.btn4.color = "green"
        self.root.ids.btn5.color = "green"
        self.root.ids.btn6.color = "green"
        self.root.ids.btn7.color = "green"
        self.root.ids.btn8.color = "green"
        self.root.ids.btn9.color = "green"

        # Reset The Score Label
        self.root.ids.score.text = "X GOES FIRST!"

        # Reset The Winner Variable
        self.winner = False

	
MainApp().run()
