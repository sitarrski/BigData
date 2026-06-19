import pandas as pd

try:
    piosenki = pd.read_csv('unique_tracks.txt', sep='<SEP>', header=None,
                     names=['track_id', 'song_id', 'artist_name', 'song_title'],
                     engine='python', encoding='ISO-8859-1')

    trojki = pd.read_csv('triplets_sample_20p.txt', sep='<SEP>', header=None,
                       names=['user_id', 'track_id', 'date'],
                       engine='python', encoding='ISO-8859-1') # jest czesc encoding, bo moga wystepowac znaki spoza
                                                               # kodowania UTF-8
    print("Dane wczytane")
except UnicodeDecodeError as e: # zapobiegamy wykrzaczeniu sie programu w razie problemow z roznymi znakami
    print(f"Wystepuje blad: {e}")

for col in piosenki.columns: # zamieniamy dane na tekst tak aby funkcja strip zadzialala prawidlowo, za pomoca strip
    # usuwamy wszelkie spacje miedzy i po tytulach, nazwach artystow itd.
    piosenki[col] = piosenki[col].astype(str).str.strip()
for col in trojki.columns:
    trojki[col] = trojki[col].astype(str).str.strip()

trojki['date'] = pd.to_numeric(trojki['date'], errors='coerce') # konwersja daty, coerce zamienia niepoprawne wartosci
# na wartosci NaN (brak danych)
trojki['date'] = pd.to_datetime(trojki['date'], unit='s') # zmiana jednostek z unix tak aby byla data

print(piosenki.isnull().sum()) # sprawdzamy braki

piosenki_duplikat = piosenki.drop_duplicates(subset=['song_id']) # usuwamy mozliwe powtorzenia piosenki (jedna piosenka moze miec
                                                     # kilka song_id
df = pd.merge(trojki, piosenki_duplikat, left_on='track_id', right_on='track_id', how='inner') # laczymy zbiory dla analizy

najpop = df.groupby(['artist_name','song_title']).size().sort_values(ascending=False).head(10)
print("10 najpopularniejszych piosenek z danych:")
for (artysta, tytul), ile in najpop.items():
    print(f"{artysta} - {tytul}: {ile}")

uzytkownicy = df.groupby('user_id')['song_id'].nunique().sort_values(ascending=False).head(10)
print("Top 10 uzytkownikow:")
for uzytkownik, ile in uzytkownicy.items():
    print(f"{uzytkownik} - {ile}")

top_artysta = df['artist_name'].value_counts()
if not top_artysta.empty:
    artysta_nazwa = top_artysta.index[0]
    artysta_ile = top_artysta.iloc[0]
    print(f"Najpopularniejszy artysta: {artysta_nazwa}\nLiczba odtworzen: {artysta_ile}")

df['month'] = df['date'].dt.month
miesieczne = df['month'].value_counts().reindex(range(1,13), fill_value=0).sort_index()
print("Ranking w podziale na miesiace:")
for miesiac, ile in miesieczne.items():
    print(f"{int(miesiac)} - {int(ile)}")

piosenki_queen = df[df['artist_name'] == 'Queen'].groupby('song_id').size().nlargest(3).index.tolist()
fani_queen = df[df['song_id'].isin(piosenki_queen)].groupby('user_id')['song_id'].nunique()
lista_fanow = fani_queen[fani_queen == 3].index.tolist()
lista_fanow.sort()

for id_fan in lista_fanow[:10]:
    print(id_fan)

print(f"Ilosc uzytkownikow: {len(lista_fanow)}")


