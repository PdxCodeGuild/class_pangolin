# Find number of sentences
doc1 = 'wrds_doc.txt'

def get_snt(d):
    with open(d) as f:
        num_snt = f.read().count('.')
        return num_snt

# Find number of words
def get_wrd(d):
    with open(d) as f:
        for line in f:
            num_wrd = len(line.split())
            return num_wrd

# Find number of letters
def get_chr(d):
    with open(d) as f:
        num_chr = len(f.read().replace(' ','').replace('.', '').replace(',',''))
        return num_chr

ari = (4.71 * (get_chr(doc1) / get_wrd(doc1)) + 0.5 * (get_wrd(doc1) / get_snt(doc1)) - 21.43)
print(ari)