import pandas as pd

df_nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index,row in df_nato.iterrows()}

word = input("Enter a word")

print([nato_dict[alphabet.upper()] for alphabet in word])
