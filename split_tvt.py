import

 ''' convert text into vectors'''
 ''
 ''

 classifier = LinearSVC(c = 0.1) ''' c = 0.10, c = 0.100: one of these will be the most accurate!
 find through validation set: for hw'''
 classifier.fit(x_train, y_train) ''' <list of vectors>, <list of labels>'''
 classifier.predict(<training examples>)