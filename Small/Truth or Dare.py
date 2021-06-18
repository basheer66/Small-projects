import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk
from tkinter import messagebox
import tkinter.font
import time
# Getting Data
def get_data():
    
    data = requests.get('https://www.teenvogue.com/story/best-truth-or-dare-questions')

    soup = BeautifulSoup(data.text, 'html.parser')

    data1 = []

    for div in soup.find_all('div', { "class": "grid--item body body__container article__body grid-layout__content" }):
        values = [li.text for li in div.find_all('li')]
        data1.append(values)
        global questions
        global dares
        questions = data1[0][0:50]
        dares = data1[0][50:]
get_data()

# tkinter

root = tk.Tk()
root.configure(bg = 'black')
#root.resizable(False, False)
root.geometry('500x200')
root.title('Truth or Dare')
the_title = tk.Label(root, text="Truth or Dare",
    bg='black',
    fg='#249F38',
    bd=0,
    font= tk.font.Font(family='Helvitica', size=25),
    height=1,
    width=15)
the_title.place(x=100, y=0)
tk.Label(root, text = 'How many Players?',bg='black',
    fg='#249F38',
    bd=0,
    font= tk.font.Font(family='Helvitica', size=16),
    height=1,
    width=15).place(x=50, y=105)
entry1 = tk.Entry(root, width = 5)
entry1.place(x=240, y=110)

def open_new_window():
    global turn
    player_amount = int(entry1.get())
    game = tk.Toplevel(root)
    game.geometry('800x400')
    game.resizable(False, False)
    game.title("Truth or Dare")
    turn = 0
    def change_player_turn():
        global turn
        turn = turn + 1
        tk.Label(game, text = 'Player {} turn!'.format(turn), font = 'arial 15 bold').place(x= 20, y=50)
        if turn == player_amount:
            turn = 0
    def random_truth():
        tk.Label(game, text = str(random.choice(questions))).place(x=20, y=330)
    def random_dare():
        dare_label = tk.Label(game, text = str(random.choice(dares)), font = "arial 15").place(x=20, y=200)
    tk.Button(game, text = "Done", command = change_player_turn).place(x=395, y=350)
    tk.Button(game, text = "Truth", font = "arial 20 bold", padx = 0.5, bg = 'pale violet red', command = random_truth).place(x=100, y=300)
    tk.Button(game, text = "Dare", font = "arial 20 bold", padx = 0.5, bg = 'pale violet red', command = random_dare).place(x=250, y=300)
    #tk.Button(game, text = "Another question")
def get_player_amount():
    player_amount = entry1.get()
    open_new_window()

tk.Button(root, text = 'proceed', command = get_player_amount, width=8).place(x=290, y=110)




root.mainloop()
