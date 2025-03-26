name = "Dave"
count = 1


def another():
    color = "Blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "Red"
        print(color)
        print(name)
    print(color)
    greeting("Dave")

another()
print(count)

