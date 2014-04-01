#Machine learning introduction with Eric and Danny

## What is machine learning: Some definitions

###Cross validation:
Definition supervised learning:

Supervised learning occurs when your break your data set into "training" and "validation" portions.  

Definition unsupervised learning:

Unsupervised learning occurs when you only run your model once on the whole data set.

###Label:
Definition label: A label is a specific outcome for a piece of training data.

Example (linear regression):

Say we have a bunch of data points with both x and y values.  So every x has a corresponding y relating them. Now say we want to draw a line approximating a function for all of the data points.  One way to do this is with linear regression.  The result of linear regression is an equation of the form:

y_hat = alpha*x + beta

Where y_hat is the result of the linear regression on not the individual y's for each data point.

So for example say you're linear regression produces the following line:

       	       	   y_hat = 5*x + 7

Now we compare how this alpha and beta, which necessarily produce y_hat, with the true value for y in each case.  

The true y for each x is the label in this case.

Say we had the following data:

x   y
2   17
3   17
4   54
17  205
9   54

jump to python example with statsmodels

###python code:
## unsupervised learning 
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import pylab 

\#Load data
url = 'http://vincentarelbundock.github.io/Rdatasets/csv/HistData/Guerry.csv'
dat = pd.read_csv(url)

\# Fit regression model (using the natural log of one of the regressors)
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

\# Inspect the results
print results.summary()

dat.plot()
pylab.show()

\#Load data
url = 'http://vincentarelbundock.github.io/Rdatasets/csv/HistData/Guerry.csv'
dat = pd.read_csv(url)

training, testing = np.array_split(dat,2)

\# supervised learning 
# Fit regression model (using the natural log of one of the regressors)
results_training = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=training).fit()

results_testing = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=testing).fit()


\# Inspect the results
print results_training.summary()

print results_testing.summary()

dat.plot()
pylab.show()


Example (naive bayesian classification):

Say we have two pieces of text with the following labels:

"hi I really like you" , "acceptable"
"You are such a dick", "unacceptable"

In this case, the labels are acceptable and unacceptable, which will be produced for pieces of text as those shown above.  The naive bayesian classifier need not be for binary labels.  Labels can take on N many values as the first example illustrats.

jump to python example with textblob
#Python

http://stevenloria.com/how-to-build-a-text-classification-system-with-python-and-textblob/


###Scoring function:

Defintion scoring function: A scoring function is a way of validating that your model is actually improving.  So an example of metric that means your "fit" is getting better is R^2.


###Overfitting:

Definition overfitting: A model is overfit to the sample data if it appears to fit the sample data very well but cannot fit any new data well.

Example: (go to the board)

###information gain:

(Fill in the blank)
 