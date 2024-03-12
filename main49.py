def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)

liczba = 5
wynik = silnia(liczba)
print("Silnia z", liczba, "to:", wynik)
