import numpy as np

def preprocess(image):
    resized_image = image.resize((224, 224))
    return np.array(resized_image).astype("float32") / 255