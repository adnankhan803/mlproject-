import sys
import logging 

#when ever error raises this fucntion is called and returns a message 
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() 
    #exc_inf - execution info
    #exc_tb - on which file and line exception occured and other info
    #error_detail give three part of info but we need last one _,_,exc_tb

    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    #defines how a message should look like with respect to custom exception

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    #prints error message 
    def __str__(self):
        return self.error_message



