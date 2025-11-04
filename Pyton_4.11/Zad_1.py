def sprawdz_BMI(bmi):
    if bmi < 16:
        print('wygłodzenie')
    elif 16 <= bmi < 17:
        print('wychudzenie')
    elif 17 <= bmi < 18.5:
        print('niedowaga')
    elif 18.5 <= bmi < 25:
        print('Waga prawidłowa')

sprawdz_BMI(16.5)
sprawdz_BMI(16.5)
sprawdz_BMI(17.1)
sprawdz_BMI(24)