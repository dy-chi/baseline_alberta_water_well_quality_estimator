# Add location data to water analysis and smell model prediction


# import well data from csv
import pandas as pd
import geopandas as gpd

# Read the 'well' CSV file
wells = pd.read_csv('csv_tables\WELL.csv')

# Read the 'well_test' CSV file

well_test = pd.read_csv('csv_tables\WELL_TEST.csv')

# create a subset of df with only well_id and well_test_id
well_test_sub = well_test[['WELL_ID','WELL_TEST_ID']]

# Subsetting the data

wells_sub = wells[['WELL_ID','LATTITUDE','LONGITUDE']]

# read well analysis which has been cleaned in previous steps
 
well_analysis_full = pd.read_csv('well_analysis_full.csv')

# merge location data to well_analysis_full

merged_df = pd.merge(well_test_sub, wells_sub, on='WELL_ID', how='left')
merged_df = pd.merge(merged_df, well_analysis_full, on='WELL_TEST_ID', how='inner')

well_analysis_full_lat_long=merged_df


# Read the smell_words CSV file
smell_words_output = pd.read_csv('smell_words_output.csv')
sw_sub=smell_words_output[['WELL_TEST_ID','MODEL_PREDICTION']]
# merge location data to smell_words
merged_df = pd.merge(well_test_sub, wells_sub, on='WELL_ID', how='left')
merged_df = pd.merge(merged_df, sw_sub, on='WELL_TEST_ID', how='inner')
smell_words_lat_long=merged_df
# create a GeoDataframe for well_analysis_full

geometry = gpd.points_from_xy(well_analysis_full_lat_long.LONGITUDE, well_analysis_full_lat_long.LATTITUDE)
well_analysis_full_geo = gpd.GeoDataFrame(well_analysis_full_lat_long, geometry=geometry, crs='EPSG:4326')

# create a GeoDataframe for smell_words

geometry = gpd.points_from_xy(smell_words_lat_long.LONGITUDE, smell_words_lat_long.LATTITUDE)
wells_smell_geo = gpd.GeoDataFrame(smell_words_lat_long, geometry=geometry, crs='EPSG:4326')


# RemoveIdentically located wells, (likely duplicates despite having different well_ids)

well_analysis_full_geo_disolved_first=well_analysis_full_geo.dissolve(by=well_analysis_full_geo['geometry'], aggfunc='first')
well_analysis_full_geo_disolved_first.rename(columns={'geometry':'geometry_2'},inplace=True)
well_analysis_full_geo_disolved_first.reset_index(inplace=True)
well_analysis_full_geo_disolved_first.drop('geometry_2', axis=1, inplace=True)


wells_smell_geo_first=wells_smell_geo.dissolve(by=wells_smell_geo['geometry'], aggfunc='first')
wells_smell_geo_first.rename(columns={'geometry':'geometry_2'},inplace=True)
wells_smell_geo_first.reset_index(inplace=True)
wells_smell_geo_first.drop('geometry_2', axis=1, inplace=True)

#drop all rows with missing values 
well_analysis_full_geo_disolved_first.dropna(inplace=True)




chemistry_variables = [
    'carbonate_value',
    'nitrite as nitrogen_value',
    'nitrate as nitrogen_value',
    'ph_value',
    'bicarbonate_value',
    'total dissolved solids_value',
    'fluoride_value',
    'chloride_value',
    'manganese_value',
    'iron_value',
    'sulphate_value',
    'calcium_value',
    'sodium_value',
    'potassium_value',
    'magnesium_value',
    'iron (total)_value',
    'nitrite + nitrate as nitrogen_value',
    'ionic balance_value'
]

#drop all rows with extreme positive outliers values above 6x std (this affects estimated values especailly for nitrates)

threshold = 6 

# Calculate the mean and standard deviation for each column in the list
mean_values = well_analysis_full_geo_disolved_first[chemistry_variables].mean()
std_deviations = well_analysis_full_geo_disolved_first[chemistry_variables].std()

# Calculate the upper bound for outliers for each column
upper_bounds = mean_values + threshold * std_deviations

# Create a filtered DataFrame without positive outliers for each column
filtered_df = well_analysis_full_geo_disolved_first.copy()

for column_name in chemistry_variables:
    filtered_df = filtered_df[filtered_df[column_name] <= upper_bounds[column_name]]


well_analysis_full_geo_disolved_first=filtered_df

well_analysis_full_no_geo_dups=well_analysis_full_geo_disolved_first

# saving as a csv file 
well_analysis_full_no_geo_dups.to_csv('well_analysis_full_no_geo_dups.csv', index=False)

