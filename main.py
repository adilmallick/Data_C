import pandas as pd

f1 = pd.read_csv('files/ip_1m.tsv', sep='\t')
f2 = pd.read_csv('files/user_email_hash.1m.tsv', sep='\t')
f3 = pd.read_csv('files/plain_32m.tsv', sep='\t')

merge_f1_f2 = pd.merge(left=f1, right=f2, how='left', left_on='id', right_on='id')
merge_f1_f2_f3 = pd.merge(left=merge_f1_f2, right=f3, how='left', left_on='email', right_on='email')

merge_f1_f2_f3.iloc[:,[0,2,3,4,5,1]]
# merge_f1_f2_f3.to_csv("file.tsv", sep='\t')

# merge_f1_f2_f3.to_csv('file.tsv', sep="\t")
# f4 = pd.read_csv('file.tsv', sep='\t')
# print(f4)
# f4.iloc[:,[0,2,3,4,5,1]]

# merge_f1_f2_f3.dropna()

