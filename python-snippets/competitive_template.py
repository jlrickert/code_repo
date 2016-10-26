infile = open('problemIN.txt')
outfile = open('problemOUT.txt')

data_in = infile.read()

# assumes test cases are split by an empty line
test_sets = data_in.split('\n\n')

for test_set in test_sets:
    try:
        # code goes here for test set
        pass
    except Exception:
        pass

infile.close()
outfile.close()
