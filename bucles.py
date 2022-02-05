def run():
    limit = 1000000
    counting = 0
    square_2 = 2**counting
    while square_2 < limit:
        print('2 elevado a ' + str(counting) + 
        ' es igual a: ' + str(square_2))
        counting += 1
        square_2 = 2**counting  




if __name__ == '__main__':
    run()