n_files = 1000000
files = []

for i in range(n_files):
    f = open('test.txt')
    files.append(f)
    f.close()

# no errors, all correct!
