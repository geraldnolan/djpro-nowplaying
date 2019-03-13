import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        #print("EVENT")
        #print(event.event_type)
        #print(event.src_path)
        #print(event)
        if event.event_type == "created" and "NowPlaying.txt" in event.src_path :
           with open(os.path.expanduser("~/Music/djay Pro 2/djay Media Library.djayMediaLibrary/NowPlaying.txt"),"r") as infile:
            nowplaying = infile.read().splitlines()

            outfile = open(os.path.expanduser("~/Music/djay Pro 2/djay Media Library.djayMediaLibrary/Now_Playing.txt"),"w")

            nowplayingtest = nowplaying[1].replace("Artist:", "").strip() + " - " + nowplaying[0].replace("Title:", "").strip()
            print (nowplayingtest)

            outfile.write(nowplayingtest)

            #Closing of the input and output file
            outfile.close()
        

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()