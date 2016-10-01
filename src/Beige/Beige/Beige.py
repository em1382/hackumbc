# Beige scans Twitter for offensive tweets, and posts the offending accounts on a review website.

import Twitter

def main():
    ck = "OyIpsi9JYB0PnF1ufCgltuO1u"
    cs = "EGUEGZQ8jJvrApUQHr5Edx1tyOO3V2Sy9A6Ye3xykApH5IeZmM"
    at = "737509189354823681-EEe6qnjQggUmrEwmKW8fnF19DAfXZri"
    ats = "Qfyk8a53n7sSXeOnrpPRg0FS44CNSoMdf8zJMlbLFzF1c"
    
    twitter = Twitter.Twitter(ck, cs, at, ats)
    
    print(twitter.get_public_tweets())

if __name__ == "__main__":
    main()