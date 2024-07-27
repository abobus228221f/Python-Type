import tkinter as tk
from tkinter import ttk
import random
import os
import json
import time

class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Game")
        self.root.geometry("600x400")
        self.root.configure(bg='#282c34')

        # Load saved data
        self.load_data()

        self.sentences = [
            "Hi, Charlotte. We are ready to send all the needed materials for your presentation.",
            "This is the tech support of the ReStudios. How can we help you?",
            "Welcome to ReStudios, Mike. We are happy to tell that you are hired!",
            "Hello, Phill. We can start to send first copies of the app for testing.",
            "Dear testers. The development team said that the product is ready for testing.",
            "Hi, dear Daniel. We can tell that the final product is ready for sales!",
            'Hello, dear dev team. As the testers say "The product is working perfectly!"',
            "The software update is scheduled for next week.",
            "Please review the documentation before our next meeting.",
            "The user interface needs some improvements.",
            "We appreciate your feedback and suggestions.",
            "Our team is committed to delivering high-quality products.",
            "The new feature will enhance user experience significantly.",
            "Thank you for your patience and understanding.",
            "We are constantly working to improve our services.",
            "The final version of the app will be released soon.",
            "Our team is excited to launch the new update.",
            "Please let us know if you encounter any issues.",
            "We value your input and contributions.",
            "The project is progressing as planned.",
            "Your hard work and dedication are appreciated.",
            "We are looking forward to your presentation.",
            "The beta version is available for testing.",
            "Thank you for being a part of our team.",
            "We are confident in the quality of our product.",
            "The new design looks amazing and is user-friendly.",
            "Please ensure all the documents are updated.",
            "We need to finalize the marketing strategy soon.",
            "Our customers have provided positive feedback.",
            "The development phase is nearing completion.",
            "We should celebrate our team's achievements.",
            "The test results have exceeded our expectations.",
            "Please attend the meeting tomorrow at 10 AM.",
            "The training session will be held next week.",
            "The product launch is scheduled for next month.",
            "Our team is motivated and working hard.",
            "Thank you for your cooperation and support.",
            "The recent upgrades have improved performance.",
            "Please submit your reports by end of day.",
            "The project budget needs to be reviewed.",
            "Our client is pleased with the progress made.",
            "The new office layout is more efficient.",
            "We have achieved our quarterly targets.",
            "Please ensure all team members are informed.",
            "The app is compatible with all major platforms.",
            "Our partnership with the new vendor is beneficial.",
            "The user manual is comprehensive and clear.",
            "The support team is available 24/7.",
            "Please update your work status regularly.",
            "The presentation was well-received by the audience.",
            "The feedback loop is crucial for improvements.",
            "Our team has a strong commitment to quality.",
            "The new recruits are adapting quickly.",
            "The testing phase is critical for success.",
            "Please adhere to the project timelines.",
            "The interface design is intuitive and modern.",
            "Our service levels have improved significantly.",
            "The collaboration with the external team is smooth.",
            "The bug fixes have been successfully implemented.",
            "The final review will be conducted next week.",
            "The training materials are ready for distribution.",
            "The system upgrade was completed last night.",
            "Our network security has been enhanced.",
            "Please check the latest updates on the portal.",
            "The user base has grown substantially.",
            "The workflow process has been optimized.",
            "The client's requirements have been fully met.",
            "The project scope has been clearly defined."
        ]

        self.success_messages = [
            "Great job!",
            "Well done!",
            "You're doing amazing!",
            "Keep it up!",
            "Fantastic!",
            "Excellent work!",
            "Impressive!",
            "You're a natural!",
            "Outstanding!",
            "Keep going!"
        ]

        self.current_sentence = random.choice(self.sentences)
        self.current_index = 0

        self.speedrun_mode = False
        self.start_time = None

        self.show_main_menu()

    def show_main_menu(self):
        self.clear_widgets()
        self.root.configure(bg='#282c34')

        self.title_label = tk.Label(self.root, text="Typing Game", font=('Helvetica', 32), fg='#61dafb', bg='#282c34')
        self.title_label.pack(pady=40)

        self.start_button = tk.Button(self.root, text="Start Game", font=('Helvetica', 14), command=self.start_game, bg='#61dafb', fg='#282c34')
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", font=('Helvetica', 14), command=self.root.quit, bg='#ff6f61', fg='#282c34')
        self.quit_button.pack(pady=10)

        self.speedrun_button = tk.Button(self.root, text="Speedrun Mode", font=('Helvetica', 10), command=self.toggle_speedrun, bg='#3c4049', fg='#61dafb')
        self.speedrun_button.place(x=10, y=10)

    def toggle_speedrun(self):
        self.speedrun_mode = not self.speedrun_mode
        if self.speedrun_mode:
            self.speedrun_button.config(bg='#61dafb', fg='#282c34')
        else:
            self.speedrun_button.config(bg='#3c4049', fg='#61dafb')

    def start_game(self):
        self.clear_widgets()
        self.root.configure(bg='#282c34')

        if self.speedrun_mode:
            self.start_time = time.time()
            self.timer_label = tk.Label(self.root, text="00:00:00", font=('Helvetica', 14), fg='#008000', bg='#000000')
            self.timer_label.place(x=450, y=10)
            self.update_timer()

        # Frames
        self.top_frame = tk.Frame(self.root, bg='#282c34')
        self.top_frame.pack(pady=10, anchor='nw')

        self.frame = tk.Frame(self.root, bg='#282c34')
        self.frame.pack(pady=10)

        self.text_frame = tk.Frame(self.root, bg='#282c34')
        self.text_frame.pack(pady=10)

        self.bottom_frame = tk.Frame(self.root, bg='#282c34')
        self.bottom_frame.pack(pady=10, anchor='sw')

        # Email counter
        self.emails_left = random.randint(5, 20)
        self.emails_label = tk.Label(self.top_frame, text=f"Emails left: {self.emails_left}", font=('Helvetica', 14), fg='#ffffff', bg='#282c34')
        self.emails_label.pack(side='left', padx=20)

        # Shifts completed
        self.shifts_label = tk.Label(self.top_frame, text=f"Shifts completed: {self.completed_shifts}", font=('Helvetica', 14), fg='#ffffff', bg='#282c34')
        self.shifts_label.pack(side='left', padx=20)

        # Display Sentence
        self.display_sentence = tk.StringVar()
        self.display_sentence.set(self.current_sentence)

        self.label = tk.Label(self.text_frame, textvariable=self.display_sentence, font=('Helvetica', 16), fg='#61dafb', bg='#282c34', wraplength=500)
        self.label.pack(pady=20)

        # Entry box
        self.entry = tk.Entry(self.frame, font=('Helvetica', 14), bg='#3c4049', fg='#ffffff', insertbackground='#ffffff', relief='flat', borderwidth=2)
        self.entry.pack(pady=20, ipadx=5, ipady=5)
        self.entry.bind('<KeyRelease>', self.on_key_release)
        self.entry.bind('<Return>', self.check_text)

        # Feedback label
        self.feedback_label = tk.Label(self.frame, text="", font=('Helvetica', 12), fg='#ff6f61', bg='#282c34')
        self.feedback_label.pack(pady=10)

        # Life system
        self.lives = 3
        self.life_boxes = []
        for i in range(3):
            box = tk.Label(self.bottom_frame, text="□", font=('Helvetica', 20), fg='#ffffff', bg='#282c34')
            box.pack(side='left', padx=5)
            self.life_boxes.append(box)

    def update_timer(self):
        if self.speedrun_mode:
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time % 1) * 1000)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:03}")
            self.root.after(50, self.update_timer)

    def on_key_release(self, event):
        typed_text = self.entry.get()
        self.update_display(typed_text)

    def update_display(self, typed_text):
        displayed_text = ""
        correct_text = self.current_sentence[:len(typed_text)]

        for i, char in enumerate(correct_text):
            if i < len(typed_text):
                if typed_text[i] == char:
                    displayed_text += char
                else:
                    displayed_text += f"{char}"
            else:
                displayed_text += f"{char}"

        displayed_text += self.current_sentence[len(typed_text):]
        self.display_sentence.set(displayed_text)

    def check_text(self, event):
        typed_text = self.entry.get()
        if typed_text == self.current_sentence:
            self.feedback_label.config(text=random.choice(self.success_messages), fg='#61dafb')
            self.current_sentence = random.choice(self.sentences)
            self.display_sentence.set(self.current_sentence)
            self.entry.delete(0, tk.END)
            self.emails_left -= 1
            self.emails_label.config(text=f"Emails left: {self.emails_left}")

            if self.emails_left == 0:
                self.completed_shifts += 1
                self.save_data()
                self.show_shift_complete_screen()
        else:
            self.lives -= 1
            self.life_boxes[3 - self.lives - 1].config(fg='red')
            self.entry.config(fg='red')
            self.root.after(500, lambda: self.entry.config(fg='white'))
            if self.lives == 0:
                self.show_game_over_screen()

    def show_shift_complete_screen(self):
        self.clear_widgets()
        self.root.configure(bg='#282c34')

        self.complete_label = tk.Label(self.root, text="Shift Complete!", font=('Helvetica', 24), fg='#61dafb', bg='#282c34')
        self.complete_label.pack(pady=40)

        self.hint_label = tk.Label(self.root, text="Press 'Enter' for next shift or 'Q' to quit.", font=('Helvetica', 14), fg='#61dafb', bg='#282c34')
        self.hint_label.pack(pady=10)

        self.root.bind('<Return>', self.start_game)
        self.root.bind('<q>', self.quit_game)

    def show_game_over_screen(self):
        self.clear_widgets()
        self.root.configure(bg='#8b0000')

        self.game_over_label = tk.Label(self.root, text="Game Over", font=('Helvetica', 24), fg='#ffffff', bg='#8b0000')
        self.game_over_label.pack(pady=20)

        self.hint_label = tk.Label(self.root, text="Press 'Enter' to retry or 'Q' to quit.", font=('Helvetica', 14), fg='#ffffff', bg='#8b0000')
        self.hint_label.pack(pady=10)

        self.root.bind('<Return>', self.start_game)
        self.root.bind('<q>', self.quit_game)

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
            widget.place_forget()

    def load_data(self):
        try:
            with open('game_data.json', 'r') as file:
                data = json.load(file)
                self.completed_shifts = data['completed_shifts']
        except FileNotFoundError:
            self.completed_shifts = 0

    def save_data(self):
        data = {'completed_shifts': self.completed_shifts}
        with open('game_data.json', 'w') as file:
            json.dump(data, file)

    def quit_game(self, event=None):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()
