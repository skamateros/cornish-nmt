file = 'tatoeba.tsv'
output = 'tatoeba-processed.tsv'

en_s = []
kw_s = []

with open(file, 'rt') as f:
    for line in f:
        if len(line.strip()) > 1:
            en, kw = tuple(line.strip().split('\t'))
            if en not in en_s:
                en_s.append(en)
                kw_s.append(kw)
data = [en + '\t' + kw for en, kw in zip(en_s, kw_s)]

with open(output, 'wt') as f2:
    for pair in data:
        f2.write(f'{pair}\n')