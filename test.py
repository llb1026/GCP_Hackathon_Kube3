import keras
import numpy as np
from keras.applications import resnet50
#Load the ResNet50 model
resnet_model = resnet50.ResNet50(weights='imagenet')
# input image must be size 224x224
#C:\_train_data
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
from PIL import Image
# --------------------------------------------------------- #
filename = "images/plant.jpeg"
original = load_img(filename, target_size=(224, 224))
#print('PIL image size',original.size)
#plt.imshow(original)
#plt.show()
numpy_image = img_to_array(original)
#plt.imshow(np.uint8(numpy_image))
#plt.show()
#print('numpy array size',numpy_image.shape)
image_batch = np.expand_dims(numpy_image, axis=0)
#print('image batch size', image_batch.shape)
#plt.imshow(np.uint8(image_batch[0]))
# --------------------------------------------------------- #
processed_image = resnet50.preprocess_input(image_batch.copy())
# get the predicted probabilities for each class
predictions = resnet_model .predict(processed_image)
print(predictions)
# convert the probabilities to class labels