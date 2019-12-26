from emailverifier import Client
from emailverifier import exceptions
import simplejson as json
from distutils.util import strtobool


# Config email verifier

verifier = Client("at_xpgLenoojRMjEwBUZwILCtt7KvxMJ")


def emailVerifier(email):
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

        dispose = str(disposable_check).capitalize()
        catch = str(catch_all_check).capitalize()
        free = str(free_check).capitalize()

        dispose_check = strtobool(dispose)
        catch_check = strtobool(catch)
        freeCheck = strtobool(free)

        # Conditions
        if bool(dispose_check) == True or bool(catch_check) == True:
            msg = "We do not recognize this email address. Please provide a valid email address."
            resp = {'message':msg, 'status_code':400}
            return resp
        elif bool(freeCheck) == False:
            msg = "Please use an email address from a free email provider like Gmail, Hotmail,etc."
            resp = {'message':msg, 'status_code':400}
            return resp

        msg = "Email is verified and message has been sent."
        resp = {'message':msg, 'status_code':200}
        return resp
    except exceptions.HttpException:
        msg = "Sorry, we cannot access email service now. Please try again later."
        resp = {'message':msg, 'status_code':500}
        return resp
    except exceptions.GeneralException:
        msg = "Sorry, we cannot access email service now. Please try again later."
        resp = {'message':msg, 'status_code':500}
        return resp
    
