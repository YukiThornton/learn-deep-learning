import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_save(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.save("output/ch03_mnist_show.png", "PNG")

def get_any_image():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    img = x_train[0]
    label = t_train[0]
    print("label: " + str(label))
    print(img.shape)
    img = img.reshape(28, 28)
    print(img.shape)
    return img
