import json
import re

i2p = json.loads(open('mi2p.json', 'r').read())
d2i = json.loads(open('md2i.json', 'r').read())
c2i = json.loads(open('mc2i.json', 'r').read())
p2i = json.loads(open('mp2i.json', 'r').read())


def stransform(k):
    o1 = k.strip().lower()
    o2 = re.sub(r'[^a-z0-9]', '', o1)
    return o2


def render(idxs):
    if len(idxs) == 0:
        return "Unknown"
    elif len(idxs) == 1:
        return i2p[str(idxs[0])][0]
    else:
        return [i2p[str(i)][0] for i in idxs].__str__()


def find_province(residential_province, residential_city, residential_district):
    p = stransform(residential_province)
    if p in p2i:
        return render(p2i[p])

    c = stransform(residential_city)
    if c in c2i:
        return render(c2i[c])

    d = stransform(residential_district)
    if d in d2i:
        return render(d2i[d])

    return "Unknown"
