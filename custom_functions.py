import pandas as pd
from haversine import haversine
import scipy.stats as ss
import numpy as np

def wrangler(df: pd.DataFrame) -> pd.DataFrame:
    """
    - Keeping the duplicated id values , they will be useful for later analysis 
    - Convert to datetime and int accordingly
    - Deduct NaN basement footage from rest area info
    - Substitute the NaN renovated as 0, since 0 is anyway the majority of data
    - Did not establish waterfront correlation and not relevant to client, so column is excluded
    - View is also excluded as 19k of 21k data is 0 and not relevant to our client
    - Adds lat_long tuple column and center_distance columns calculating each property distance from Seattle center. Unit is miles.
    - Reordering columns according to our project priorities
    """
    df = df.drop(columns=['id', 'id.1', 'waterfront', 'view'])
    df.rename(columns={'date':'sold_date'}, inplace=True)
    df['sold_date'] = pd.to_datetime(df['sold_date'])
    df.yr_renovated = df.yr_renovated/10
    df['price_per_sqft'] = df['price']/df['sqft_living']
    df['sqft_basement'].fillna(df['sqft_living'] - df['sqft_above'], inplace=True)
    df['yr_renovated'] = df.yr_renovated.fillna(0)
    columns_to_int = ['price_per_sqft','sqft_living', 'sqft_lot', 'sqft_basement','sqft_living15', 'sqft_lot15', 'price', 'yr_renovated', 'sqft_above', 'bedrooms']
    df[columns_to_int] =df[columns_to_int].astype(int)
    seattle_center = (47.6018266,-122.3778238)
    df['lat_long'] = tuple(zip(df['lat'], df['long']))
    df['center_distance'] = df['lat_long'].apply( lambda row: haversine(seattle_center, row, unit='mi'))
    df= df[['price','price_per_sqft','sqft_living','grade','condition','center_distance','bedrooms', 'bathrooms', 'floors', 'sqft_lot', 'sqft_above', 'sqft_basement', 'sqft_living15', 'sqft_lot15','yr_built', 'yr_renovated', 'sold_date', 'zipcode', 'house_id', 'lat','long']]
    return df


def cramers_corrected_stat(df,cat_col1,cat_col2):
    """
    This function spits out corrected Cramer's correlation statistic
    between two categorical columns of a dataframe 
    """
    crosstab = pd.crosstab(df[cat_col1],df[cat_col2])
    chi_sqr = ss.chi2_contingency(crosstab)[0]
    n = crosstab.sum().sum()
    r,k = crosstab.shape
    phi_sqr_corr = max(0, chi_sqr/n - ((k-1)*(r-1))/(n-1))    
    r_corr = r - ((r-1)**2)/(n-1)
    k_corr = k - ((k-1)**2)/(n-1)
    
    result = np.sqrt(phi_sqr_corr / min( (k_corr-1), (r_corr-1)))
    return round(result,3)


def anova_pvalue(df,cat_col,num_col):
    """
    This function spits out the anova p-value (probability of no correlation) 
    between a categorical column and a numerical column of a dataframe
    """
    CategoryGroupLists = df.groupby(cat_col)[num_col].apply(list)
    AnovaResults = ss.f_oneway(*CategoryGroupLists)
    p_value = round(AnovaResults[1],3)
    return p_value
