class Research(object):
    def __init__(self, name, hour, machine, seq):
        self.name = name
        self.hour = hour
        self.machine = machine
        self.seq = seq

    def get_name(self):
        return self.name

    def get_hour(self):
        return self.hour

    def get_machine(self):
        return self.machine

    def get_seq(self):
        return self.seq