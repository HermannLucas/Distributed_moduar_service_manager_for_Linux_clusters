import argparse
from Core import Starter

parser = argparse.ArgumentParser(description = "Start the package manager on this machine.")

parser.add_argument("-H", "--head", default = False, help = "Starts as Head", action = "store_true")
parser.add_argument("-c", "--config", nargs = 1, help = "Start using a precise configuration file", metavar = "Config file")
parser.add_argument("-n", "--name", nargs = 1, type = str, help = "Specify the name of this machine", metavar = "Client name")
parser.add_argument("-ns", "--nameService", nargs = 1,  help = "To use a different NameService than the one in the configuration file.", metavar = "Nameservice")
parser.add_argument("-s",  "--shell", default = False, help = "Open up a shell to interact with the application.", action = "store_true")
parser.add_argument("-connect", default = False, action = "store_true")
args = parser.parse_args()

init_args = {}
init_args["Head"] = args.head

if args.config:
    init_args["config"] = args.config

if args.name:
    init_args["name"] = str(args.name)[2:len(args.name)- 3]

if args.nameService:
    init_args["nameservice"] = args.nameService

init_args["Shell"] = args.shell

init_args["connect"] = args.connect
    
start = Starter(init_args)

#print("type {}, config {}, name {}, nameservice {}.".format(start.type, start.config_path, start.name, start.nameservice))
