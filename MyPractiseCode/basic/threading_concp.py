import threading


def task1():
    print("TASK1......")
    for i in range(20):
        print("task1", i)


def task2():
    print("TASK2....")
    for i in range(11, 20):
        print("task2", i)


t1 = threading.Thread(target=task1, name="t1")
t2 = threading.Thread(target=task2, name="t2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")
