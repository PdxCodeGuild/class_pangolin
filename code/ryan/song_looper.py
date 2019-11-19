from pydub import AudioSegment
from pydub.playback import play

# loop class to creat audio loop instances
class Song_loop:
    song = AudioSegment.from_wav("blue_sky_main.wav")
# start/stop times of audio loop, number of repeats
    def __init__(self, start, end, repeats):
        self.start = start 
        self.end = end 
        self.repeats = repeats
# convert start/stop times in minutes and seconds to seconds
    def convert_to_seconds(self):
        if self.start > 59:
            min_to_sec = (self.start // 100) * 60
            seconds = self.start % 100
            self.start = min_to_sec + seconds
        if self.end > 59:
            min_to_sec = (self.end // 100) * 60
            seconds = self.end % 100
            # add 3 seconds to end to allow time for fade between plays
            self.end = (min_to_sec + seconds) + 3
# plays the loop, allows to repeat the same loop over if needed
    def play_loop(self):
        # converts start/stop times to milliseconds, as needed in pydub
        # fade added at end
        l = Song_loop.song[self.start * 1000: self.end * 1000].fade_out(5000)
        play(l * self.repeats)
        while True:
            play_same = input("Would you like to play the same loop again?  (y)es, (n)o:  ")
            if play_same == "y":
                play(l * self.repeats)
            elif play_same == "n":
                break

def main():
    while True:    
        start = input("\n\n\nEnter the start time of your loop (ex. '5' to start at 5 second mark, '112' for 1 minute 12 seconds, or enter 'done' to exit:  ")
        if start == "done":
            break
        end = input("Enter the end time of your loop (ex. '5' to end at 5 second mark, '112' for 1 minute 12 seconds:  ) ")
        repeats = input("Enter the number of times your loop should repeat: ")
    
        loop = Song_loop(int(start), int(end), int(repeats))
        loop.convert_to_seconds()
        loop.play_loop()
main()




