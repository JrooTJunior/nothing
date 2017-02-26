import time
from sys import stdout


class Pacman:
    def __init__(self, size=2, timeout=.5):
        self.size = size - 1
        self.timeout = timeout

        self.pos = 0
        self.shift = 1
        self.spinner_symbols = ['|', '/', '-', '\\']

    def play(self):
        while True:
            if self.pos >= self.size:
                self.shift = -1
            if self.pos <= 0:
                self.shift = 1
            self.pos += self.shift

            self.out("[{spinner}]\t[{pacman}]".format(spinner=self.spinner(), pacman=self.pacman()))

            time.sleep(self.timeout)

    def out(self, text):
        stdout.write('\r')
        stdout.write(text)
        stdout.flush()

    def get_pacman_symbol(self):
        symbol = 'Є' if self.shift > 0 else 'Э'
        return symbol.upper() if self.pos % 2 else symbol.lower()

    def pacman(self):
        line = ''
        for pos in range(self.size + 1):
            if pos == self.pos:
                line += self.get_pacman_symbol()
            elif pos % 2 and pos > self.pos:
                line += '-'
            else:
                line += ' '
        return line

    def spinner(self):
        spin = self.spinner_symbols.pop(0)
        self.spinner_symbols.append(spin)
        return spin


if __name__ == '__main__':
    pacman = Pacman(32, .5)
    try:
        pacman.play()
    except KeyboardInterrupt:
        exit()
