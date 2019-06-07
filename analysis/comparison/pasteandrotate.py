import os
import csv

try: import pandas as pd
except ImportError:
    import pip
    pip.main(['install', '--user', 'pandas'])
    import pandas as pd

def getdata(filename):
    df = pd.read_csv(filename, delim_whitespace=True)
    return (df["gb_per_s"].tolist())
import sys
ourdir = sys.argv[1]
print("grabbign files from "+ourdir)
#ourdir=os.path.dirname(os.path.realpath(__file__))
answer = []
for file in os.listdir(ourdir):
    if file.startswith("all"):
        continue
    if file.startswith("detailed"):
        continue
    if file.endswith(".table"):
        fullpath = os.path.join(ourdir, file)
        answer.append([file[:-6]]+getdata(fullpath))
print("#simdjson RapidJSON sajson")
answer.sort()
for l in answer:
    print("\t".join(map(str,l)))



