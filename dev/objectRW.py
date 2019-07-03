try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

import os

def saveObject(obj, filename):
    if isPkl(filename):
        makePath(filename)
        with open(filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    else:
        print("file must end with .pkl")

def loadObject(filename):
    if isPkl(filename):
        try:
            with open(filename, 'rb') as obj
                return pickle.load(obj)
        except:
            print("Could not open", filename)
    else:
        print("file must end with .pkl")

def makePath(path):
    os.makedirs(path) if not os.path.exists(path) else True

def isPkl(path):
    return path.endswith('.pkl')
