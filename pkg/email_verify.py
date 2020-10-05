# Third-party modules 
from emailverifier import Client
from emailverifier import exceptions
import simplejson as json
# Built-in modules 
from distutils.util import strtobool    # module for converting strings to boolean 
import os


# Config email verifier
verifier = Client(str(os.environ.get('EMAIL_VERIFIER')))


def emailVerifier(email):
    """Retrieves information from the API about the given email address
    
    Arguments:
        email {[str]} -- email address
    
    Returns:
        {[dict]} -- response message and status code
    """
    # Try and Except Block
    try:
        f = verifier.get(email, {'validateSMTP': 0, '_hardRefresh': 1})  # Verify email using api from whoisxmlapi.com

        # Convert JSON to PYTHON object
        convert = json.dumps(json.loads(f.json_string), indent=4)
        data = json.loads(convert)

        # Make checks to verify if email is good to be accepted or not.
        disposable_check, catch_all_check, free_check = (str(data['disposableCheck']).capitalize(), 
                                                            str(data['catchAllCheck']).capitalize(),
                                                             str(data['freeCheck']).capitalize())

        dispose_check, catch_check, freeCheck = (strtobool(disposable_check), 
                                                    strtobool(catch_all_check), 
                                                    strtobool(free_check))
                                                    
        # Conditions to check the validity of an email
        # Sends code 400, if dispose and catch = True or free = False. Sends code 200, if otherwise
        msg, scode = ("Please use an email address from a free email provider like Google, Microsoft,etc.", 400) if bool(dispose_check) or bool(catch_check) is True or bool(freeCheck) is False else ("Email address verified. Message sent. ", 200)
        return {'message': msg, 'status_code': scode}
    
    # Exception handlers that prevent the app from breaking down     
    except exceptions.HttpException:
        return {'message': "Sorry, Please try again.", 'status_code': 500}
    except exceptions.GeneralException:
        return {'message': "Sorry, Please try again.", 'status_code': 500}
