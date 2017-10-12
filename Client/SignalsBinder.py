from PyQt5.QtCore import QObject

class SignalsBinder(QObject):
    def __init__(self,client_bankomat,interrupt_convertor,session_data_configurator,view_operator = None,
                 bill_acceptor = None,qr_decoder = None):
        super(SignalsBinder, self).__init__()

        self.__interrupt_convertor = interrupt_convertor
        self.__client_bankomat = client_bankomat
        self.__session_data_configurator = session_data_configurator
        
        self.__qr_decoder = qr_decoder
        
###########################################################################
        
        self.__view_operator = view_operator

        self.__bill_acceptor = bill_acceptor
        
        
        
        self.snapping_client_bankomat_signals()
        self.snapping_signals_interrupt_convertor()
        self.snapping_session_data_configurator_signals()
        self.snapping_view_operator_signals()
        self.snapping_bill_acceptor_signals()
        self.snapping_qr_decoder_signals()
        
        
        

    def snapping_client_bankomat_signals(self):
        self.__client_bankomat.data_from_server_recieved.connect(self.__interrupt_convertor.detect_action)

    def snapping_signals_interrupt_convertor(self):
        self.__interrupt_convertor.inform_me.connect(self.__session_data_configurator.inform_me)
        self.__interrupt_convertor.actual_data.connect(self.__session_data_configurator.amount_kept)
        self.__interrupt_convertor.withdraw_complete.connect(self.__session_data_configurator.withdraw_complete)
        
        self.__interrupt_convertor.request_has_made.connect(self.__client_bankomat.write_data_to_server)
        
    
    def snapping_view_operator_signals(self):
        if self.__view_operator is not None:
            self.__view_operator.btn_BTC_pressed.connect(self.__interrupt_convertor.make_inform_me_btc_request)
            self.__view_operator.withdraw_btc_btn_pressed.connect(self.__interrupt_convertor.make_withdraw_btc_request)
            
    def snapping_bill_acceptor_signals(self):
        if self.__bill_acceptor is not None:
            self.__bill_acceptor.banknote_recieved.connect(self.__interrupt_convertor.make_keep_amount_btc_money_to_reserve_request)
        
    def snapping_session_data_configurator_signals(self):
        self.__session_data_configurator.monet_revieved_from_bill_acceptor.connect(
            self.__interrupt_convertor.make_keep_amount_btc_money_to_reserve_request)
        
        
    def snapping_qr_decoder_signals(self):
        self.__qr_decoder.qr_detected.connect(self.__session_data_configurator.reciecer_address_decoded)