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
        resp {[dict]} -- response message and status code
    """
    # Try and Except Block
    try:
        f = verifier.get(email, {'validateSMTP': 0, '_hardRefresh': 1})  # Verify email using api from whoisxmlapi.com

        # Convert JSON to PYTHON object
        convert = json.dumps(json.loads(f.json_string), indent=4)
        data = json.loads(convert)

        # Make checks to verify if email is good to be accepted or not.
        disposable_check = data['disposableCheck']
        catch_all_check = data['catchAllCheck']
        free_check = data['freeCheck']

        dispose = str(disposable_check).capitalize()
        catch = str(catch_all_check).capitalize()
        free = str(free_check).capitalize()

        dispose_check = strtobool(dispose)
        catch_check = strtobool(catch)
        freeCheck = strtobool(free)

        # Conditions to check the validity of an email
        if bool(dispose_check) is True or bool(catch_check) is True:
            msg = "We do not recognize this email address. Please provide a valid email address."
            resp = {'message': msg, 'status_code': 400}
            return resp
        elif bool(freeCheck) is False:
            msg = "Please use an email address from a free email provider like Google, Microsoft,etc."
            resp = {'message': msg, 'status_code': 400}
            return resp

        msg = "Email is verified and message has been sent."
        resp = {'message': msg, 'status_code': 200}
        return resp
    
    # Exception handlers that prevent the app from breaking down     
    except exceptions.HttpException:
        msg = "Sorry, we cannot access email service now. Please try again later."
        resp = {'message': msg, 'status_code': 500}
        return resp
    except exceptions.GeneralException:
        msg = "Sorry, we cannot access email service now. Please try again later."
        resp = {'message': msg, 'status_code': 500}
        return resp
