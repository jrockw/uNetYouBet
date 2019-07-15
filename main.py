from model import *
from data import *
from PIL import Image
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"
Image.MAX_IMAGE_PIXELS = 999999999

#data_gen_args = dict(rotation_range=0.2,
#                    width_shift_range=0.05,
#                    height_shift_range=0.05,
#                    shear_range=0.05,
#                    zoom_range=0.05,
#                    horizontal_flip=True,
#                    fill_mode='nearest')
data_gen_args = dict()

myGene = \
    trainGenerator(2,'data/train','image','label',data_gen_args,save_to_dir
               = None)
#you will see 60 transformed images and their masks in data/membrane/train/aug
#num_batch = 3
#for i,batch in enumerate(myGene):
#    if(i >= num_batch):
model = unet()
model_checkpoint = ModelCheckpoint('unet_membrane.hdf5', monitor='loss',verbose=1, save_best_only=True)
model.fit_generator(myGene,steps_per_epoch=300,epochs=5,callbacks=[model_checkpoint])

testGene = testGenerator("data/he")
results = model.predict_generator(testGene,2000,verbose=1)
saveResult("data/test/out",results)
