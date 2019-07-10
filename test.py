from model import *
from data import *

#create model from ours, then load weights
test_model = unet('unet_membrane.hdf5')


testData = testGenerator("data/he")
result = test_model.predict_generator(testData,2024,verbose=1)
saveResult("data/test/out",result)

