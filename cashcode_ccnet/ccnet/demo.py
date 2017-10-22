from cashcode_ccnet.ccnet.ccnet import CCNET
import sys
import signal

def print_balance(balance, amount=False):
    sys.stdout.write("\b\r Balance: " + str(balance))
    if amount:
        sys.stdout.write(" | Hmmm, Its " + str(amount) + ". Om nom nom nom...")
    else:
        sys.stdout.write("                                               ")
    sys.stdout.flush()


def print_device(device):
    print(str(device['Part']),"SERIAL" + str(device['Serial']),str(device['Asset']).encode('hex'))
    sys.stdout.flush()


def print_bill_table(table):
    print("\n== BILL TABLE ==")
    for i, bill in enumerate(table):
        if i % 4 != 0:
            sys.stdout.write("\t\t")
            sys.stdout.write(str(int(bill['amount'])) + str(bill['code']))
        else:
            sys.stdout.write("\n")
            sys.stdout.write(str(int(bill['amount'])) + str(bill['code']))


# ccnet.end()
# ccnet.retrieve()


#       ###  ####  ##   #   ###
#       #  # #     # # ##  #   #
#       #  # ####  #  # #  #   #
#       #  # #     #    #  #   #
#       ###  ####  #    #   ###

ccnet = CCNET('COM4', '03')     # Init: connect to serial
if ccnet.connect() and ccnet.start():   # reset end enable bill types
  
    print_device(ccnet.device)
    print_bill_table(ccnet.billTable)

    balance = 0
    while True:
        esc = ccnet.escrow()            # Allows get cash. return {'amount', 'code'}
        if esc is not False:
            print_balance(balance, esc['amount'])
            if ccnet.stack():           # Get this bill
                balance += esc['amount']
            print_balance(balance)
else:
    print("Connection error. Check log files")
