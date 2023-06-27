import sys # provides various functions and variables that are used to manipulate different parts of the Python runtime environment.


# When there is a error this function gets called

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #  It assigns the exception type, exception value, and traceback object to the variables _, _, and exc_tb respectively
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)) # The error message includes the filename, line number, and the original error message.

    return error_message

    
# define a custom exception class named CustomException. It inherits from the built-in Exception class.

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): # defines the initializer method
        super().__init__(error_message) # calls the initializer of the base class (Exception) using super(), passing the error_message as an argument
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    # define the string representation method for the CustomException class
    def __str__(self):
        return self.error_message # return the value of the self.error_message attribute when the exception object is converted to a string.
    

    
    
