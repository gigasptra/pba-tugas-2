from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from multiprocessing import Process
import time

def stemming(file,i):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    teks_stem = stemmer.stem(file)

    # path tujuan penyimpanan file
    stem_file = f'C:/Users/ASUS/IdeaProjects/Python/src/NLP/File Stemming/file_stem_{i}mb.txt'
    with open(stem_file,'w') as s:
        s.write(teks_stem)

    print(f'Result:success! file_stem{i}mb.txt saved')


if __name__ == "__main__" :
    # daftar file yang akan distemming
    files = ['10mb.txt','15mb.txt','20mb.txt']

    # input opsi proses yang akan dilakukan
    option_process = int(input('Pilih Proses Stemming \n1. Stemming tanpa Multiprocessing \n2. Stemming dengan Multiprocessing \nMasukkan Pilihan (angka) : '))

    proc = []
    i=10 # indentasi untuk penomoran file hasil

    start = time.perf_counter() # awal perhitungan waktu pemrosesan
    for file in range(len(files)):
        if option_process == 1: # Stemming tanpa Multiprocessing
            with open('C:/Users/ASUS/IdeaProjects/Python/src/NLP/File Proses Stemming/'+files[file], 'r') as p:
                openFile = p.read()
            stemming(openFile,i)

        elif option_process == 2: # Stemming dengan Multiprocessing
            with open('C:/Users/ASUS/IdeaProjects/Python/src/NLP/File Proses Stemming/'+files[file], 'r') as p:
                openFile = p.read()
            m = Process(target=stemming, args=(openFile,i))
            proc.append(m)

        i += 5

    for p in proc:
        p.start()

    for p in proc:
        p.join()

    # akhir perhitungan waktu pemrosesan
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,4)} seconds(s)')

