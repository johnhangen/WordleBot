#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from src.wordlePos import WordlePos
from src.textReader import TextReader


def run_app():
    root = tk.Tk()
    
    reader = TextReader(path='data/words.txt')
    with reader.read() as lines:
        words = reader.wordsToList(lines)

    wordle_solver = WordlePos(words)

    app = WordleSolverGUI(root, wordle_solver)
    root.mainloop()


class WordleSolverGUI:
    def __init__(self, master, wordle_solver) -> None:
        self.master = master
        self.wordle_solver = wordle_solver
        master.title("Wordle Solver")

        # Entry for correct letters
        tk.Label(master, text="Correct Letters (e.g., __o_e):").grid(row=0, column=0)
        self.correct_entry = tk.Entry(master)
        self.correct_entry.grid(row=0, column=1)

        # Entry for misplaced letters
        tk.Label(master, text="Misplaced Letters (e.g., l):").grid(row=1, column=0)
        self.misplaced_entry = tk.Entry(master)
        self.misplaced_entry.grid(row=1, column=1)

        # Entry for positions of misplaced letters
        tk.Label(master, text="Positions of Misplaced Letters (e.g., 3):").grid(row=2, column=0)
        self.positions_entry = tk.Entry(master)
        self.positions_entry.grid(row=2, column=1)

        # Entry for absent letters
        tk.Label(master, text="Absent Letters (e.g., arn):").grid(row=3, column=0)
        self.absent_entry = tk.Entry(master)
        self.absent_entry.grid(row=3, column=1)

        # Button to process the input
        self.solve_button = tk.Button(master, text="Solve", command=self.solve)
        self.solve_button.grid(row=4, column=0, columnspan=2)

        # Display area for possible words
        self.words_display = tk.Text(master, height=10, width=50)
        self.words_display.grid(row=5, column=0, columnspan=2)

    def solve(self) -> None:
        # Clear the previous results
        self.words_display.delete(1.0, tk.END)

        # Update the WordlePos instance
        self.wordle_solver.update_real_letters(self.correct_entry.get())
        misplaced_letters = self.misplaced_entry.get()
        positions = list(map(int, self.positions_entry.get().split()))
        self.wordle_solver.update_not_pos(misplaced_letters, positions)
        self.wordle_solver.update_not_letters(self.absent_entry.get())

        # Find possible words and display them
        self.wordle_solver.find_words()
        possible_words = self.wordle_solver.get_words()
        if possible_words:
            self.words_display.insert(tk.END, "\n".join(possible_words))
        else:
            self.words_display.insert(tk.END, "No matches found.")