import time
#
# openFile = open('out.txt', 'w')
# openFile.write(out)
# openFile.close()

with open('out.txt') as f:
    for line in f:
        print(line, end='')
        time.sleep(1)

# f.close()