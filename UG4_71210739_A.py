import json

a = int(input("Masukan jumlah barang = "))
# data = dict()

barang = []
total = 0
for x in range(a):
    nomor = x + 1
    barangNama = str(input(f'Nama Barang {nomor} = '))
    barangHarga = int(input(f'Harga Barang {nomor} = '))

    barang.append({
        "nama": barangNama,
        "harga": barangHarga
    })

    total = total + barangHarga

    print("\n")

data = dict({
    "total": total,
    "barang": barang
})

# print(data)
with open('data.json', 'w') as datafile:
    json.dump(data, datafile)
