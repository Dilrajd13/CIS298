

number =0
# open file  w is to write,this deletes all 'a' to append this adds
some_file=open('number.txt', "w")

while number< 1_000_000:

    # write to file
    some_file.write(f' {number}\n')

    number +=1
    # close file
    some_file.close()

    # open an existing file
    read_file = open('text.txt')

    # read file
    line = read_file.readline()
    while line:
        print(line, end="")
        line = read_file.readline()
        print()

        read_file.close()





        # make a menu
        choice = ""
        while choice != "4":
            print("1 one")
            print("2 two")
            choice= input()

    if choice == 1:
        print("first")
    elif choice == 2:
        print('second')
    # print(number)

