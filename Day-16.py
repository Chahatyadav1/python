import pandas
letter=[]
code=[]
df=pandas.read_csv("nato_phonetic_alphabet.csv")
for (index,row) in df.iterrows():
    code.append(row.code)
    letter.append(row.letter)
    # letter.append(row.to_list())
    # print(type(row.code))
    # code.append(row.code.to_list())
print(letter)
print(code)
