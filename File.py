with open('Test.txt', 'r') as f:
    #f_contents = f.readline()
    # while (len(f_contents) > 0):
    #    print(f_contents, end='')
    #     f_contents = f.readline()
    f_bytes = f.read(100)
    # for line in f_bytes:
    #   print(line, end='')
    # for line in f:, end=''
    #    print(line, end='')
    while (len(f_bytes) > 0):
        print(f_bytes, end='')
        f_bytes = f.read(100)
