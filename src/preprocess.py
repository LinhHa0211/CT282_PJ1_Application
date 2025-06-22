import numpy as np

def preprocess(image):
    resized_image = image.resize((224, 224))
    arr = np.array(resized_image).astype("float32") / 255
    return np.expand_dims(arr, axis=0) 
