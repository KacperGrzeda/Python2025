import pandas as pd 
def Wybor_gry_najnisza_cena():
    df_gry = pd.read_excel(ceny_gier.xlsx)
    najtasza_gra = df_gry.loc[df_gry['cena'].idxmin]
    print(f'Najtansza gra to: {najtasza_gra['gra']} za {najtasza_gra['cena']}) zl')

if __name__ == '__main__':
    Wybor_gry_najnisza_cena()
    print('Koniec')


