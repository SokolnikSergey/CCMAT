class SignalsBinder:
    def __init__(self,main_server = None, interrupt_convertor = None,balance_information_configurator = None
                 ,action_queue = None,action_performer = None,db_transactor = None ):
        self.__main_server = main_server
        self.__interrupt_convertor = interrupt_convertor
        self.__balance_information_configurator = balance_information_configurator
        self.__action_queue = action_queue
        self.__action_performer = action_performer
        self.___db_transactor = db_transactor


        self.snapping_action_queue_signals()
        self.snapping_main_server_signals()
        self.snapping_action_performer_signals()
        self.snapping_interrupt_convertor_signals()

    def snapping_main_server_signals(self):
        self.__main_server.data_recieved.connect(self.__interrupt_convertor.make_action)


    def snapping_action_queue_signals(self):
        self.__action_queue.action_added.connect(self.__action_performer.start_executing)
        
    def snapping_action_performer_signals(self):
        self.__action_performer.action_done.connect(self.__interrupt_convertor.make_response)
        ### connect signals about perform of transactions with database transactor
    
    def snapping_interrupt_convertor_signals(self):
        self.__interrupt_convertor.response_has_made.connect(self.__main_server.write_data_to_socket)
    

