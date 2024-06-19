# Token
subjek = ["saya", "kamu", "dia", "mereka", "kita"]
predikat = ["makan", "minum", "baca", "tulis", "lihat"]
objek = ["nasi", "air", "buku", "surat", "gambar"]
keterangan = ["di rumah", "di sekolah", "di kantor", "di pasar", "di taman"]

def token(word):
    if word in subjek:
        return 'S'
    elif word in predikat:
        return 'P'
    elif word in objek:
        return 'O'
    elif word in keterangan:
        return 'K'
    else:
        return None

# Input User
kalimat = input('Masukkan 1 kalimat : ').lower()
kata_kata = kalimat.split()

# Menggabungkan kata-kata yang mungkin membentuk keterangan
i = 0
tokens = []
while i < len(kata_kata):
    if i < len(kata_kata) - 1 and f"{kata_kata[i]} {kata_kata[i+1]}" in keterangan:
        tokens.append('K')
        i += 2
    else:
        t = token(kata_kata[i])
        if t is not None:
            tokens.append(t)
        i += 1

print("Tokens:", tokens)

# Validasi struktur kalimat
if len(tokens) < 2:
    print("Kalimat tidak valid ( Minimal terdiri dari Subjek dan Predikat )")
else:
    if tokens[0] == 'S':
        if tokens[1] == 'P':
            if len(tokens) == 2:
                print("Kalimat valid.")
            elif len(tokens) > 2:
                if tokens[2] == 'O':
                    if len(tokens) == 3:
                        print("Kalimat valid.")
                    elif len(tokens) == 4 and tokens[3] == 'K':
                        print("Kalimat valid.")
                    else:
                        print("Kalimat tidak valid (Struktur tidak sesuai).")
                elif tokens[2] == 'K' and len(tokens) == 3:
                    print("Kalimat valid.")
                else:
                    print("Kalimat tidak valid (Struktur tidak sesuai).")
        else:
            print("Kalimat tidak valid (Predikat tidak ditemukan setelah Subjek).")
    else:
        print("Kalimat tidak valid (Subjek harus di awal).")
