'''
  demo_echo.py - This is basic Finamon GNSS/4G Modem HAT Shield UDP echo example.
'''

import time
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from gps4ghat.BG77X import BG77X

module = BG77X()
module.debug_print("UDP echo demo")
time.sleep(2.)

contextID = "1"
module.getHardwareInfo()
module.getFirmwareInfo()
module.getIMEI()

if module.initNetwork(contextID): 
    module.setIPAddress(os.environ.get("ECHO_SERVER_IP"))    
    module.setPort(os.environ.get("ECHO_SERVER_PORT"))    
    module.activatePdpContext(contextID, 5)

    module.openConnection(contextID, "UDP", 5)
    module.sendUdpData("Hello " + module.board + " IMEI: " + module.IMEI)
    module.recvUdpData()

    module.closeConnection()
    module.deactivatePdpContext(contextID, 5)
    
module.close()


#[16:36:36] Finamon GNSS/Modem BG770A Shield created
#[16:36:42] ..RDY....APP RDY
#[16:36:42] UDP echo demo
#[16:36:42] AT...OK..
#[16:36:43] AT+CGMM...BG77....OK..
#[16:36:43] AT+CGMR...BG77LAR02A04....OK..
#[16:36:43] AT+GSN...866349041749536....OK..
#[16:36:43] AT+CMEE=2...OK..
#[16:36:43] AT+CPIN?...+CPIN: READY....OK..
#[16:36:44] AT+CFUN?...+CFUN: 1....OK..
#[16:36:44] AT+CREG=0...OK..
#[16:36:44] AT+CREG?...+CREG: 0,5....OK..
#[16:36:44] AT+CSQ...+CSQ: 99,99....OK..
#[16:36:44] AT+CEREG=0...OK..
#[16:36:45] AT+CEREG?...+CEREG: 0,5....OK..
#[16:36:45] AT+QNWINFO...+QNWINFO: "eMTC","26203","LTE BAND 20",6200....OK..
#[16:36:45] AT+QICSGP=1,1,"wsim","","",1...OK..
#[16:36:45] AT+QIACT=1...OK..
#[16:36:45] AT+QIACT?...+QIACT: 1,1,1,"10.11.32.148"....OK..
#[16:36:46] AT+QIOPEN=1,0,"UDP","52.215.34.155",7,0,0...OK....+QIOPEN: 0,0..
#[16:36:46] AT+QISEND=0,60...> 
#[16:36:46] Hello Finamon GNSS/Modem BG770A Shield IMEI: 866349041749536..SEND OK
#[16:36:46] ....+QIURC: "recv",0
#[16:36:46] AT+QIRD=0...+QIRD: 60..Hello Finamon GNSS/Modem BG770A Shield IMEI: 866349041749536....OK..
#[16:36:46] AT+QICLOSE=0...OK..
#[16:36:47] AT+QIDEACT=1...OK..

