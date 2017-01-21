# -*- coding: utf-8 -*-
#######################################
__file__    = "CaffeClassification.py"
__author__  = "Mesut Pişkin"
__license__ = "GPL"
__version__ = "1.0"
__email__   = "mesutpiskin@outlook.com"
__website__ = "www.mesutpiskin.com"
__status__  = "Development"
__date__    = "21.01.2017"
#######################################
import numpy as np
import matplotlib.pyplot as plt
import caffe

#Ağ bu fonksiyon ile oluşturulacak
def InitCaffe():
	#Sınıflandırma için hangi donanımı kullanacağımızı belirtiyoruz
	#caffe.set_mode_cpu()  #CPU yani işlemci üzerinde
	caffe.set_mode_gpu()  #GPU yani ekran kartı üzerinde 
	model_def = 'deploy.prototxt'
	model_weights = 'bvlc_reference_caffenet.caffemodel' #imagenet model dosyası
	global net
	net = caffe.Net(model_def,      # Modelin yapısını tanımlar
					model_weights,  # Eğitilmiş ağırlıkları içerir
					caffe.TEST)     # Test modunda kullanacağız			
	#Subtraction için ortalama ImageNet görüntüsü yüklenir.
	mu = np.load('ilsvrc_2012_mean.npy')
	mu = mu.mean(1).mean(1)
	#Data adı verilen transformatör giriş için oluşturulur
	global transformer
	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
	transformer.set_transpose('data', (2,0,1))  # Görüntü kanallarını en dışa taşır
	transformer.set_mean('data', mu)            # Her kanaldaki veri seti ortalaması çıkarılır.
	transformer.set_raw_scale('data', 255)      # [0, 1] 'den [0, 255]' e yeniden ölçeklendirme yapılır.
	transformer.set_channel_swap('data', (2,1,0))  # Renk uzayı RGB den BGR renk uzayına dönüştürülür.
	# Girişin boyutunu ayarlanır.
	# Varsayılan olarak kalsın. İsterseniz daha sonra farklı yığın boyutları için değiştirebiliriz
	net.blobs['data'].reshape(50,        # Yığının boyutu
							  3,         # 3 kanallı yani  BGR resimler.
							  227, 227)  # resimlerin boyutu 227x227 olarak ayarlanacak.						  
#Parametre ile gonderilen goruntu analiz edilecek					  
def RecognizeObject(imagePath):        					  
		image = caffe.io.load_image(imagePath)
		transformed_image = transformer.preprocess('data', image)
		#Görüntü verilerini ağ için ayrılan belleğe kopyalıyor
		net.blobs['data'].data[...] = transformed_image
		#Sınıflandırma
		output = net.forward()
		output_prob = output['prob'][0]  # Yığındaki ilk görüntü için çıktı olasılık vektörü
		# Imagenet tarafindan hazirlanan etiket dosyasi
		labels_file = 'synset_words.txt'			
		labels = np.loadtxt(labels_file, str, delimiter='\t')
		return  labels[output_prob.argmax()]
