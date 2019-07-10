from main import * 

test_model = keras.models.load_model('unet_membrane.hdf5')


testData = testGenerator("data/he")
result = test_model.predict_generator(testGene,440,verbose=1)
saveResults("data/test/out",results)

