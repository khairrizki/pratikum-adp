def konversi_suhu_celsius(suhu):
    batas_suhu_c = (0, 100)  

    if not (batas_suhu_c[0] <= suhu <= batas_suhu_c[1]):
        return "Suhu yang Anda inputkan tidak sesuai dengan batas suhu Celcius."

    reaumur = suhu * 4/5
    fahrenheit = (suhu * 9/5) + 32
    kelvin = suhu + 273.15

    output = f"""
    Suhu {suhu} derajat Celcius dapat dikonversi menjadi:
    
    Satuan Suhu || Derajat Suhu
    --------------------------------
    Reaumur     || {reaumur:.2f}
    Fahrenheit  || {fahrenheit:.2f}
    Kelvin      || {kelvin:.2f}
    """

    return output

suhu_input = float(input("Masukkan suhu dalam Celcius: "))
print(konversi_suhu_celsius(suhu_input))