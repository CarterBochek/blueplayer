import os
import glob
from pygame import mixer
import tkinter as tk

mixer.init()

audio_files = []  # Global variable for storing audio files

def select_song():
    global audio_files  # Access the global variable
    home_dir = os.path.expanduser("~")
    music_dir = os.path.join(home_dir, "Music")
    audio_files = glob.glob(os.path.join(music_dir, "*.mp3")) + glob.glob(os.path.join(music_dir, "*.wav"))

    if not audio_files:
        print("\nNo audio files found in the Music directory.")
        return

    song_list.delete(0, tk.END)  # Clear the song list

    for audio_file in audio_files:
        song_list.insert(tk.END, os.path.basename(audio_file))

def play_selected_song():
    selection = song_list.curselection()
    if len(selection) == 1:
        song_index = selection[0]
        song_path = audio_files[song_index]
        mixer.music.load(song_path)
        mixer.music.play()

def pause_song():
    mixer.music.pause()

def resume_song():
    mixer.music.unpause()

def set_volume():
    v = volume_scale.get()
    mixer.music.set_volume(v)

def stop_song():
    mixer.music.stop()

root = tk.Tk()
root.title("Blueplayer")

# Song list
song_list = tk.Listbox(root)
song_list.pack()
# Set the window size to 500x300 pixels
root.geometry("500x300")  
# Set the background to white and text color to black
song_list = tk.Listbox(root, bg="blue", fg="white")  

# Select button
select_button = tk.Button(root, text="Select Song", command=select_song)
select_button.pack()

# Play button
play_button = tk.Button(root, text="Play", command=play_selected_song)
play_button.pack()

# Pause button
pause_button = tk.Button(root, text="Pause", command=pause_song)
pause_button.pack()

# Resume button
resume_button = tk.Button(root, text="Resume", command=resume_song)
resume_button.pack()

# Volume scale
volume_scale = tk.Scale(root, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
volume_scale.set(0.5)
volume_scale.pack()

# Volume button
volume_button = tk.Button(root, text="Set Volume", command=set_volume)
volume_button.pack()

# Stop button
stop_button = tk.Button(root, text="Stop", command=stop_song)
stop_button.pack()

root.mainloop()
