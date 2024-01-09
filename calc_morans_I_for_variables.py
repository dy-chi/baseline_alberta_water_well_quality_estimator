import pysal
import esda

def calc_w_distance_at_lag(dataframe,lag_distances):
    '''lag_distances are in radians (roughly *111 to get distance in km at this lat), Reutrns a list of tuples with lag distance and morans I'''
    # Create a list to store Moran's I values
    w_distance_values = {}

    # Iterate through lag distances and calculate Moran's I
    for lag_distance in lag_distances:
        # Create a binary spatial weights matrix based on distance
        w_distance = pysal.lib.weights.DistanceBand.from_dataframe(dataframe, threshold=lag_distance, binary=True, silence_warnings=True)
        w_distance_values[lag_distance]=w_distance

    return w_distance_values

def calculate_variable_morans_i(dataframe, variable, lag_distances,lag_and_w_distance):
    '''lag_distances are in radians (roughly *111 to get distance in km at this lat), Reutrns a list of tuples with lag distance and morans I'''
    # Create a list to store Moran's I values
    moran_i_values = {}

    # Iterate through lag distances and calculate Moran's I
    for lag_distance in lag_distances:
        # Create a binary spatial weights matrix based on distance
        
        w_distance = lag_and_w_distance[lag_distance]
        moran_distance = esda.Moran(dataframe[variable], w_distance)
        
        
        moran_i_values[lag_distance]= moran_distance.I
                             

    return moran_i_values




def calculate_morans_i_for_variables(dataframe, chemistry_variables,lag_distances,lag_and_w_distance):
    variable_morans_I = {}  # Create a dictionary to store results for each variable
    
    for variable in chemistry_variables:
        moran_distance_values = calculate_variable_morans_i(dataframe, variable, lag_distances,lag_and_w_distance)
        #with dict of variables and moran Is, now calc 
        variable_morans_I[variable] = {'moran_distance_values': moran_distance_values}
    
    return variable_morans_I

variable_morans_I=calculate_morans_i_for_variables(well_analysis_full_geo_disolved_first,chemistry_variables,lag_distances,lag_and_w_distance)