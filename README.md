# RPS_Classification
Repositori ini berisikan project yang digunakan untuk penilaian penugasan dalam pembelajaran mesin, dalam project ini pelatihan model machine learning berupa pre trained model DenseNet-169 dilakukan dengan mengguanakan dataset RPS (Rock, Paper, Scissoros), dataset tersebut berisi 3 kategori kelas yaitu rock, paper, dan scissors dimana di dalam masing - masing kategori berisikan citra yang merepresentasikan postur rock, paper, scissors. Output yang diharapkan dari project ini merupakan machine learning yang dilatih dapat mengklasifikasikan apakah sebuah citra termasuk rock, paper, atau scissors.

# Author
Ulul Fikri - 202010370311278

# Overview
Pada peroject machine learning yang dilakukan, model Densenet-169 digunakan dan dialatih dengan dataset yang ada.

<img width="600" alt="densenet121_spXhNmT" src="https://github.com/mustarion/RPS_Classification/assets/132191412/4eee1c4a-504d-4c0d-a004-e066d00548e8">

DenseNet (Densely Connected Convolutional Networks) adalah arsitektur jaringan saraf konvolusional (CNN) yang dikembangkan untuk tugas penglihatan komputer. Konsep dasar DenseNet yaitu "densely connected"  memungkinkan setiap lapisan menerima input dari semua lapisan sebelumnya, memungkinkan informasi untuk mengalir lebih efisien melalui jaringan. DenseNet memiliki dua varian utama: DenseNet-121 dan DenseNet-169. DenseNet-169 secara umum dapat memberikan performa yang lebih baik daripada DenseNet-121, terutama pada tugas-tugas yang memerlukan representasi yang lebih dalam dan kompleks dari gambar. Namun, penggunaan DenseNet-169 juga dapat membutuhkan lebih banyak sumber daya komputasi.

# Project Flow
## 1. Laod Dataset
Pada tahapan ini, data yang diperoleh diload kedalam program. Berikut merupakan contoh dari masing - masing citra dalam setiap kategori dataset.

![rps_citra](https://github.com/mustarion/RPS_Classification/assets/132191412/0e6a26f1-85af-4826-a2c7-5e213e0e5675)

## 2. Data Augmentation
Data augmentasi dilakukan untuk mendapat lebih banyak data pada pelatihan yang akan dilakukan, data yang diproleh dari augmentasi yang dilakukan pada project ini bersifat sintetis dengan begitu jumlah data pada dataset tidak berubah. Adapun beberapa parameter dalam proses augmentasi yang dilakukan adalah: rescale=1./255, rotation_range=30, zoom_range=0.2, height_shift_range=0.2, horizontal_flip=True, fill_mode='nearest'. Hasil dari augmentasi dapat dilihat pada gambar dibawah:

![augmentasi](https://github.com/mustarion/RPS_Classification/assets/132191412/fe8de680-104c-465b-a204-98caab324380)

## 3. Machine learning Modeling
Model yang digunakan pada project ini merupakan DenseNet-169. Berikut merupakan summery model dari DenseNet-169:

![Screenshot 2023-12-11 002913](https://github.com/mustarion/RPS_Classification/assets/132191412/1f34d80f-f7b2-472f-881a-3f2f9d8f0b72)

pada model tersebut, dilakukan fine tuning dengan melakukan unfreez pada 2 layer terakhir pada model, dengan begitu 2 layer terakhir akan ikut dilatih kembali. Berikut merupakan implementasi fine tuning pada model pre trained.

![Screenshot 2023-12-11 004356](https://github.com/mustarion/RPS_Classification/assets/132191412/f5ef86c8-bbc7-44b9-8ddd-9b941d3f801f)

Setelah dilakuakn fine tuning pada model, model akan digabungkan dengan fully connected layer yang digunakan untuk memberikan hasil akhir klasifikasi machine learning yang dilakukan. Adapun beberapa layer dalam fully connected layer yang digunakan adalah, GlobalMaxPooling2D(), Dense(512, activation='relu'), Dropout(0.5), Dense(128, activation='relu'), Dropout(0.3), Dense(3, activation='softmax'). Adapun hasil akhir dari model yang digunakan setelah melalui preses fine tuning dan implementasi fully connected layer adalah sebagai berikut:

![Screenshot 2023-12-11 004818](https://github.com/mustarion/RPS_Classification/assets/132191412/8fee96d2-7a43-40ae-a973-4ff6080b487b)

Setelah arsitektur machine learning dibuat, selanjutnyya adalah tahap pelatihan model. pada tahapan ini data dibangi menjadi 3 kategori yaitu data train, data test, dan juga data validation. setelah itu dilakukan pelatihan dengan data train sebagai bahan pelatihan dan data validation sebagai indikator penilaian. Pelatihan model dilakukan sebanyak 5 epoch  pelatihan yang dapat dilihat pada gamabr dibawah ini:

![Screenshot 2023-12-11 090431](https://github.com/mustarion/RPS_Classification/assets/132191412/f5b9e801-ed60-46ab-9b29-1d367b9c6d52)

Hasil dari pelatihan dapat dilihat pada graf berikut:

![augmentasi](https://github.com/mustarion/RPS_Classification/assets/132191412/44d1c176-8794-4a72-95fd-7f5953bd9a1d)

Dari pelatihan yang dilakukan dapat diliaht bahwa model yang dilatih memiliki masih memiliki gap dengan validation pada masing - masing parameter akurasi maupun loss, namun dari graf yang ditampilkan dapat disumsikan hanya dibutuhkan epoch yang lebih banyak agar gap antra parameter dengan validatationnya bisa semakin mengecil. 

![Screenshot 2023-12-11 092712](https://github.com/mustarion/RPS_Classification/assets/132191412/aeaa5d6e-1942-41be-b854-269f7503509a)

Dari penelitian yang dilaukan memberikan hasil akurasi sebesar 99.6%, hasil yang didapat menunjukkan bahwa model yang dilatih sudah cukup baik.


