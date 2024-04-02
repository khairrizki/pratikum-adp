def ganti_vokal(lirik):
    vokal = 'aeiou'
    lirik_baru=''.join( 'i' if char in vokal else char for char in lirik)
    print("Lirik baru:",lirik_baru)
lirik_lagu = input("Masukkan lirik lagu: ")
ganti_vokal(lirik_lagu)
