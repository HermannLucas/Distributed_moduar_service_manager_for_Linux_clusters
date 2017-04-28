import abc

class Abstract_interface:
    __metaclass__ = abc.ABCMeta
    
    @property
    @abc.abstractmethod
    def version(self):
        return self.__version
    
    @property
    @abc.abstractmethod
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @abc.abstractmethod
    def start(self):
        pass
    
    @abc.abstractmethod
    def stop(self):
        pass
    
    def restart(self):
        self.stop()
        self.start()
    
    
    @abc.abstractmethod
    def change_conf(self):
        pass
    
    @property
    @abc.abstractmethod
    def conf(self):
        return

class Abstract_Order:
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def execute(self):
        pass
