 #!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    while True:
        try:
            print('{}'.format(my_list[count]), end='')
            count += 1
        except IndexError:
            break
        if count == x:
            break
    print()
    return count
