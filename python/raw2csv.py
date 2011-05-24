#!/usr/bin/python

import csv
import glob
import sys

HEADER = ["candidatura",
        "abs",
        "rel",
        "emp",
        "alc_perc",
        "votos",
        "votos_perc",
        "concej",
        "conc2007",
        "votos2007",
        "vot_perc2007",
        "cand2007"]

def raw2csv(path):
    fin = open(path)
    fout = open('%(path)s/../csv/%(filename)s.csv' % {'path':
        '/'.join(path.split('/')[:-1]),
        'filename': path.split('/')[-1]}, 'w')
    writer = csv.writer(fout)
    d = fin.readlines()
    rows = map(lambda x: x.replace(' ', '').replace('.','').\
            replace('Color', '').replace('\n','').replace(',', '.').\
            replace('%', '').split('\t'), d)
    rows = [[float(z) if z.isdigit() else z for z in x] for x in rows]
    writer.writerow(HEADER)
    for r in rows:
        writer.writerow(r[1:])
    fout.close()
    fin.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        raw2csv(path)
    else:
        print 'usage: raw2csv file'
        sys.exit()

def make_global_count(_glob, of=None):
    from collections import defaultdict
    #global conc count
    d = defaultdict(lambda: 0)
    for f in glob.glob(_glob):
        h = True
        fin = open(f)
        r = csv.reader(fin)
        for l in r:
            if h:
                h = False
                continue
            if len(l) > 7:
                key = l[0]
                conc = l[7]
                conc = float(conc) if conc else 0
                d[key] += conc
    rank = sorted(d, key=lambda x:d[x], reverse=True)
    return zip(rank,[d[k] for k in rank])



def make_new_count(_glob, of=None):
    from collections import defaultdict
    #global conc count
    d = defaultdict(lambda: 0)
    for f in glob.glob(_glob):
        h = True
        fin = open(f)
        r = csv.reader(fin)
        for l in r:
            if h:
                h = False
                continue
            if len(l) > 8:
                key = l[0]
                conc = l[7]
                conc2007 = l[8]
                conc = float(conc) if conc else 0
                conc2007 = float(conc2007) if conc2007 else 0
                if conc2007 == 0 and conc != 0:
                    d[key] += conc
    rank = sorted(d, key=lambda x:d[x], reverse=True)
    return zip(rank,[d[k] for k in rank])

def make_lost_count(_glob, of=None):
    from collections import defaultdict
    #global conc count
    d = defaultdict(lambda: 0)
    for f in glob.glob(_glob):
        h = True
        fin = open(f)
        r = csv.reader(fin)
        for l in r:
            if h:
                h = False
                continue
            if len(l)>8:
                cand2007 = l[11]
                conc = l[7]
                conc2007 = l[8]
                conc = float(conc) if conc else 0
                conc2007 = float(conc2007) if conc2007 else 0
                if conc2007 != 0 and conc == 0:
                    d[cand2007] -= conc2007
    rank = sorted(d, key=lambda x:d[x])
    return zip(rank,[d[k] for k in rank])

def make_2007_count(_glob, of=None):
    from collections import defaultdict
    #global conc count
    d = defaultdict(lambda: 0)
    for f in glob.glob(_glob):
        h = True
        fin = open(f)
        r = csv.reader(fin)
        for l in r:
            if h:
                h = False
                continue
            conc2007 = 0
            if len(l) > 7:
                key = l[0]

            if len(l) > 8:
                conc2007 = l[8]
                conc2007 = float(conc2007) if conc2007 else 0
                d[key] += conc2007
    rank = sorted(d, key=lambda x:d[x], reverse=True)
    return zip(rank,[d[k] for k in rank])


# conc amount for parties which loss all their conc

#In [3]: dl = raw2csv.make_lost_count('../data/csv/*.csv', '')

#In [4]: len(dl)
#Out[4]: 167

#In [5]: sum([y for x,y in dl])
#Out[5]: -762.0

# conc from parties which gain repr for the first time
# XXX minus bildu / and RESTO artifact !!!

#In [6]: dn = raw2csv.make_new_count('../data/csv/*.csv', '')

#In [7]: sum([y for x,y in dn])
#Out[7]: 6894.0

# That's 10% global conc!!

#In [14]: (6894.0 - (1167.0 +1243.0) ) / 67706.0
#Out[14]: 0.066227513071219685

# 6 % if we leave bildu/ resto artifact out.


# total parties conc

#In [8]: d = raw2csv.make_global_count('../data/csv/*.csv', '')

#In [9]: sum([y for x,y in d])
#Out[9]: 67706.0


# d7 = raw2csv.make_2007_count('../data/csv/*.csv', '')


# In [18]: f = open('../data/gcount/2007.csv', 'w')

# In [19]: writer = csv.writer(f)

# In [20]: for i,dd in enumerate(d7):
#        writer.writerow([i] + list(dd))

