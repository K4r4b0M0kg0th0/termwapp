from termwapp import Termwapp
from message import Message
from image import Image
from music import Music
from multiple import Multiple

if __name__ == "__main__":
    tp = Termwapp()
    message = Message(tp)
    message.send_message("Desired Contact Name", "Hello, this is a message sent via the Linux terminal.")
    image = Image(tp)
    image.send_image('/path/to/image.jpg')
    music = Music(tp)
    music.send_music('/path/to/music.mp3')
    multiple = Multiple(tp)
    multiple.send_to_multiple(["Person 1", "Person 2", "Group Name"], "Hello, this is a message sent to multiple people or groups via the Linux terminal.")
    tp.close_driver()
