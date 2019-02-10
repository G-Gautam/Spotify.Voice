import speech_recognition as sr
import spotipy
import spotipy.util as util

token = util.prompt_for_user_token("12161935268", "user-modify-playback-state", client_id='a2dd7655430442dd98f19f08a6e32f18',
                                       client_secret='a91bb014e5e04930a1861505ee0eab87', redirect_uri='http://localhost:8888/callback')
spotify = spotipy.Spotify(auth = token)

command = None

def spotifyControl(cnt):
    global spotify
    if (cnt == "pause"):
        spotify.pause_playback()

    if (cnt == "play"):
        spotify.start_playback()

    if (cnt == "next"):
        spotify.next_track()

    if (cnt == "back"):
        spotify.previous_track()

r = sr.Recognizer()
mic = sr.Microphone()
mic.list_microphone_names()


while(command == None):

    with mic as source:
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(command)
        spotifyControl(command)
        command = None
    except Exception:
        continue




