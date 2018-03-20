import time
from datetime import datetime
import pytz

# global variables
base_url = 'http://192.168.1.7:3000/'
interval = 3 #in minutes


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
            'CHANNEL': 0,
            'CLK': 18,
            'MISO': 23,
            'MOSI': 24,
            'CS': 25
        },
        'temp_id': '28-0417a2f3c1ff' 
    },
    2 : {
        'name': '2',
        'url': {
            'plot': '5a83097df6a328228cafe861',
            'location': '5a830958f6a328228cafe85f'
        },
        'moisture': {
            'CHANNEL': 0,
            'CLK': 18,
            'MISO': 23,
            'MOSI': 24,
            'CS': 25
        },
        'temp_id': '28-0417a2f3c1ff' 
    },
    3 : {
        'name': '3',
        'url': {
            'plot': '5a85b11b92fcff3e9ac3f198',
            'location': '5a830958f6a328228cafe85f'
        },
        'moisture': {
            'CHANNEL': 1,
            'CLK': 18,
            'MISO': 23,
            'MOSI': 24,
            'CS': 25
        },
        'temp_id': '28-0417a2ecd4ff' 
    },
    4 : {
        'name': '4',
        'url': {
            'plot': '5a94e21c95bf020cf443bf99',
            'location': '5a830958f6a328228cafe85f'
        },
        'moisture': {
            'CHANNEL': 1,
            'CLK': 18,
            'MISO': 23,
            'MOSI': 24,
            'CS': 25
        },
        'temp_id': '28-0417a2ecd4ff' 
    }
}
	
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

        # create timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #create objects for request
        data = {
            'timestamp': timestamp,
            'temp': temperature,
            'moisture': moisture
        }
        url = base_url + bed['url']['location'] + '/' + bed['url']['plot'] + '/' + 'add-data'

        # send request
        print(data)
        server.send_data(url, data)

        # increment loop
        i = i+1

    time.sleep(interval*60)
