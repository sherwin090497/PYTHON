# Lock Driver
# Roswell James Castaneda 820249749
# Sherwin Labadan 820229989

import bluepy.btle as btle
import RPi.GPIO as GPIO
import time

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
servoOne = GPIO.PWM(11, 50)
servoOne.start(0)


class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        print(data.decode("utf-8"))
        return data


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


# Function for recieving the code
def waitForCode(p, s, c):
    recCode = ""
    recSecCode = false

    # We check for any recieved data from arduino
    if (p.waitForNotifications(1)):
        # Send code to security software
        # If key is right, return true else false;

        if (recSecCode == True):
            unlockLock(True)
            c.write(bytes("Success", "utf-8"))
        else:
            unlockLock(False)
            c.write(bytes("Fail", "utf-8"))


# function to set angle of servo.
def setAngle(angle):
    duty = angle / 18 + 2
    servoOne.ChangeDutyCycle(duty)
    time.sleep(2)
    servoOne.ChangeDutyCycle(0)


# Function to use servo and unlock door
def unlockLock(operation):
    # Setup for Servo
    if (operation == True):
        print("Unlocking Door")
        # Need to calibrate, set angle to open lock
        setAngle(180)
        # Need to calibrate, set angle to close lock
        setAngle(90)
    elif (operation == False):
        print("Key Wrong: Not Unlocking Door")


def main():
    exit = False

    # Connect to HM-10 BT device
    p = btle.Peripheral("64:69:4E:21:CB:8D")
    s = p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
    c = s.getCharacteristics()[0]

    # script Loop
    while exit == false:
        waitForCode(p, s, c)

    p.disconnect()
    servoOne.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    main()