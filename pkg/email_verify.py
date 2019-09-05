from emailverifier import Client
from emailverifier import exceptions
import simplejson as json


# Config email verifier

verifier = Client("at_xpgLenoojRMjEwBUZwILCtt7KvxMJ")


def emailVerifier(email='adom.466@gmail.com'):
    # Retrieve an info for the given email address
    try:
        f = verifier.get(email,  {'validateSMTP': 0, '_hardRefresh': 1}) # Verify email using api from whoisxmlapi.com
        
        # Convert JSON to PYTHON object
        convert = json.dumps(json.loads(f.json_string), indent=4)
        data = json.loads(convert)
        
        # Make checks to verify if email is good to be accepted or not.
        disposable_check = data['disposableCheck']
        catch_all_check = data['catchAllCheck']
        free_check = data['freeCheck']

        # Conditions
        if disposable_check == 'true' or catch_all_check == 'true':
            msg = "We do not recognize this email address. Please provide a valid email address."
            resp = {'message':msg, 'status_code':400}
            return resp
        elif free_check == 'false':
            msg = "Please use an email address from a free email provider like Gmail, Hotmail,etc."
            resp = {'message':msg, 'status_code':400}
            return resp

        msg = "Email has been verified and message has been sent."
        resp = {'message':msg, 'status_code':200}
        return resp
    except exceptions.HttpException:
        msg = "Sorry, an error has occured. Please try again later."
        resp = {'message':msg, 'status_code':500}
        return resp
    except exceptions.GeneralException:
        msg = "Sorry, an error has occured. Please try again later."
        resp = {'message':msg, 'status_code':400}
        return resp
    
