# Cat Breed Image Classification

### **Why Cat Breed Image Classification**
---
There are many cat owners who don't know the breed of their own cat. They're several stray, uncared for cats whose breed alre alsso unknown. The goal of this project was to help people know what kind of cat they have. We will usse an image classifier to figure out what breed of cat is in the photo that the user uploads. 

### **Dataset**
---
Data found in Kaggle: https://www.kaggle.com/datasets/ma7555/cat-breeds-dataset

Detailed description of data:
- ID: unique pet identifier number
- URL: website url of the photo
- Type: the type of animal (cat)
- Age: the age of the cat
- Gender: the cat's gender
- Size: the size of the photo
- Coat: cat's coat characteristic (25133 missing values)
- Breed: cat's breed 
- Photos: url link to the image of the cat in small, medium, large (has bad url that no longer work)
- Med-photos: medium sized photos of 1 cat in URL mode


### **Project Progress**
---
We utilized PCA to do the following: 
- To perform feature extraction which helps reduce the training data
- To recreate the cat images

### **Model**
---
Utilized Support Vector Machine (SVM) and Convolutional Neural Netowrk (CNN). We received an evaulation of 84% accuracy rate for 3 breeds: bombay, siamese, and tabby. 

### **Cat Breed Image Classification in Action**
---
We used Streamlit to create a website application. We utilized pickle library to create a pickle file for our model. We then implemented our model on a file uploader that the user will use, to upload an image of cats. 


### **RESOURCES:**
---
1. Tensorflow/Keras: 
  - Installing Tensorflow: https://www.tensorflow.org/install/pip
  - https://www.tensorflow.org/guide
  - https://keras.io/about/
  - https://www.geeksforgeeks.org/introduction-to-tensorflow/
  - https://machinelearninggeek.com/keras-tutorial-for-beginners/
 
2. Image Classification: 
  - https://www.tensorflow.org/tutorials/images/classification

3. Neural Network Image Classification: 
  - https://www.youtube.com/watch?v=Gz_PsRRxrHM
  - https://www.youtube.com/watch?v=t0EzVCvQjGE
  - https://www.youtube.com/watch?v=4jDAKS2V3jY [Part 1]
  - https://www.youtube.com/watch?v=57sdqEd48Fc [Part 2]
  - https://www.youtube.com/watch?v=Fv1cvFEYPwA [Part 4]
  - https://stackabuse.com/image-recognition-in-python-with-tensorflow-and-keras/
  - https://www.geeksforgeeks.org/python-image-classification-using-keras/
