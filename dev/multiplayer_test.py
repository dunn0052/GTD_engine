from controllerIO import Controller

c1 = Controller(0)
c2 = Controller(1)

while True:
    b0 = c1.getInput()
    b1 = c2.getInput()
    if b0:
        print(b0)
    if b1:
        print(b1)
