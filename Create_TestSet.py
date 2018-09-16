## To create a test set from Downloaded data set
## This function has been tested with Download_Dataset module instead of
## git_pull_Datasets
import Download_Dataset
#import Stratified_test_train_set
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

housing = Download_Dataset.load_housing_data()
# below function commented out as sklearn used
#def split_train_test(data, test_ratio):
#    shuffled_indices = np.random.permutation(len(data))
#    test_set_size = int(len(data)*test_ratio)
#    test_indices = shuffled_indices[:test_set_size]
#    train_indices = shuffled_indices[test_set_size:]
#    return data.iloc[train_indices], data.iloc[test_indices]

#housing = Stratified_test_train_set.stratify()
housing["income_cat"]=np.ceil(housing["median_income"]/1.5)
housing["income_cat"].where(housing["income_cat"]<5,5.0,inplace=True)

#below method is to generate random test and train indices
#train_set,test_set = split_train_test(housing, 0.2)
#train_set, test_set = train_test_split(housing, test_size = 0.2, random_state = 42)
#print(len(train_set)), "train +", len(test_set), "test"

##below method is to create stratified test and train data
split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
##below method to create a stratified sampled test data for income category proportions
print(strat_test_set["income_cat"].value_counts()/len(strat_test_set))

##create a copy of trian set and plot the data for visualization 
housing = strat_train_set.copy()
housing.plot(kind = "scatter", x="longitude", y="latitude", alpha =0.4, s=housing["population"]/100, label="population", figsize=(10,7), c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,)
plt.show()
plt.legend()
