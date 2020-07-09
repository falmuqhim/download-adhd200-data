import urllib.request
import os
import pandas as pd

# sites = ['KKI', 'NeuroIMAGE', 'NYU', 'OHSU', 'Peking_1',
#          'Peking_2', 'Peking_3', 'Pittsburgh', 'WashU']
sites = ['Brown']

# needs to be updated
path = '/Users/falmuqhim/FIU/Lab/adhd200/ADHD200_testing_pheno/'

for site in sites:
    print('started: ' + site)
    file_id = 26024
    while file_id <= 26022:
        file_name = str(file_id).split('.')[0].zfill(7)
        print('downloading: ' + file_name)
        url = 'https://s3.amazonaws.com/fcp-indi/data/Projects/ADHD200/RawData/' + site
        try:
            urllib.request.urlretrieve(
                url + '/' + file_name + '/session_1/anat_1/mprage.nii.gz', './anat_2_' + site + '/' + file_name + '_mprage.nii.gz')
        except Exception as e:
            print('Error: ' + file_name)
            print('Error: ' + site)
            print('--------')
        file_id += 1
