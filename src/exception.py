
import sys 

def error_message_detail(error,error_detail:sys):
    _,_,excel_tb=error_detail.exc_info()
    error_name=excel_tb.tb_frame.f_code.co_filename
    error_message=f"error occured in python script name {error_name} line number {excel_tb.tb_lineno} error message {str(error)}"

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

