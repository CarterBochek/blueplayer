# Music player in python
import os
import glob
from pygame import mixer

# mixer.init()
# --------------------------Path of your music
# mixer.music.load("/home/carter/Music/Polkavant - Signos.mp3")

# mixer.music.play()
print('\nWelcome to blueplayer!\n')
def select_song():
    # Get the user's home directory
    home_dir = os.path.expanduser("~")
    
    # Specify the subdirectory where the music files are located
    music_dir = os.path.join(home_dir, "Music")
    
    # Get a list of audio files in the music directory
    audio_files = glob.glob(os.path.join(music_dir, "*.mp3")) + glob.glob(os.path.join(music_dir, "*.wav"))
    
    if not audio_files:
        print("\nNo audio files found in the Music directory.")
        return
    
    # Display the available songs to the user
    print("\nAvailable songs:")
    for i, audio_file in enumerate(audio_files):
        print(f"{i+1}. {os.path.basename(audio_file)}")
    
    # Get the user's song choice
    song_choice = input("Enter the song number: ")
    
    try:
        song_choice = int(song_choice)
        if song_choice < 1 or song_choice > len(audio_files):
            raise ValueError
    except ValueError:
        print("\nInvalid song number.")
        return
    
    # Load and play the selected song
    song_path = audio_files[song_choice - 1]
    mixer.music.load(song_path)
    mixer.music.play()
    print('\nBlueplayer is now playing...\n')
# Initialize pygame.mixer
mixer.init()

# Call the select_song() function to start the song selection process
select_song()
mixer.music.set_volume(0.5)

while True:
    # print("Type 'pause' to pause")
    # print("Type 'resume' to resume")
    # print("Type 'volume' set volume; default is 0.5")
    # print("Type 'stop' to stop")
    print("\nType in 'help' if you want to view available settings")

    player_setting = input('\n')

    if player_setting == "pause":
        mixer.music.pause()
        print('\nBlueplayer is now paused...\n')
    elif player_setting == "play":
        mixer.music.unpause()
        print('\nBlueplayer is now playing...\n')
    elif player_setting == "volume":
        v = float(input("\nEnter volume(0 to 1; 0.1 or 0.6 etc)\n"))
        mixer.music.set_volume(v)
    elif player_setting == 'help':
        print("\nType 'pause' to pause\nType 'play' to resume playback\nType 'volume' to set volume; default is 0.5\nType 'select' to choose a different song\nType 'stop' to stop")
    elif player_setting == 'select':
        print('\nSelect a new song to play:\n')
        select_song()
    elif player_setting == "stop":
        mixer.music.stop()
        print('\nBlueplayer is now shutting down, thanks for stopping by!\n')
        break