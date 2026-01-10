import os

path = 'en-kw-tatoeba'
with open('tatoeba.tsv', 'w') as f7:
    with open(os.path.join(path, 'tatoeba.en-kw.en'), 'rt') as f1:
        with open(os.path.join(path, 'tatoeba.en-kw.kw'), 'rt') as f2:
            for source, target in zip(f1, f2):
                f7.write(f'{source.strip()}\t{target.strip()}\n')
