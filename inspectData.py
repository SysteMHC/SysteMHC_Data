import pandas as pd

df = pd.read_csv("SysteMCH_Data/annotation/cleanedTable_id.csv")

fileids = df[df["MHCAllele"] == 'A03,A24,B07,B51']["FileName"]
allMzXMLs = glob.glob("/mnt/Systemhc/Data/PXD001872/*.mzXML")

res = list()
for i in fileids:
    res  += [x for x in allMzXMLs if ntpath.basename(x) == i]


for i in df["SampleID"].unique():
    tmp = df[df["SamleID"] == i]
    files_toProcess = tmp['FileName']
    print "==============================================="
    print files_toProcess


res = os.listdir("/mnt/Systemhc/Data/PXD001872/")

# check if files in annotations are physically present.

if len(list(set(df['FileName']) - set(res))) == 0:

import glob


[x for x in res if re.search('JY_EBV_1_Tubingen_120706_AR_CoOpNO_JY_Normal_W_10',x)]


