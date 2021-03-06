teori = int(input('Nilai Ujian Teori : '))
praktek = int(input('Nilai Ujian Praktek : '))
if teori >= 70 and praktek >= 70:
    print('Selamat, anda lulus!')
elif teori >= 70 and praktek < 70:    
    print('Anda harus mengulang ujian praktek.')
elif teori < 70 and praktek >= 70:
    print('Anda harus mengulang ujian teori.')
elif teori and praktek < 70:
    print('Anda harus mengulang ujian teori dan praktek.')