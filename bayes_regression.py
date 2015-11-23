import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

nfeatures = 4
data = np.loadtxt('program_text_features.csv', delimiter = ',', skiprows = 0, usecols=range(1,nfeatures))
X = data[ : , : ]
y = np.array([1 for _ in range(X.shape[0])]) # set speedup to 1 for everything for now

def split_train_test(X, y, fraction_train = 9.0 / 10.0):
    end_train = round(X.shape[ 0 ] * fraction_train)
    X_train = X[ 0 : end_train, ]
    y_train = y[ 0 : end_train ]
    X_test = X[ end_train :, ]
    y_test = y[ end_train : ]
    return X_train, y_train, X_test, y_test

def normalize_features(X_train, X_test):
    mean_X_train = np.mean(X_train, 0)
    std_X_train = np.std(X_train, 0)
    std_X_train[ std_X_train == 0 ] = 1
    X_train_normalized = (X_train - mean_X_train) / std_X_train
    X_test_normalized = (X_test - mean_X_train) / std_X_train
    return X_train_normalized, X_test_normalized

X_train, y_train, X_test, y_test = split_train_test(X, y)
X_train, X_test = normalize_features(X_train, X_test)
X_train = np.concatenate((X_train, np.ones((X_train.shape[ 0 ], 1))), 1)
X_test = np.concatenate((X_test, np.ones((X_test.shape[ 0 ], 1))), 1)


# Augment X, y
invT2 = 10
precision = np.identity(nfeatures) * invT2
cholesky_precision = np.linalg.cholesky(precision)
X_train_aug = np.concatenate((X_train, cholesky_precision), axis=0)
y_train_aug = np.transpose(np.concatenate((y_train, np.zeros(nfeatures))))

# Get QR decomposition of X
Q, R = np.linalg.qr(X_train_aug)
Rinv = np.linalg.inv(R)
RinvQ = np.dot(Rinv,Q.T)
wridge = np.dot(RinvQ, y_train_aug)
print wridge

# Generate test y values
y_test_pred = np.dot(X_test, wridge)

rms = sqrt(mean_squared_error(y_test, y_test_pred))
print rms


