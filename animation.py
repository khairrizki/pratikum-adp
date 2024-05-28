import os
from termcolor import colored, cprint

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

bersihkan_layar()

for i in range(10):
    cprint(" " * 20, 'white', "on_blue", end="")

def cetak_logo_visa():
    v = [
        "V       V",
        " V     V ",
        "  V   V  ",
        "   V V   ",
        "    V    "
    ]
    i = [
        " IIIIII ",
        "   II   ",
        "   II   ",
        "   II   ",
        " IIIIII "
    ]
    s = [
        "  SSSSS ",
        " S      ",
        "  SSSSS ",
        "      S ",
        "  SSSSS "
    ]
    a = [
        "    A    ",
        "   A A   ",
        "  AAAAA  ",
        " A     A ",
        "A       A"
    ]
    
    for j in range(5):
        print(colored(v[j], 'blue'), end="  ")
        print(colored(i[j], 'blue'), end="  ")
        print(colored(s[j], 'blue'), end="  ")
        print(colored(a[j], 'blue'))

print(" " * 30)
cetak_logo_visa()
for i in range(10):
    cprint(" " * 20, 'white', "on_yellow", end="")
print("\n" * 2)
