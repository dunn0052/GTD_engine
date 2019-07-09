class dt:

    def __init__(self):
        self.dt = [0]
        
    def update(self):
        self.dt[0] += 1



class rec:

    def __init__(self, dt):
        self.dt = dt

    def update(self):
        print(self.dt)

d = dt()
r = rec(d.dt)

for i in range(10):
    r.update()
    d.update()
