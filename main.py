#importing all the library require for the Music Plyer
import tkinter as tk
import os
from pygame import mixer

#Creating the window  
canvas = tk.Tk()
canvas.geometry('400x400')
canvas.title("Music Player")
canvas.iconbitmap('icon.ico')
canvas.config(bg='black')

#Songs folder
songLib="C:\\Users\Admin\Desktop\music player\songs"

# initializing  mixer
mixer.init()

#Storing the imades for the buttons
prev_img=tk.PhotoImage(file='prev.png')
pause_img=tk.PhotoImage(file='pause.png')
play_img=tk.PhotoImage(file='play.png')
next_img=tk.PhotoImage(file='next.png')
stop_img=tk.PhotoImage(file='stop-button.png')


#Creating the functions for all the buttons
def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(songLib+"\\"+listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    #deselect the current song
    listbox.select_clear('active')

def play_next():
    #saving the index of current song
    next_song = listbox.curselection()
    next_song = next_song[0]+1
    next_song_name = listbox.get(next_song)
    label.config(text=next_song_name)
    
    #function to play song
    mixer.music.load(songLib+"\\"+next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    next_song = listbox.curselection()
    next_song = next_song[0]-1
    next_song_name = listbox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(songLib+"\\"+next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)  

def pause_song():
    if pauseButton["text"]=="Pause":
        mixer.music.pause()
        pauseButton["text"]="Play"
    else:
        mixer.music.unpause()
        pauseButton["text"]="Pause"
        
#list box to show the songs
listbox= tk.Listbox(canvas,fg= "black",bg="white",width="80",font=('poppins',14))
listbox.pack(padx=15,pady=15)

#Display the name of the song playing
label= tk.Label(canvas,text=' ',bg='black',fg='yellow',font=('poppins', 18))
label.pack(pady=15)

#Frame to contain all the button packed together
top=tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=5,anchor='center')

#Creating All the buttons and adding them to the frame
#And providing them the functionality
prevButton =tk.Button(canvas,text="Prev",image=prev_img,bg='black',borderwidth=0,command=play_prev)
prevButton.pack(pady=15,in_=top,side='left')

stopButton= tk.Button(canvas,text="Stop",image=stop_img,bg='black',borderwidth=0,command=stop)
stopButton.pack(pady=15,in_=top,side='left')

playButton= tk.Button(canvas,text="Play",image=play_img,bg='black',borderwidth=0,command=select)
playButton.pack(pady=15,in_=top,side='left')

pauseButton= tk.Button(canvas,text="Pause",image=pause_img,bg='black',borderwidth=0,command=pause_song)
pauseButton.pack(pady=15,in_=top,side='left')

nextButton= tk.Button(canvas,text="Next",image=next_img,bg='black',borderwidth=0,command=play_next)
nextButton.pack(pady=15,in_=top,side='left')

#adding song file to the listbox
for root,dirs ,files in os.walk(songLib):
    for song in files:
        listbox.insert('end',song)

#mainLoop
canvas.mainloop()