import time
import datetime

# global variables
base_url = 'http://192.168.1.7:3000/'
interval = 60 #seconds


# import local functions
import temp
import adc
import server

beds = {
    1 : {
        'name': '1',
        'url': {
            'plot': '5a83097bf6a328228cafe860',
            'location': '5a830958f6a328228cafe85f'
        },
        'moisture': {
            'CHANNEL': 1,
            'CLK': 18,
            'MISO': 23,
            'MOSI': 24,
            'CS': 25
        },
        'temp_id': '28-00000a016e68' 
    },
    2 : {
        'name': '2',
        'url': {
            'plot': '5a83097df6a328228cafe861',
            'location': '5a830958f6a328228cafe85fsfdb'
        },
        'moisture': {
            'CHANNEL': 1,
            'CLK': 18,
            'MISO': 23,
            'MOSI': 24,
            'CS': 25
        },
        'temp_id': '28-00000a016e68' 
    }
}

# print(beds['1']['moisture']['pins'])

	
while True:
    length = len(beds)
    # print(length)
    i = 1
    while i <= length:
        bed = beds[i]

        # get moisture reading
        CHANNEL = bed['moisture']['CHANNEL']
        CLK  = bed['moisture']['CLK']
        MISO = bed['moisture']['MISO']
        MOSI = bed['moisture']['MOSI']
        CS   = bed['moisture']['CS']
        moisture = adc.read_moisture(CHANNEL, CLK, MISO, MOSI, CS)

        # get temp readings
        temp_id = bed['temp_id']
        temperature = temp.read_temp(temp_id)

        #send data to server
        data = {
            'time': time.time(),
            'temp': temperature,
            'moisture': moisture
        }
        url = base_url + bed['url']['location'] + '/' + bed['url']['plot'] + '/' + 'add-data'
        server.send_data(url, data)
        print(url)
        print(data)


    time.sleep(interval)
