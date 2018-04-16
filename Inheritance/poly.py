class Base:
    def __init__(self, filename):
        self.filename = filename
        print("Base class init.")
        print(self.parent_recv)


class Sub(Base):
    parent_recv = 'From Sub class'

    def __init__(self, filename, file_long):
        super().__init__(filename)
    def play(self):
        print("Sub play.")



class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise ValueError("Invalid file format")

        self.filename = filename

class MP3(AudioFile):
    ext = 'mp3'

    def play(self):
        print(f'Play with {self.filename} as {self.ext}')


class Wave(AudioFile):
    ext = 'wav'

    def play(self):
        print(f'Play with {self.filename} as {self.ext}')


class Ogg(AudioFile):
    ext = 'ogg'

    def play(self):
        print(f'Play with {self.filename} as {self.ext}')

if __name__ == '__main__':
    s = Sub("a.mp3", 20)
    s.play()

    mp3 = MP3("my.mp3")
    mp3.play()

    print(help(MP3))