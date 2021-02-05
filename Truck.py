class Truck(object):

    def __init__(self, id):
        self.max_load = 16
        self.current_location = ""
        self.current_load = []
        self.id =id


    def add(self, item):
        if len(self.current_load) < self.max_load:
            if len(item) > 2:
                self.current_load.append(item)

    def deliver(self, item, address):
        if self.current_location == address:
            for i in self.current_load:
                if item in self.current_load[i]:
                    self.current_load.remove(self.current_load[i])

    def get_id(self):
        return self.id

    def print(self):
        print("Truck " + str(self.id) + " has a current load of " + str(self.current_load))


