
def f(x):
    if x >= 0:
        return 3*x**2 + 7*x -2
    else:
        return 2*x**2 - 5*x - 4
def g(x):
    return f(x)**2 - f(x)**0.5

def h(x):
    return f(x)*g(x)

def main():
    while True:
        n = int(input("Masukkan jumlah nilai x: "))
        
        tabel = [["Nomor", "x", "f(x)", "g(x)", "h(x)"]]
        for i in range(n):
            x = float(input(f"Masukkan nilai x ke-{i+1}: "))
            baris = [i+1, x, f(x), g(x), h(x)]
            tabel.append(baris)
        
        for baris in tabel:
            print("\t".join(map(str, baris)))
        
        lanjutkan = input("Lanjutkan? (Y/N): ")
        if lanjutkan.lower() != 'y':
            break

if __name__ == "__main__":
    main()

