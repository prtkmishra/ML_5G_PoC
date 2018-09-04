## Downloading and presenting an online data using urllib
## To run script on Jupyter uncomment lines as mentioned
import os
import tarfile
import ssl
#%pylab                                             #Jupyter
#%matplotlib inline                                 #Jupyter
import matplotlib.pyplot as plt
import pandas as pd

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
   getattr(ssl, '_create_unverified_context', None)):
   ssl._create_default_https_context = ssl._create_unverified_context

from six.moves import urllib
download_root = "https://github.com/ageron/handson-ml/raw/master/"
housing_path = "datasets/housing"
housing_url = download_root+housing_path+"/housing.tgz"


def fetch_housing_data(house_url = housing_url, house_path = housing_path):
   if not os.path.isdir(house_path):
       os.makedirs(house_path)
   tgz_path = os.path.join(house_path, "housing.tgz")
   urllib.request.urlretrieve(house_url, tgz_path)
   housing_tgz = tarfile.open(tgz_path)
   housing_tgz.extractall(path=house_path)
   housing_tgz.close()
fetch_housing_data()

def load_housing_data(housing_path=housing_path):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


housing = load_housing_data()
#print (housing.head())
#print (housing.info())
#print (housing["ocean_proximity"].value_counts())
#print (housing.describe())
#housing.hist(housing['longitude'],bins=50)
plt.hist(housing['total_rooms'], bins=50)
#plt.hist(x, bins=50)
#plt.hist(x)

plt.show()                                                  #Not required by Jupyter
