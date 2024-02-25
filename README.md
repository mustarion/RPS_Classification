# RPS_Classification
This project is intended for my assignment in my machine learning class. This project used Pre-Trained model DenseNet-169 and trained on the RPS (Read, Paper, Scissor) dataset to produce a model that can classify the Rock, Paper, and Scissors. 

## Dataset
Dataset being used in this project is based on " RPS (Read, Paper, Scissor) " dataset from https://www.kaggle.com/datasets/frtgnn/rock-paper-scissor. The dataset contain multiple categories such rock, paper, scissors with each categories contain of 840 images.


## Pre-Trained Model
Pretrained model is machine learning model that has been trained on large scale dataset and can be fine-tuned for specfic task. in this project, DenseNet-169 is trained using the adjusment of trashnet dataset to provide classification result.

<img width="600" alt="densenet121_spXhNmT" src="https://github.com/mustarion/RPS_Classification/assets/132191412/4eee1c4a-504d-4c0d-a004-e066d00548e8">

DenseNet (Densely Connected Convolutional Networks) is a convolutional neural network (CNN) architecture developed for computer vision tasks. The fundamental concept of DenseNet is "densely connected," allowing each layer to receive input from all previous layers, enabling information to flow more efficiently through the network. DenseNet has two main variants: DenseNet-121 and DenseNet-169. Generally, DenseNet-169 can provide better performance than DenseNet-121, especially in tasks requiring deeper and more complex image representations. However, the use of DenseNet-169 may also require more computational resources.

## Evaluation
To determind the quality of the conducted classification, several matriks evaluation are being used such:
- accuracy
- precision
- recall
- f1-score
- support
  
Those evalutaioin matriks conducted in order to determine is the classification result considered good or still need to be improved.


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


