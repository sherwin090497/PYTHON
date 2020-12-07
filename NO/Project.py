# Lock Driver
# Roswell James Castaneda 820249749
# Sherwin Labadan 820229989

import bluepy.btle as btle
import RPi.GPIO as GPIO
import sys
import select
import time
import hashlib

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
servoOne = GPIO.PWM(11, 50)
servoOne.start(0)

# global variable for bluetooth data.
recData = ""


# Delegate to handle notifications from BT device
class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        global recData
        recData = data.decode("utf-8")


# Function to test two-way comms.
def testSend():
    # Connect to HM-10 BT device
    p = btle.Peripheral("64:69:4E:21:CB:8D")
    s = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
    c = s.getCharacteristics()[0]

    # Write to bluetooth device
    c.write(bytes("POGGERS BRO", "utf-8"))

    # Read from bluetooth device
    p.withDelegate(ReadDelegate())

    notif = False;

    while notif == False:
        print("waiting...")
        while p.waitForNotifications(1):
            print("recieved")
            notif = True
            break

    p.disconnect()


# Function to encrypt string
def Encryption(input):
    buttonInput = hashlib.sha512(input.encode())
    encryptedInput = buttonInput.hexdigest()
    key = Compare(encryptedInput)
    return key


# Function to compare keypad input to see if it is the correct key
def Compare(compareInput):
    # Actual key is 0981725
    key = 'ff078a828af9cacd6a7c28489222d18c0daf9cf673eea6ef91a060de9a889034b17aa6164fd7f388e99d2af7384f9e7bd044ecf7b39f65d151ecdcfdcfb86e0b'
    if key == compareInput:
        return 1
    else:
        return 0

    # Function for recieving the code


def WaitForCode(p, s, c):
    recCode = ""
    SecCode = False

    # We check for any recieved data from arduino
    if (p.waitForNotifications(1)):
        print("Recieved input: " + recData)
        recCode = Encryption(recData)
        print(recCode)
        SecCode = Compare(recCode)

        if (SecCode == True):
            c.write(bytes("Success", "utf-8"))
            unlockLock(True)
        else:
            c.write(bytes("Fail", "utf-8"))
            unlockLock(False)

    else:
        pass


# function to set angle of servo.
def setAngle(angle):
    duty = (angle / 18) + 2
    servoOne.ChangeDutyCycle(duty)
    time.sleep(2)
    servoOne.ChangeDutyCycle(0)


# Function to use servo and unlock door
def unlockLock(operation):
    # Setup for Servo
    if (operation == True):
        print("Unlocking Door")
        # Set angle to open lock
        setAngle(90)
        # wait 10 seconds (8 + 2 second delay of servo)
        time.sleep(8)
        # open lock
        setAngle(0)
    elif (operation == False):
        print("Key Wrong: Not Unlocking Door")


def main():
    exitP = False

    # Connect to HM-10 BT device
    p = btle.Peripheral("64:69:4E:21:CB:8D")
    s = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
    c = s.getCharacteristics()[0]
    p.withDelegate(ReadDelegate())

    # script Loop
    while exitP == False:
        input = select.select([sys.stdin], [], [], 1)[0]
        if input:
            input = sys.stdin.readline().rstrip()
            if input == "q":
                exitP = True
        WaitForCode(p, s, c)

    p.disconnect()
    servoOne.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    main()