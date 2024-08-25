from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import cv2
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# loading pre-trained model
model = MobileNetV2(weights='imagenet')

WASTEFUL_PRODUCTS = [
    'plastic_bottle', 'plastic_bag', 'styrofoam', 'packaging', 'plastic_cutlery',
    'plastic_straws', 'plastic_wrap', 'plastic_cups', 'plastic_bowls', 'polystyrene',
    'disposable_diapers', 'cotton_balls', 'cotton_swabs', 'tissue_paper', 'kitchen_towels',
    'fast_food_wrappers', 'plastic_clothing', 'single_use_cups', 'plastic_menus', 'packet'
]
RECYCLABLE_PRODUCTS = [
    'glass_bottle', 'aluminum_can', 'paper', 'cardboard', 'metal', 'plastic_bottle',
    'plastic_container', 'paper_bag', 'newspaper', 'magazines', 'book', 'cardboard_box',
    'tetra_pak', 'aluminum_foil', 'steel_can', 'cereal_box', 'milk_carton', 'egg_carton',
    'plastic_jug', 'plastic_jar', 'plastic_container', 'carton', 'safety_pin', 'hook', 'toilet_tissue'
]

camera = cv2.VideoCapture(0)

last_update_time = time.time()
update_interval = 2  

def classify_frame(frame):
    img = cv2.resize(frame, (224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0]
    label = decoded_preds[0][1]
    confidence = decoded_preds[0][2]
    return label, confidence

def generate_frames():
    global last_update_time
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            label, confidence = classify_frame(frame)

            current_time = time.time()
            if current_time - last_update_time >= update_interval:
                if confidence >= 0.2:
                    if label in WASTEFUL_PRODUCTS:
                        classification_text = f'ITEM STATUS: WASTE'
                    elif label in RECYCLABLE_PRODUCTS:
                        classification_text = f'ITEM STATUS: RECYCLABLE'
                    else:
                        classification_text = f'ITEM STATUS: OTHER'
                else:
                    classification_text = 'ITEM STATUS: UNKNOWN'

                # Send classification result to client via SocketIO
                socketio.emit('classification', {'text': classification_text})

                # Update the last update time
                last_update_time = current_time
            else:
                # If not time to update, use the last classification text
                classification_text = 'ITEM STATUS: UNKNOWN'

            # Encode frame as JPEG and yield for streaming
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def landing_page():
    return render_template('landing.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    socketio.run(app, debug=True)
