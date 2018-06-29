class Pomodoras:

    def __init__(self):
        self.pomodoras = []

    def add_pom(self, pomodora):
        self.pomodoras.append(pomodora)

    def remove_pom(self, index):
        return self.pomodoras.pop(index)


if __name__ == "__main__":
    pass
