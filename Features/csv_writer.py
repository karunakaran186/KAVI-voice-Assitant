#create and read from a csv file
# import csv 
import datetime
import pandas as pd
# 


# def get_length(file):
#     return 1
def append_data(file ,query, response):
    # fieldnames = ['date', 'time', 'query', 'response']
    #the number of rows?
    # next_id = get_length(file)
    # output = pd.read_csv(file)
    # sr_no = 0 
    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M:%S")
    pd.read_csv(file, delimiter= ',')
    df = pd.DataFrame()
    df = df.append([[date, time,query, response]]).set_index(0.00,drop=True)
    df.to_csv(file ,header= False, mode= "a")
    # df.add()
    # sr_no += 1 
    # output =pd.read_csv('data.csv')
    # print(output)
    # output.append(pd.DataFrame({'Date': date, 'time':time, 'query':query, 'response': response}, ignore_index = True))
    # print(output.head())
        # writer.writeheader()
        # writer.writerow()
# append_data('data.csv', "agaga","agagag5")
# append_data('data.csv', "agaga","agagag4")
# append_data('data.csv', "agaga","agagag3")
# append_data('data.csv', "agaga","agagag2")
# append_data('data.csv', "agaga","agagag1")
def prev_response(attribute):
    data = pd.read_csv('data.csv')
    (prev_attribute) = str(data.iloc[-1:][attribute])
    a =(list(prev_attribute.split(' '))[4]).split('\n')
    return a[0]
def prev_time(file):
    data = pd.read_csv(file)
    (prev_attribute) = str(data.iloc[-2:]['time'])
    a =(list(prev_attribute.split(' '))[4]).split('\n')
    return a[0]