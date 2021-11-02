yehh = input('dna: ')


def dna_convervter(dna):
    yehh = str(dna).replace(' ', '')
    dna = []
    rna = []
    protein = []
    three_guy = ''
    count = 1
    # dna
    for i in yehh:
        x = ['a', 't', 'g', 'c']
        if i.lower() not in x:
            print('error')
            exit()
        else:
            continue
    for letters in yehh:
        if letters.lower() == 'a':
            three_guy += 'A'
        elif letters.lower() == 't':
            three_guy += 'T'
        elif letters.lower() == 'g':
            three_guy += 'G'
        elif letters.lower() == 'c':
            three_guy += 'C'
        if count == 3:
            count = 1
            dna.append(three_guy)
            three_guy = ''
        else:
            count += 1
    three_guy = ''
    # rna
    for letters_rna in yehh:
        if letters_rna.lower() == 'a':
            three_guy += 'U'
        elif letters_rna.lower() == 't':
            three_guy += 'A'
        elif letters_rna.lower() == 'g':
            three_guy += 'C'
        elif letters_rna.lower() == 'c':
            three_guy += 'G'
        if count == 3:
            count = 1
            rna.append(three_guy)
            three_guy = ''
        else:
            count += 1

    # protein
    for i in rna:
        if i == ('UUU' or 'UUC'):
            protein.append('Phe')
        elif i == ('UUA' or 'UUG'):
            protein.append('Leu')
        elif list(i)[0] == 'U' and list(i)[1] == 'C':
            protein.append('Ser')
        elif i == ('UAU' or 'UAC'):
            protein.append('Tyr')
        elif i == ('UAA' or 'UAG'):
            protein.append('Stop')
        elif i == ('UGU' or 'UGC'):
            protein.append('Cys')
        elif i == 'UGA':
            protein.append('Stop')
        elif i == 'UGG':
            protein.append('Trp')
        elif list(i)[0] == 'C' and list(i)[1] == 'U':
            protein.append('Leu')
        elif list(i)[0] == 'C' and list(i)[1] == 'C':
            protein.append('Pro')
        elif i == ('CAU' or 'CAC'):
            protein.append('His')
        elif i == ('CAA' or 'CAG'):
            protein.append('Gln')
        elif list(i)[0] == 'C' and list(i)[1] == 'G':
            protein.append('Arg')
        elif i == ('AUU' or 'AUC' or 'AUA'):
            protein.append('Ile')
        elif i == 'AUG':
            protein.append('Met')
        elif list(i)[0] == 'A' and list(i)[1] == 'C':
            protein.append('Thr')
        elif i == ('AAU' or 'AAC'):
            protein.append('Asn')
        elif i == ('AAA' or 'AAG'):
            protein.append('Lys')
        elif i == ('AGU' or 'AGC'):
            protein.append('Ser')
        elif i == ('AGA' or 'AGG'):
            protein.append('Arg')
        elif list(i)[0] == 'G' and list(i)[1] == 'U':
            protein.append('Val')
        elif list(i)[0] == 'G' and list(i)[1] == 'C':
            protein.append('Ala')
        elif i == ('GAU' or 'GAC'):
            protein.append('Asp')
        elif i == ('GAA' or 'GAG'):
            protein.append('Glu')
        elif list(i)[0] == 'G' and list(i)[1] == 'G':
            protein.append('Gly')

    return (f'DNA: {" ".join(dna)}\n'
            f'mRNA: {" ".join(rna)}\n'
            f'protein: {" ".join(protein)}')


print(dna_convervter(yehh))