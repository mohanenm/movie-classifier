# movie-review-classifier
used NLTK to classify movie reviews as positive or negative(sentiment analysis hw for nlp course). 

### How to use 
 
##### 1. install Natural langauge Toolkit Mac/Linux, run 'sudo pip install -U nltk'
##### 2. In Terminal clone from GH, 'git clone https://github.com/mohanenm/movie-classifier'
##### 3. run, on the command line, 'python ./classifier.py'
##### 4. wait a bit and get your results
##### 5. Fork and Modify it! 

### How to mess with it

#### 1. Fork it, make it your own 
#### 2. Look at the comments on where to test different reviews
#### 3. email me with any questions

### Code source
#### 1. https://www.twilio.com/blog/2017/09/sentiment-analysis-python-messy-data-nltk.html
#### 2. NLTK DOCUMENTATION

#### You will be working with movie review data, which you can download here:https://github.com/dennybritz/cnn-text-classification-tf/tree/master/data/rt-polaritydata
 * find two files there (one with positive and one with negative reviews).
 * build a binary classifier that will perform movie review classifica-tion automatically.
 * 1.split data randomly into training (70%), development (15%)and test (15%) sets. (10 points)
 * 2.Download and install LibSVM from https://www.csie.ntu.edu.tw/~cjlin/libsvm/.
    Convert the sentiment data into LibSVM sparse format. (30points) 
    find some guidelines by following these links:https://www.csie.ntu.edu.tw/~cjlin/libsvm/faq.html#/Q03:_Data_preparationhttps://stats.stackexchange.com/questions/61328/libsvm-data-format 
 * 3.Use LibSVM command-line tools such as svm-train and svm-predict totrain and evaluate a linear SVM model on your development set. 
   Tune alinear SVM by trying a few different C values such as 0.0001, 0.001, . . . ,1000, 10000 on thedevelopmentset. 
 * Report the accuracy you obtainedfor each model. (30 points)4.Evaluate your best model on the test set. Report the final accuracy ofyour model on thetestset. (30 points)
