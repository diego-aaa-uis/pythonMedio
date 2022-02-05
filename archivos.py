"""def read():
    numbers = []
    with open("./archivos/numbers.txt", "r") as f:
        #encoding="utf-8"
        for line in f:
            numbers.append(int(line))
        print(numbers)"""
def read():
    numbers = []
    f= open("home/diego-aaa/pythonMedio/nuevasClases/archivos/numbers.txt", "r") 
    for line in f:
        numbers.append(int(line))
    print(numbers)

def write():
    names = ["María", "Fernanda", "Andrés", "Antonio"]
    f= open("/home/diego-aaa/pythonMedio/nuevasClases/archivos/names.txt", "a", encoding="utf-8")
    for name in names:
        f.write(name)
        f.write("\n")


def run():
    write()

if __name__ == "__name__":
    run()
