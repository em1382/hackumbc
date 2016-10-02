from threading import Thread
import twython
import webbrowser

consumer_key = "OyIpsi9JYB0PnF1ufCgltuO1u"
consumer_secret = "EGUEGZQ8jJvrApUQHr5Edx1tyOO3V2Sy9A6Ye3xykApH5IeZmM"
access_token = "737509189354823681-EEe6qnjQggUmrEwmKW8fnF19DAfXZri"
access_token_secret = "Qfyk8a53n7sSXeOnrpPRg0FS44CNSoMdf8zJMlbLFzF1c"
    
class Worker(Thread):
    """A threaded version of Beige"""
    def __init__(self, tweet, post_id, screen_name, blacklist):
        Thread.__init__(self)
        self.tweet = tweet
        self.post_id = post_id
        self.screen_name = screen_name
        self.blacklist = blacklist

    # Analyzes the tweet.
    def run(self):
        for word in self.tweet.rstrip().split():
            if word.decode('utf-8', errors='ignore') in self.blacklist:
                t = twython.Twython(consumer_key, consumer_secret, access_token, access_token_secret)
                print(self.post_id, "@" + self.screen_name)
                t.create_block(user_id=self.post_id)
                print("User blocked. Offending word was", word.decode('utf-8', errors='ignore')[0] + ((len(word) - 1) * "*") + ".")
            if word.decode('utf-8', errors='ignore') == "Rick":
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        return "Completed" # Kills the Thread. Kind of a hack...
        
class CustomStreamer(twython.TwythonStreamer):
    """A custom Twython streamer that grabs racist and offensive tweets"""
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, blacklist):
            super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)
            self.blacklist = blacklist
    
    # This method is called when data is successfully recieved from the Twitter API.
    def on_success(self, data):
        if 'text' in data:
            worker = Worker(data['text'].encode('utf-8', errors='ignore'), data['user']['id'], data['user']['screen_name'], self.blacklist)
            worker.start()

    # This method is called when an error is returned by the Twitter API.
    def on_error(self, status_code, data):
        return "Error, status code was " + str(status_code) + "."

def main():
    with open("redacted.txt") as f:
        print("Scanning blacklist...")
        blacklist = [x.rstrip() for x in f.readlines()]
        print("Blacklist scanned successfully!")
        
    print("Establishing connection to the Twitter API...")
    streamer = CustomStreamer(consumer_key, consumer_secret, access_token, access_token_secret, blacklist)
    print("Succeeded!")
    try:
        streamer.statuses.filter(track=blacklist)
    except KeyboardInterrupt:
        print("Exiting...")
        
    
if __name__ == "__main__":
    main()


            
    

