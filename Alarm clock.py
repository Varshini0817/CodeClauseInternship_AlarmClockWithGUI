from tkinter import *
import datetime
import time
import pygame
from tkinter import filedialog

class AlarmClock:
    def __init__(self):
        self.clock = Tk()
        self.clock.title("Alarm Clock")
        self.clock.geometry("400x400")

        time_format = Label(self.clock, text="Enter time in 24-hour format!", fg="white", bg="black", font="Arial")
        time_format.place(x=60, y=120)

        add_time = Label(self.clock, text="Hour Min Sec", font=60)
        add_time.place(x=110)

        set_your_alarm = Label(self.clock, text="Set your alarm time", fg="blue", relief="solid", font=("Helvetica", 7, "bold"))
        set_your_alarm.place(x=0, y=29)

        self.hour = StringVar()
        self.min = StringVar()
        self.sec = StringVar()

        hour_time = Entry(self.clock, textvariable=self.hour, bg="pink", width=15)
        hour_time.place(x=110, y=30)

        min_time = Entry(self.clock, textvariable=self.min, bg="pink", width=15)
        min_time.place(x=150, y=30)

        sec_time = Entry(self.clock, textvariable=self.sec, bg="pink", width=15)
        sec_time.place(x=200, y=30)

        submit = Button(self.clock, text="Set Alarm", fg="red", width=10, command=self.actual_time)
        submit.place(x=110, y=70)

        browse_button = Button(self.clock, text="Browse Sound", command=self.browse_sound_file)
        browse_button.place(x=250, y=70)

        self.selected_sound = StringVar()

        self.stop_button = Button(self.clock, text="Stop Alarm", fg="red", width=10, command=self.stop_alarm)
        self.stop_button.place(x=220, y=200)

        self.alarm_playing = False
        pygame.mixer.init()

        self.clock.mainloop()

    def alarm(self, set_alarm_timer, sound_file):
        self.alarm_playing = True
        while self.alarm_playing:
            time.sleep(1)
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            date = current_time.strftime("%d/%m/%Y")
            print("The set time is: ",date)
            print(now)

            if now == set_alarm_timer:
                print("Wake up!!!")
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play(-1)  # Play the alarm in a loop until stopped
                break

    def actual_time(self):
        set_alarm_timer = f"{self.hour.get()}:{self.min.get()}:{self.sec.get()}"
        sound_file = self.selected_sound.get()
        self.alarm(set_alarm_timer, sound_file)

    def browse_sound_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3")])
        self.selected_sound.set(file_path)

    def stop_alarm(self):
        self.alarm_playing = False
        pygame.mixer.music.stop()

if __name__ == "__main__":
    alarm_clock = AlarmClock()
