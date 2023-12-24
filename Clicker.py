import time
# Data\autoClick.pyw is path for the actual clicker
import subprocess
def assurance():
    CPS = input("How many clicks per second would you like(increments of 10 aka must be divisible by 10)")
    
    if (int(CPS) % 10 != 0):
        print("this is not divisible by ten, please try again, make sure the number of clicks per second you want is divisible by ten")
        # needs to be ten as we are opening more python files based on how many clicks we want, loop clicks 10 times per second all the time
        CPS = assurance()
        
    if int(CPS) >= 1000:
        #making sure they want such a rapid speed
        areYouSure = input("Are you sure you want to click " +CPS+" each second? It will likely lag")
        areYouSure = areYouSure.lower()
        if areYouSure == "y" or areYouSure == "yes": # they confirmed they want this speed
            return(int(CPS))
        elif areYouSure == "n" or areYouSure == "no": # they rejected the speed they chose
            CPS = assurance()
            # looping by jamming them through the function again
    return(int(CPS))    
print("Welcome to Quintin's Auto Clicker!")
CPS = assurance()
print("Press Home when you want to exit the autoclicker, if it doesnt close on the first attempt press it again")
time.sleep(3)

if CPS >= 100: # choses the more powerful file based on input
    Instances = CPS // 100
    for i in range(Instances):
        subprocess.Popen(['pythonw', 'Data/autoClickBigger.pyw']) #sadly not as accurate as i suggested it is
else:
    Instances = CPS // 10
    for i in range(Instances):
        subprocess.Popen(['pythonw', 'Data/autoClick.pyw'])

print("Done")
time.sleep(1)
