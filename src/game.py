class Game:
    def __init__(self):
        self.is_running = False

    def run(self):
        self.is_running = True

    def loop(self):
        while(self.is_running):
            self.process_input()
            self.update()
            self.render()

    def process_input(self):
        print("Processing input")

    def update(self):
        print("Updating")

    def render(self):
        print("Rendering to the screen")