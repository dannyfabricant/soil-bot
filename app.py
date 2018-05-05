import time
from datetime import datetime
import pytz

# global variables
base_url = 'http://18.236.117.12:3000' #server
# base_url = 'http://192.168.1.6:3000' #local
interval = 0.5 #in minutes


# import local functions
import temp
import adc
import server
from config import beds
	
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
        # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamp = int( time.time() )

        #create objects for request
        data = {
            'timestamp': timestamp,
            'temp': temperature,
            'moisture': moisture
        }
        url = base_url + '/d/' + bed['url']['location'] + '/' + bed['url']['plot'] + '/' + 'add-data'

        # send request
        print(data)
        server.send_data(url, data)

        # increment loop
        i = i+1

    time.sleep(interval*60)
