#
# Example file for formatting time and date output
# 

from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now(); #get the current date and time
    
    ### DATE FORMATTING ###
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print now.strftime("%Y"); #Full year with century, %y prints just the year without century
    print now.strftime("%a, %d %B, %y"); #abbreviated day, num, full month, abbreviated year
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print now.strftime("%c");
    print now.strftime("%x");
    print now.strftime("%X");
    
    ### TIME FORMATTING ####
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print now.strftime("%I:%M:%S %p"); #12-Hour:Minute:Second:AM/PM
    print now.strftime("%H:%M"); # 24-Hour:Minute
    
if __name__ == "__main__":
    main();
