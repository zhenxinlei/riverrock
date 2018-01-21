class APriceRecorder :
	def __init__(self, value):
        	self.value = value
        	super().__init__()
    
    	@abstractmethod
    	def do_something(self):
        	pass
