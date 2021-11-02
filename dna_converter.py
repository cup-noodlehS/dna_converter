while True:
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
            dna_letter = {
                'a': 'A',
                't': 'T',
                'g': 'G',
                'c': 'C'
            }
            three_guy += dna_letter[letters]
            if count == 3:
                count = 1
                dna.append(three_guy)
                three_guy = ''
            else:
                count += 1
        three_guy = ''
        # rna
        for letters_rna in yehh:
            rna_letter = {
                'a': 'U',
                't': 'A',
                'g': 'C',
                'c': 'G'
            }
            three_guy += rna_letter[letters_rna]
            if count == 3:
                count = 1
                rna.append(three_guy)
                three_guy = ''
            else:
                count += 1

        # protein
        for i in rna:
            if i in ['UUU', 'UUC']:
                protein.append('Phe')
            elif i in ['UUA', 'UUG']:
                protein.append('Leu')
            elif list(i)[0] == 'U' and list(i)[1] == 'C':
                protein.append('Ser')
            elif i in ['UAU', 'UAC']:
                protein.append('Tyr')
            elif i in ['UAA', 'UAG']:
                protein.append('Stop')
            elif i in ['UGU', 'UGC']:
                protein.append('Cys')
            elif i == 'UGA':
                protein.append('Stop')
            elif i == 'UGG':
                protein.append('Trp')
            elif list(i)[0] == 'C' and list(i)[1] == 'U':
                protein.append('Leu')
            elif list(i)[0] == 'C' and list(i)[1] == 'C':
                protein.append('Pro')
            elif i in ['CAU', 'CAC']:
                protein.append('His')
            elif i in ['CAA', 'CAG']:
                protein.append('Gln')
            elif list(i)[0] == 'C' and list(i)[1] == 'G':
                protein.append('Arg')
            elif i in ['AUU', 'AUC', 'AUA']:
                protein.append('Ile')
            elif i == 'AUG':
                protein.append('Met')
            elif list(i)[0] == 'A' and list(i)[1] == 'C':
                protein.append('Thr')
            elif i in ['AAU', 'AAC']:
                protein.append('Asn')
            elif i in ['AAA' or 'AAG']:
                protein.append('Lys')
            elif i in ['AGU', 'AGC']:
                protein.append('Ser')
            elif i in ['AGA', 'AGG']:
                protein.append('Arg')
            elif list(i)[0] == 'G' and list(i)[1] == 'U':
                protein.append('Val')
            elif list(i)[0] == 'G' and list(i)[1] == 'C':
                protein.append('Ala')
            elif i in ['GAC', 'GAU']:
                protein.append('Asp')
            elif i in ['GAA', 'GAG']:
                protein.append('Glu')
            elif list(i)[0] == 'G' and list(i)[1] == 'G':
                protein.append('Gly')

        return (f'DNA: {" ".join(dna)}\n'
                f'mRNA: {" ".join(rna)}\n'
                f'protein: {" ".join(protein)}')


    print(dna_convervter(yehh))
