import pandas as pd


# read dataset from csv file
def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df


# calculate the mean of variable:
def get_mean(df, var):
    mean_var = df[var].mean()
    return mean_var


# calculate the median of variable:
def get_median(df, var):
    median_var = df[var].median()
    return median_var


# calculate the standard deviation of variable:
def get_std(df, var):
    std_var = df[var].std()
    return std_var


# calculate the min of variable:
def get_min(df, var):
    min_var = df[var].min()
    return min_var


# calculate the max of variable:
def get_max(df, var):
    max_var = df[var].max()
    return max_var


# calculate the quantile of variable:
def get_quantile(df, var, quantile):
    quantile_value = df[var].quantile(quantile)
    return quantile_value
