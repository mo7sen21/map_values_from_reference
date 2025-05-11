import numpy as np
import pandas as pd

df = 'test.csv'

# creating dict for hospital names , regions

hopistal_ref = {'Al Ain' : ['al-ain-hospital',
            'al-jowhara-hospital',
            'al-madar',
            'al-yahar',
            'bawadi',
            'zakher'],

            'Abu Dhabi' :['airport-road-hospital',
                  'al-noor-hospital',
                  'al-mamora',
                  'al-mussafah',
                  'baniyas',
                  'khalifa-cityl',
                  'madinat-zayed',
                  'reem-mall-clinic'],

            'Dubai' : ['city-hospital',
              'City-Hospital-Comprehensive-Cancer-Centre',
              'parkview-hospital',
              'welcare-hospital',
              'al-barsha-dialysis-centre',
              'al-qusaisl',
              'al-sufouh',
              'al-tawar-dialysis-centre',
              'arabian-ranches',
              'creek-harbour',
              'deira',
              'dubai-hills',
              'dubai-mall',
              'ibn-battuta',
              'me-aisem',
              'meadows',
              'mirdif',
              'springs']}


# the function to apply this dict and get corporate links also

def get_region(df ,column_link, column_region, column_hospital , ref ):
    df[column_region] = ''
    df[column_hospital] = ''
    df[column_link].fillna('',inplace= True)
    for k in ref.keys():
        print(k)
        for h in ref[k]:
            print(h)
            df.loc[df[column_link].str.contains(h), column_region] = k
            df.loc[df[column_link].str.contains(h), column_hospital] = h
    df.loc[(~df[column_region].isin(ref.keys())) & (df[column_link].str.contains('corporate')) , column_region] = 'corporate'
    df.loc[(~df[column_region].isin(ref.keys())) & (df[column_link].str.contains('corporate')) , column_hospital] = 'corporate'

    return df


# applying the function

df_fin = get_region(df ,'Page path and screen class', 'Real_Region' , 'Hospital',hopistal_ref)


# exporting edited file

df_fin.to_csv('test_edited.csv' , index = False)
