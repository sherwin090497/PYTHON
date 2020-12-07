# Lock Driver
# Roswell James Castaneda 820249749
# Sherwin Labadan 820229989

import bluepy.btle as btle

class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        print(data.decode("utf-8"))
        return data
    
#Function to test two-way comms.
def testSend():
    #Connect to HM-10 BT device
    p = btle.Peripheral("64:69:4E:21:CB:8D")
    s = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
    c = s.getCharacteristics()[0]
    
    #Write to bluetooth device
    c.write(bytes("POGGERS BRO","utf-8"))
    
    #Read from bluetooth device
    p.withDelegate(ReadDelegate())
    
    notif = False;
    
    while notif == False:
        print("waiting...") 
        while p.waitForNotifications(1):
            print("recieved")
            notif = True
            break
       
        
    p.disconnect()
    
def main():
    testSend()
    

if __name__ == "__main__":
    main()
