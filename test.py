import librosa
import librosa.display

class GenreFSM:
    def __init__(self):
        # Define the states representing different genres
        self.states = {
            'Blues': (60, 80),
            'Dubstep': (140, 160),
            'Hip-Hop': (80, 115),
            'Jazz/Country': (90, 120),
            'Pop': (90, 130),
            'Rock': (160, 220),
            'R&B': (70, 90),  
        }
        
        # Define the transitions between states
        self.transitions = {
            'Blues': ['Dubstep','Hip-Hop','Jazz/Country','Pop','Rock','R&B'],
            'Dubstep': ['Blues','Hip-Hop','Jazz/Country','Pop','Rock','R&B'],
            'Hip Hop': ['Blues','Dubstep','Jazz/Country','Pop','Rock','R&B'],
            'Jazz/Country': ['Blues','Dubstep','Hip-Hop','Pop','Rock','R&B'],
            'Pop': ['Blues','Dubstep','Hip-Hop','Jazz/Country','Rock','R&B'],
            'Rock': ['Blues','Dubstep','Hip-Hop','Jazz/Country','Pop','R&B'],
            'R&B': ['Blues','Dubstep','Hip-Hop','Jazz/Country','Pop','Rock'],
        }
        
        # Initialize the FSM with the starting state
        self.current_state = 'Unknown'
        
    def determine_genre(self, audio_file):
        # Load the audio file and compute its tempo using librosa
        y, sr = librosa.load(audio_file)
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
        
        # Determine the genre based on the tempo
        matching_genre = None
        for genre, (min_bpm, max_bpm) in self.states.items():
            if min_bpm <= tempo <= max_bpm:
                matching_genre = genre
                break
        
        # If a matching genre is found, transition to it
        if matching_genre:
            self.transition_genre(matching_genre)
            return matching_genre
        else:
            print(f"No matching genre found for tempo {tempo}.")
            return 'Unknown'
    
    def transition_genre(self, genre):
        # Transition to a new genre if possible
        if genre in self.transitions.get(self.current_state, []):
            self.current_state = genre
        else:
            print(f"Cannot transition from {self.current_state} to {genre}.")
    
    def get_current_genre(self):
        return self.current_state

# Example usage
if __name__ == "__main__":
    song_genre_fsm = GenreFSM()
    
    # Example audio files (replace with your own audio files)
    audio_files = ['tracks\What a Wonderful World.mp3', 'tracks\I Can\'t Stop.mp3', 'tracks\I Love It.mp3', 'tracks\One Dance.mp3']
    
    for audio_file in audio_files:
        genre = song_genre_fsm.determine_genre(audio_file)
        current_genre = song_genre_fsm.get_current_genre()
        
        print(f"Audio File: {audio_file} => Genre: {genre}")
        print(f"Current Genre: {current_genre}\n")