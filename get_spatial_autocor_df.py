import pandas as pd
# list of chemistry variables 
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

#list of features with max allowable values
chemistry_variables_mac_list = ['nitrite as nitrogen_value', 'fluoride_value', 'nitrate as nitrogen_value', 'nitrite + nitrate as nitrogen_value']
mac_values = [1, 1.5, 10, 10]
chemistry_variables_ao_list = [
    'manganese_value',
    'iron_value',
    'iron (total)_value',
    'sodium_value',
    'chloride_value',
    'sulphate_value',
    'total dissolved solids_value',
    'ph_value'
]
# list of features with aethsetic objective values
ao_values_dict = {
    'manganese_value': 0.05,
    'iron_value': 0.3,
    'iron (total)_value': 0.3,
    'sodium_value': 200,
    'chloride_value': 250,
    'sulphate_value': 500,
    'total dissolved solids_value': 500,
    'ph_value': 8.5
}

mac_values_dict = dict(zip(chemistry_variables_mac_list, mac_values))






variable_morans_I={'carbonate_value': {'moran_distance_values': {0.005: 0.13911639335220918,
0.01: 0.12394588109756921,
0.02: 0.09876547009291448,
0.03: 0.08307408879556794,
0.04: 0.07206140364032995,
0.05: 0.06371728904809215,
0.06: 0.058166838000802246,
0.07: 0.0536990693635664,
0.08: 0.04935600631527842,
0.09: 0.04636188794538173,
0.1: 0.04264463492264432,
0.2: 0.025275129773076745}},
'nitrite as nitrogen_value': {'moran_distance_values': {0.005: 0.00904055009104592,
0.01: 0.008014967122178987,
0.02: 0.0047187140254194015,
0.03: 0.003217547077100207,
0.04: 0.002551811518044821,
0.05: 0.0025506971833943208,
0.06: 0.0024036917053942273,
0.07: 0.0020738419658836204,
0.08: 0.0023300755894049797,
0.09: 0.002006163056093247,
0.1: 0.0017228280163410288,
0.2: 0.0012092604765209026}},
'nitrate as nitrogen_value': {'moran_distance_values': {0.005: 0.38592000559101736,
0.01: 0.35168559303284525,
0.02: 0.14289133629575798,
0.03: 0.14439636694258273,
0.04: 0.1286526054553932,
0.05: 0.08258060829948306,
0.06: 0.06721340144960435,
0.07: 0.05737187372163642,
0.08: 0.04872658896617216,
0.09: 0.039375651124558375,
0.1: 0.034755234360198575,
0.2: 0.01800739697518908}},
'ph_value': {'moran_distance_values': {0.005: 0.5051286300087824,
0.01: 0.4379624001429124,
0.02: 0.34260775171578656,
0.03: 0.28825817906413986,
0.04: 0.2578662470178735,
0.05: 0.23575000258485346,
0.06: 0.21596603967802014,
0.07: 0.20247431638509394,
0.08: 0.1910742394843252,
0.09: 0.18087711601030673,
0.1: 0.17112421701571942,
0.2: 0.12487883630971645}},
'bicarbonate_value': {'moran_distance_values': {0.005: 0.6376110502321521,
0.01: 0.5872880588661518,
0.02: 0.5472286018001612,
0.03: 0.5142033783727361,
0.04: 0.4865286233384619,
0.05: 0.4687110399308149,
0.06: 0.4532310035329231,
0.07: 0.43728561864427085,
0.08: 0.42268102970394494,
0.09: 0.41183321472582196,
0.1: 0.4016017631869747,
0.2: 0.34779182694610766}},
'total dissolved solids_value': {'moran_distance_values': {0.005: 0.5944528783811186,
0.01: 0.5171603438517224,
0.02: 0.42588344684152746,
0.03: 0.3698222423777493,
0.04: 0.3442846560855718,
0.05: 0.3201310179599076,
0.06: 0.3016628447743936,
0.07: 0.2827560730363955,
0.08: 0.2710454895923069,
0.09: 0.26046435287631164,
0.1: 0.25100423823285495,
0.2: 0.196736802680536}},
'fluoride_value': {'moran_distance_values': {0.005: 0.6477235841934968,
0.01: 0.5217466548591834,
0.02: 0.4167433922362721,
0.03: 0.35951331250943186,
0.04: 0.3358974531392159,
0.05: 0.3143432647582013,
0.06: 0.2981931404551946,
0.07: 0.28500090544554507,
0.08: 0.2747348015211226,
0.09: 0.2650241205056938,
0.1: 0.25495810770136834,
0.2: 0.1979186935134562}},
'chloride_value': {'moran_distance_values': {0.005: 0.5539790776364865,
0.01: 0.46261099186721777,
0.02: 0.3668874793332898,
0.03: 0.37247994079743635,
0.04: 0.36587360074404296,
0.05: 0.3346817970189839,
0.06: 0.32106498773713416,
0.07: 0.3109305733249134,
0.08: 0.3063406054616792,
0.09: 0.301941374817568,
0.1: 0.2947060814193326,
0.2: 0.2577475705635995}},
'manganese_value': {'moran_distance_values': {0.005: 0.005646246433404644,
0.01: 0.0037740597410790325,
0.02: 0.004664869626844939,
0.03: 0.0027600216305655664,
0.04: 0.002343209001925929,
0.05: 0.0019383702132647485,
0.06: 0.0019013248219033516,
0.07: 0.0018911493881568796,
0.08: 0.001662490348336691,
0.09: 0.0015781568307355648,
0.1: 0.0014831156291311087,
0.2: 0.0006512063185721675}},
'iron_value': {'moran_distance_values': {0.005: 0.01700493623114797,
0.01: 0.012764546198017935,
0.02: 0.006608525306043397,
0.03: 0.006058814485185411,
0.04: 0.00536270862221369,
0.05: 0.010752918383137182,
0.06: 0.008531673396651096,
0.07: 0.0069936151130853995,
0.08: 0.006236053370524319,
0.09: 0.005424086681082941,
0.1: 0.004688779173744786,
0.2: 0.002699479376056184}},
'sulphate_value': {'moran_distance_values': {0.005: 0.5983722466560685,
0.01: 0.5026407018551702,
0.02: 0.3997537408482819,
0.03: 0.3444593627975963,
0.04: 0.3192341386382983,
0.05: 0.2974721465685662,
0.06: 0.2790192987870711,
0.07: 0.26200416406863913,
0.08: 0.25083936615714775,
0.09: 0.23984177185916347,
0.1: 0.2309415340825988,
0.2: 0.1757261989124483}},
'calcium_value': {'moran_distance_values': {0.005: 0.4826207506943547,
0.01: 0.41000604112282474,
0.02: 0.3029889429029043,
0.03: 0.25732946320783356,
0.04: 0.23572468824203574,
0.05: 0.22003157997401193,
0.06: 0.20732945080340318,
0.07: 0.2008837065941237,
0.08: 0.19347039821454542,
0.09: 0.18565190781490057,
0.1: 0.1768686919351961,
0.2: 0.126050020213496}},
'sodium_value': {'moran_distance_values': {0.005: 0.6495858747126072,
0.01: 0.5860706694340999,
0.02: 0.4901174654343961,
0.03: 0.4214327597321065,
0.04: 0.3814701718742489,
0.05: 0.3607857486201374,
0.06: 0.34096946996122796,
0.07: 0.32086206189511374,
0.08: 0.30595486975301056,
0.09: 0.29377980094083284,
0.1: 0.28288398088890965,
0.2: 0.21755737246544668}},
'potassium_value': {'moran_distance_values': {0.005: 0.09112021992532648,
0.01: 0.068012152133372,
0.02: 0.058175563084645575,
0.03: 0.053223516193192606,
0.04: 0.05119595297027749,
0.05: 0.053572082803367296,
0.06: 0.05360887786672541,
0.07: 0.05390279436565107,
0.08: 0.05283995060703167,
0.09: 0.05144412841323857,
0.1: 0.05013225930065751,
0.2: 0.04366421730986693}},
'magnesium_value': {'moran_distance_values': {0.005: 0.5231530656506523,
0.01: 0.45323230860644825,
0.02: 0.3406066016736636,
0.03: 0.28201496655290303,
0.04: 0.25118226504457136,
0.05: 0.2372993713405863,
0.06: 0.21996336671314717,
0.07: 0.21084436960929076,
0.08: 0.2013000694259028,
0.09: 0.19134217424855526,
0.1: 0.18219863162857913,
0.2: 0.12006060839352432}},
'iron (total)_value': {'moran_distance_values': {0.005: 0.02444204356171548,
0.01: 0.00913477638893515,
0.02: 0.00408735695080831,
0.03: 0.003507913317505183,
0.04: 0.0030081156141874604,
0.05: 0.0017307043759259328,
0.06: 0.001349699509894244,
0.07: 0.0010875813874154719,
0.08: 0.0010825534155956113,
0.09: 0.0008560203132789731,
0.1: 0.0012093297123525553,
0.2: 0.0009466489137247868}},
'nitrite + nitrate as nitrogen_value': {'moran_distance_values': {0.005: 0.3845914441553198,
0.01: 0.35079643872193733,
0.02: 0.1429966004181208,
0.03: 0.14554149433365351,
0.04: 0.1296333602163871,
0.05: 0.08282033708242954,
0.06: 0.06723341479845554,
0.07: 0.057142858891422094,
0.08: 0.048529550292355776,
0.09: 0.039142870887974975,
0.1: 0.0345511951679048,
0.2: 0.017668916669552105}},
'ionic balance_value': {'moran_distance_values': {0.005: 0.20158245526564855,
0.01: 0.2075950681681488,
0.02: 0.17700291031994483,
0.03: 0.1488908342483409,
0.04: 0.1317573871908926,
0.05: 0.12047373846165949,
0.06: 0.11242568900765952,
0.07: 0.10493195510118573,
0.08: 0.0977273726254071,
0.09: 0.09220932810216982,
0.1: 0.0865316973061551,
0.2: 0.04966602969461521}}}

spatial_autocor_df = pd.DataFrame({'chemistry_variables': chemistry_variables})


def find_highest_lag_distances_above_threshold(morans_i_dict, threshold):
    highest_lag_distances = {}
    
    for variable, moran_values in morans_i_dict.items():
        lag_distances_and_values = moran_values['moran_distance_values']
        highest_lag_distance = None
        highest_moran_i = -1  # Initialize to a value lower than the threshold
        
        for lag_distance, moran_i in lag_distances_and_values.items():
            if moran_i > threshold and (highest_lag_distance is None or lag_distance > highest_lag_distance):
                highest_lag_distance = lag_distance
                highest_moran_i = moran_i
        
        if highest_lag_distance is not None:
            highest_lag_distances[variable] = (highest_lag_distance, highest_moran_i)
    
    return highest_lag_distances

def find_lowest_lag_distances_above_threshold(morans_i_dict, threshold):
    lowest_lag_distances = {}
    
    for variable, moran_values in morans_i_dict.items():
        lag_distances_and_values = moran_values['moran_distance_values']
        lowest_lag_distance = None
        lowest_moran_i = float('inf')  # Initialize to a high value
        
        for lag_distance, moran_i in lag_distances_and_values.items():
            if moran_i > threshold and (lowest_lag_distance is None or lag_distance < lowest_lag_distance):
                lowest_lag_distance = lag_distance
                lowest_moran_i = moran_i
        
        if lowest_lag_distance is not None:
            lowest_lag_distances[variable] = (lowest_lag_distance, lowest_moran_i)
    
    return lowest_lag_distances


# Define your threshold
threshold = 0.5

# Call the function to find the highest lag distances above the threshold
highest_lag_distances = find_highest_lag_distances_above_threshold(variable_morans_I, threshold)

# Print the results
for variable, (lag_distance, moran_i) in highest_lag_distances.items():
    print(f"For '{variable}', the highest lag distance above Moran I {threshold} is {lag_distance:.3f} with Moran's I of {moran_i:.3f}")
    variable_index=spatial_autocor_df[spatial_autocor_df['chemistry_variables'] == variable].index[0]
    spatial_autocor_df.at[variable_index, 'strong_0.5_spatial_auto_cor_dist'] = lag_distance

threshold = 0.3

# Call the function to find the highest lag distances above the threshold
highest_lag_distances = find_highest_lag_distances_above_threshold(variable_morans_I, threshold)

# Print the results
for variable, (lag_distance, moran_i) in highest_lag_distances.items():
    print(f"For '{variable}', the highest lag distance above Moran I {threshold} is {lag_distance:.3f} with Moran's I of {moran_i:.3f}")
    variable_index=spatial_autocor_df[spatial_autocor_df['chemistry_variables'] == variable].index[0]
    spatial_autocor_df.at[variable_index, 'weak_0.3_spatial_auto_cor_dist'] = lag_distance