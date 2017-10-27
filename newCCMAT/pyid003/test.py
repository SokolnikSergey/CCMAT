#!/usr/bin/env python3
from  pyid003.id003 import BillVal,POW_UP,POW_UP_BIA,POW_UP_BIS
import pyid003.id003
import serial
import time
import logging


def main():
    port = 'COM11'  # JCM UAC device (USB serial adapter)
    
    bv = BillVal(port)
    bv.send_command(0x40)
    print("Please connect bill validator.")
    bv.power_on()
    
    if bv.init_status == POW_UP:
        logging.info("BV powered up normally.")
    elif bv.init_status == POW_UP_BIA:
        logging.info("BV powered up with bill in acceptor.")
    elif bv.init_status == POW_UP_BIS:
        logging.info("BV powered up with bill in stacker.")
        
    bv.poll()


if __name__ == '__main__':
    main()
