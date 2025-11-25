import matplotlib.pyplot as plt 
from Functions import num_of_letters
def plot_letter_counts(letter_counts):
    letters = list(letter_counts.keys())
    ounts = list(letter_counts.values())
    plt.figure(figsize=(10, 5))
    plt.bar(letters, counts, color='skyblue')
    plt.xlabel('Litery')
    plt.ylabel('Ilosc w tekscie')
    plt.tittle('Czestotliwosc wystepowania liter w tekscie')
    plt.grid(axis='y' , linestyle='--')
    plt.show()
    
    
text = 'Wizerunki mężczyzn podejrzewanych o dokonanie kradzieży zostały zarejestrowane przez kamerę monitoringu. Funkcjonariusze proszą o kontakt osoby, które rozpoznają obu lub jednego z mężczyzn albo posiadają jakiekolwiek informacje mogące pomóc w ustaleniu ich tożsamości. olicja zapewnia pełną anonimowość wszystkim osobom przekazującym informacje. Śledczy szczegółowo analizują każdy sygnał mogący pomóc w zatrzymaniu sprawców.'
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
'n', 'o', 'u', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
result = num_of_letters(text, letters)
print(result)
plot_letter_counts(result)


