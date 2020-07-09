import urllib.request
import os
import pandas as pd

sites = ['KKI', 'NeuroIMAGE', 'NYU', 'OHSU', 'Peking_1',
         'Peking_2', 'Peking_3', 'Pittsburgh', 'WashU']
# sites = ['WashU']
path = '/Users/falmuqhim/FIU/Lab/adhd200/ADHD200_training_pheno/'

statsFiles = ['aseg.stats', 'lh.aparc.a2009s.stats',
              'lh.aparc.DKTatlas40.stats', 'lh.aparc.stats', 'lh.BA.stats', 'lh.BA.thresh.stats', 'lh.curv.stats', 'lh.entorhinal_exvivo.stats', 'lh.w-g.pct.stats', 'rh.aparc.a2009s.stats', 'rh.aparc.DKTatlas40.stats', 'rh.aparc.stats', 'rh.BA.stats', 'rh.BA.thresh.stats', 'rh.curv.stats', 'rh.entorhinal_exvivo.stats', 'rh.w-g.pct.stats', 'wmparc.stats']

for site in sites:
    print('started: ' + site)
    os.mkdir('pre'+site)
    df_labels = pd.read_csv(path+site+'/'+site+'_phenotypic.csv')
    for row in df_labels.iterrows():
        file_id = str(row[1]['ScanDir ID']).split('.')[0].zfill(7)
        print('downloading: ' + file_id)
        url = 'https://s3.amazonaws.com/fcp-indi/data/Projects/ADHD200/surfaces/freesurfer/5.3/' + \
            file_id + '/stats/'
        os.mkdir('pre'+site+'/' + file_id)
        os.mkdir('pre'+site+'/' + file_id + '/' + 'stats')
        for file in statsFiles:
            try:
                urllib.request.urlretrieve(
                    url + file, './pre' + site + '/' + file_id + '/stats/' + file)
            except Exception as e:
                print('Error: ' + file_id)
                print('Error: ' + site)
                print('--------')
                break
