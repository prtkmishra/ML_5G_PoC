## To create a test set from Downloaded data set
## This function has been tested with Download_Dataset module instead of
## git_pull_Datasets
import Download_Dataset
import numpy as np

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data)*test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
housing = Download_Dataset.load_housing_data()
train_set,test_set = split_train_test(housing, 0.2)
print(len(train_set)), "train +", len(test_set), "test"
