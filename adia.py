from lcd20x4 import LCD
from Hions import Protons
from Eh import Electrons
import time
from datetime import datetime as dt
import bme280

f = open('/home/pi/Prj/pola.txt','a',1)
pH = Protons()
Eh = Electrons()
d = LCD(bus=1,address=0x3f)
while True:
   pH.write('R')
   Eh.write('R')
   time.sleep(2)
   rph = pH.read()
   rph = rph.split(' ')
   #rph = rph[-1]
   reh = Eh.read()
   reh = reh.split(' ')
   #reh = reh[-1]
   
   temp, pres, hum = bme280.readBME280All()
   dts = dt.utcnow().strftime('%m-%d %H:%M:%S')
   #dts = dt.now().isoformat()
   line = '{}, {}, {}, {}, {}'.format(dts, rph[-1], reh[-1], temp, pres)
   #print a, type(a)
   d.write_lines([dts,
'pH:'+rph[-1] + ';Eh:' + reh[-1],
'temp:{:.2f};{}kPa'.format(temp,int(pres))])
   f.write(line+'\n')
   time.sleep(30)
