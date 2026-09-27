emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh hi, I didn't see you there.")

def say(phrase):
    print(phrase + " " + emoticon)
