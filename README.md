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
For the first step, load dataset into the program. This is the example of the dataset being loaded:

![rps_citra](https://github.com/mustarion/RPS_Classification/assets/132191412/0e6a26f1-85af-4826-a2c7-5e213e0e5675)

## 2. Data Augmentation
Augmentation is a method to increase the number of data in a dataset. This method works by synthetically enlarging the data inside the dataset, so the added data does not affect the actual number of data in the dataset. Some of the parameter being used in augmentation include: 
-	rescale=1./255
-	rotation_range=30
-	zoom_range=0.2
-	height_shift_range=0.2
-	horizontal_flip=True
-	fill_mode='nearest'
the augmentation result can be seen down here:

![augmentasi](https://github.com/mustarion/RPS_Classification/assets/132191412/fe8de680-104c-465b-a204-98caab324380)

## 3. Machine learning Modeling
In this step we construct the machine learning model architecture to be trained on the RPS dataset. The Pre-Trained model being used in this project is DenseNet-169. Here is the summary of the DenseNet-169 model’s:

![Screenshot 2023-12-11 002913](https://github.com/mustarion/RPS_Classification/assets/132191412/1f34d80f-f7b2-472f-881a-3f2f9d8f0b72)

The model used being fine toned with unfreezing 2 layers in the end of the model layers. Unfreezing 2 layers will make it trainable, so the layers can be trained with the new task which is training on the RPS dataset. The fine tuning proses result can be seen down here:

![Screenshot 2023-12-11 004356](https://github.com/mustarion/RPS_Classification/assets/132191412/f5ef86c8-bbc7-44b9-8ddd-9b941d3f801f)

After fine toned the model, the models being merge with fully connected layer. Fully connected layer are used to connect the learned representation with the desired output, usually this kind of layer are used in the end of the machine learning architecture model’s. the several layers in the fully connected layer used are:
-	GlobalMaxPooling2D()
-	Dense(512, activation='relu')
-	Dropout(0.5)
-	Dense(128, activation='relu')
-	Dropout(0.3)
-	Dense(3, activation='softmax')
The final result of the machine learning architecture model being used can be seen down here as a summary model:

![Screenshot 2023-12-11 004818](https://github.com/mustarion/RPS_Classification/assets/132191412/8fee96d2-7a43-40ae-a973-4ff6080b487b)

The next step is training the model, the dataset (loaded data + augmented data) split into 3 sub dataset such as data train, data validation, and data test. the training process conducted by using data train as the training material and data test as the evaluation indicator. Training is conducted for a total 5 training epochs, as showing below:

![Screenshot 2023-12-11 090431](https://github.com/mustarion/RPS_Classification/assets/132191412/f5b9e801-ed60-46ab-9b29-1d367b9c6d52)

The result can be seen down here:

![augmentasi](https://github.com/mustarion/RPS_Classification/assets/132191412/44d1c176-8794-4a72-95fd-7f5953bd9a1d)

![Screenshot 2023-12-11 092712](https://github.com/mustarion/RPS_Classification/assets/132191412/aeaa5d6e-1942-41be-b854-269f7503509a)

From the graph and result above, can be seen that the accuracy can reach up to 99%, but there is still a gap between the training result and validation both in the accuracy and the loss evaluation. That’s mean, the model still get overfitting even the accuracy of the model considered to be good.


