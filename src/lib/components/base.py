class Component:
    def __init__(self, actor, update_order = 1):
        self.actor = actor
        self.update_order = update_order

    def update(self, delta_time):
        pass

    def destroy(self):
        pass