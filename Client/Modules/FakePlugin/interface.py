from Client.Module_interface import Abstract_interface

class Concrete_interface(Abstract_interface):
    
    def __init__(self):
        self.name = "Fake plugin"
    
    @property
    def version(self):
        return "A precise version"

    def start(self):
        print("Plugin {} is now started.".format(self.name))
    
    def stop(self):
        print("Plugin {} is now stopped.".format(self.name))

def begin(mod_man):
	return Concrete_interface()
