import os
import glob
from pygame import mixer
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QInputDialog, QPushButton, QListWidget, QVBoxLayout, QWidget


class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blueplayer")
        self.setGeometry(100, 100, 400, 300)

        self.status_label = QLabel(self)

        self.song_list_widget = QListWidget(self)
        self.song_list_widget.itemClicked.connect(self.song_selected)

        self.play_button = QPushButton("Play", self)
        self.play_button.clicked.connect(self.play_music)

        self.resume_button = QPushButton("Resume", self)
        self.resume_button.clicked.connect(self.resume_music)

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.clicked.connect(self.pause_music)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_program)

        self.volume_button = QPushButton("Volume", self)
        self.volume_button.clicked.connect(self.set_volume)

        self.song_choice = None

        mixer.init()
        self.setup_ui()
        self.update_song_list()

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        layout.addWidget(self.status_label)
        layout.addWidget(self.song_list_widget)
        layout.addWidget(self.play_button)
        layout.addWidget(self.resume_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.volume_button)

    def update_song_list(self):
        self.song_list_widget.clear()

        home_dir = os.path.expanduser("~")
        music_dir = os.path.join(home_dir, "Music")
        audio_files = glob.glob(os.path.join(music_dir, "*.mp3")) + glob.glob(os.path.join(music_dir, "*.wav"))

        if not audio_files:
            self.status_label.setText("No audio files found in the Music directory.")
            return

        self.status_label.setText("Available songs:")
        for audio_file in audio_files:
            song_name = os.path.basename(audio_file)
            self.song_list_widget.addItem(song_name)

    def song_selected(self, item):
        song_index = self.song_list_widget.indexFromItem(item).row()
        self.song_choice = song_index + 1

    def play_music(self):
        if self.song_choice is not None:
            song_path = os.path.join(os.path.expanduser("~"), "Music", self.song_list_widget.currentItem().text())
            mixer.music.load(song_path)
            mixer.music.play()
            self.status_label.setText("Blueplayer is now playing...")

    def resume_music(self):
        mixer.music.unpause()
        self.status_label.setText("Blueplayer is now playing...")

    def pause_music(self):
        mixer.music.pause()
        self.status_label.setText("Blueplayer is now paused...")

    def stop_program(self):
        mixer.music.stop()
        self.status_label.setText("Blueplayer is now stopped.")
        QApplication.quit()

    def set_volume(self):
        v, ok = QInputDialog.getDouble(self, "Set Volume", "Enter volume (0 to 1):", decimals=2)
        if ok:
            mixer.music.set_volume(v)


if __name__ == "__main__":
    app = QApplication([])
    window = MusicPlayer()
    window.show()
    app.exec()
