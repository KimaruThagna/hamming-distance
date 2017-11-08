#HAMMING DISTNACE IS THE NUMBER OF POSITIONS BETWEEN 2 STRINGS OF EQUAL LENGTH WHERE THE
# CORRESPONDING SYMBOLS ARE DIFFERENT. MOSTLY APPLIED IN CODING THEORY AND COMMUNICATIONS
def hammingDistance(x, y):
    if type(x) and type(y)==str:
        if len(x)==len(y):
            hamming=0
            i = 0
            s1, s2 = [], []
            [[s1.append(ord(val))] for val in x] # the ord function returns the ASCII
            # equivalent of a letter
            [[s2.append(ord(val))] for val in y]
            for x in s1:
                if x!=s2[i]: # assumption, strings are of equal length
                    hamming+=1
                i+=1
            return hamming
        else:
            return "Strings not of equal length"

    elif type(x) and type(y)==int:
        return bin(x ^ y).count('1')
    else:
        return "Unknown format of inputs"
    # bin converts int to binary string
    # x^y is a logical operator which produces 0 when digits in corresponding positions match
    # and 1 if otherwise

print(hammingDistance(2,10))
protein_sequence1="GAATGCAGATGGACTCTAGA"
protein_sequence2="GAATAGCTAATCACTCTAGA"
print(hammingDistance(protein_sequence1,protein_sequence2))
print("There is a",
      int((len(protein_sequence1)-hammingDistance(protein_sequence1,protein_sequence2))/len(protein_sequence1)*100),
"% match between the 2 protein sequences")