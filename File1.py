# with open("Test1.txt", "w") as f:
# f.write("This is the first Line")
# f.seek(0)
# f. write('R')
# with open("Test1.txt", "r") as fr:
#   f_contents = fr.readline()
#  for line in f_contents:
#     print(line, end='')
#    f_contents = fr.readline()
# with open("Test.txt", "r") as rf:
#     with open("Test_copy.txt", "w") as wf:
#         for line in rf:
#             wf.write(line)

# with open("Test_copy.txt", "r") as fr:
#     f_contents = fr.readline()
#     while (len(f_contents) > 0):
#         print(f_contents, end='')
#         f_contents = fr.readline()
with open("GulMohar1.jpg", "rb") as rf:
    with open("GulMohar2.jpg", 'wb') as wf:
        chunk_size = 4096
        f_contents = rf.read(chunk_size)
        while (len(f_contents) > 0):
            wf.write(f_contents)
            f_contents = rf.read(chunk_size)
