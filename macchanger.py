import subprocess
import optparse
import re

#re=regular expression
def get_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest='interface',help="to change interface")
    parse_object.add_option("-m","--mac",dest='macid',help="to change macid ")
    return parse_object.parse_args()
def macchanger(user_interface,maccaddress):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",maccaddress])
    subprocess.call(["ifconfig",user_interface,"up"])

def macchangeresult(interface):
    ifconfig =subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group()
    else :
        return None

(user_data,attributes) = get_input()
macchanger(user_data.interface,user_data.macid)
final=str(macchangeresult(user_data.interface))

if final == user_data.macid:
    print("successful")
else:
    print("error")