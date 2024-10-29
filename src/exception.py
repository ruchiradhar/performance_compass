# file allows raising of exception with custom error message
# imports 
import sys #allows manipulation of runtime environment
from src.logger import logging

# custom error message function
def error_message_detail(error, error_detail:sys): 
    _,_,exc_tb= error_detail.exc_info() # the third exception from error_detail contains info we need for o
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_num=exc_tb.tb_lineno
    error_mes=str(error)
    error_message= "Error occured in python script name [{0}] line number [{1}] error message= [{2}]".format(
        file_name, line_num,error_mes
    )
    return error_message

# custom exception handling with custom error message
class CustomException(Exception): #inherit from Exception Class
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message