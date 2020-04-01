import pandas as pd
import numpy as np

def csv_file_read(gn, sn, pn):
    file_path = '../csv/'
    file_name = file_path + 'gondola_' + str(gn) + '_shelf_' + str(sn) + '_plate_' + str(pn) + '.csv'

    weight_data = pd.read_csv(file_name)
    timestamp = np.array(list(weight_data.iloc[:, 0]))
    weight_value = np.array(list(weight_data.iloc[:, 1]))


    down_ts = []
    down_wv = []

    for jj in np.arange(0, len(weight_value)-10, 10):
        #print(jj)
        tmp_ts = timestamp[jj: jj + 10]
        tmp_wv = weight_value[jj: jj + 10]
        #print(tmp_wv)

        mean_ts = np.mean(tmp_ts)
        mean_wv = np.mean(tmp_wv)
        #print(mean_wv)
        down_ts.append( mean_ts)
        down_wv.append( mean_wv)


    return np.array(down_ts), np.array(down_wv)
