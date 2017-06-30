import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy.types as types
import analysis 
import numpy as np
import datetime
# import pymysql

### fill up the username and password ###
db_info = {
    'host': '140.142.198.89',
    'user': '',
    'password': '',
    'port': 53306,
    'dbname': 'orca2016'
}

sql_str = 'mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}'.format
engine = create_engine(sql_str(**db_info))

## enter you sql query in the multi-line command #####
## For this code runs, please at least select the variables below from od-transfer
## transfer_boarding_time, transfer_boarding_date, exit_time, transfer_duration 
query = '''SELECT transfer_boarding_time, transfer_boarding_date, exit_time, transfer_duration
FROM `od-transfer`
WHERE exit_time > 0''' # ignore the ones fail to process the exit time 
df = pd.read_sql(query, engine)

############### Combine time and date into one variable ########################
df.transfer_boarding_date = pd.to_datetime(df.transfer_boarding_date)
df['transfer_boarding_combine'] = df.transfer_boarding_date + df.transfer_boarding_time
df['exit_time_timedelta'] = pd.to_timedelta(df.exit_time)
df['exit_combine'] = df.transfer_boarding_date + df.exit_time_timedelta
# drop the excess column
df.drop(['exit_time_timedelta','transfer_boarding_date','transfer_boarding_time','exit_time'],inplace=True,axis=1,errors='ignore')


############### Calculate valid time duration ##################################
df['diff'] = df['transfer_boarding_combine']-df['exit_combine']

############## Solving the midnight issue ###################################### 
############## Select the ones with transfer duration with in 2 hours ##########
df['test_time'] = df['exit_combine']
df.ix[df['diff']< datetime.timedelta(seconds=0),'test_time'] -= datetime.timedelta(days=1)
df['test_diff'] = df['transfer_boarding_combine'] - df['test_time'] 
df.ix[df['test_diff']> datetime.timedelta(seconds=7500),'test_diff'] = np.nan # output null for rows having exit time after transfer boarding time

############# Select the ones that transfer duration is within -5 minutes ######
df.ix[ np.logical_and(df['test_diff'].isnull(), df['diff']>= datetime.timedelta(seconds= -300)),'test_diff'] = df['diff']

############ Drop the invalid rows and excess columns ###########################
df = df.drop(df[df['test_diff'].isnull()].index)
df = df.rename(columns={'test_diff':'calc_transfer_duration'})
df.drop(['diff','test_time'],inplace=True,axis=1,errors='ignore')

###########  Drop the wrong transfer_duration column IF NEEDED ################## 
# df.drop(['transfer_duration'],inplace=True,axis=1,errors='ignore')

############ Export to csv IF NEEDED #############################################
# df.to_csv('~/Desktop/view_data.csv')



###########  Debugging Code ###################################################
# temp_df = df.loc[df['calc_time_duration']!= df['transfer_duration']]
# temp_df.head()