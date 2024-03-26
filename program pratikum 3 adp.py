def main():
    n = int(input("Masukkan nilai n: "))

    if 3 <= n <= 199 and not (100 <= n <= 109):
        f1, f2 = 1, 1
        sigma = 2  

        for _ in range(3, n + 1):
            f1, f2 = f2, f1 + f2
            sigma += f2

        print("Bilangan Fibonacci ke", n, "adalah:", f2)
        print("Jumlah induksi dari f(1) hingga f(", n, ") adalah:", sigma)
    else:
        print(n)

if __name__ == "__main__":
    main()
