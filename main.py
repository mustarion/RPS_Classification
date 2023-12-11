from flask import Flask
import os
import tensorflow as tf
import numpy as np
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import skimage
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

app.config['UPLOAD_FOLDER'] = './static/uploads/'

cnn_model = tf.keras.models.load_model(STATIC_FOLDER  + "/model_modul.h5")

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route("/classify", methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        try:
            file = request.files["image"]
            upload_image_path = os.path.join(dir_path,'static','uploads', secure_filename(file.filename))
            print(upload_image_path)
            file.save(upload_image_path)
        except FileNotFoundError:
            return render_template("home.html")    
        label,prob = classify(cnn_model, upload_image_path) 
    else:
        return render_template("home.html")
    return render_template(
        "class.html", image_file_name=file.filename, label=label, prob=prob
    )

def classify(model,image):
    class_names = ['paper', 'rock', 'scissors']
    new_image = plt.imread(image)
    resize_img = skimage.transform.resize(new_image, (150,150,3))
    pred = model.predict(np.array([resize_img]))
    list_index = [0,1,2]
    x = pred
    labels = []
    classified = []
    for i in range(3):
        for j in range(3):
            if x[0][list_index[i]] > x[0][list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    
    for i in range(2):
        label = class_names[list_index[i]]
        labels.append(label)
        classified_prob = round(pred[0][list_index[i]] * 100,2)
        classified.append(classified_prob)
    return labels, classified

@app.route("/classify/<filename>")
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
 
    app.run()