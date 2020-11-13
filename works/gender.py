#genderai

from tensorflow.python.keras.applications.vgg16 import preprocess_input
from works.utils import load_random_imgs, show_test_samples
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.image import img_to_array, load_img
from ebikazuki.settings_dev import BASE_DIR
import numpy as np

# modelへ保存データを読み込み
model = load_model(BASE_DIR+'/works/studied_model_lite.h5')

def gender(Img):
    # 評価の実施
    #test_data_dir = BASE_DIR+'/works/img/male_female/test2'
    #x_test, true_labels = load_random_imgs(test_data_dir, seed=1)
    img_data = load_img(Img, target_size=(224, 224))
    x_test = np.array([img_to_array(img_data)])
    true_labels = ["None"]
    x_test_preproc = preprocess_input(x_test.copy())/255.
    probs = model.predict(x_test_preproc)

    # 学習画像を取り込むジェネレータを作成。それぞれのパラメータを設定
    img_gen = ImageDataGenerator(
        rescale=1/255.,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        preprocessing_function=preprocess_input
    )

    return probs[0][0]