import numpy as np
from keras.models import load_model

class ModelLoader:
    def __init__(self) -> None:
        self.__model_1 = load_model("src/models/Model_V1.keras")
        self.__model_2 = load_model("src/models/Model_V2.keras")
        self.__model_3 = load_model("src/models/Model_V3.keras")
        self.__model_4 = load_model("src/models/Model_V4.keras")
        self.__d = {
            "V1": self.__model_1,
            "V2": self.__model_2,
            "V3": self.__model_3,
            "V4": self.__model_4
        }

    def get_model(self, version: str):
        return self.__d[version]
    
    def get_all_versions(self):
        return self.__d.keys()
        
class Predictor:
    def __init__(self) -> None:
        self.__d = {
            0: "Lễ hội Đua Ghe Ngo",
            1: "Hội Lim",
            2: "Lễ hội Hùng Vương",
            3: "Lễ hội Vía Bà Chúa Xứ Núi Sam",
        }

    def predict(self, keras_model, X_test):
        probs = keras_model.predict(X_test)
        predicted_class = np.argmax(probs, axis=1)[0]
        return self.__d[predicted_class]