# Third-party modules 
from flask_mail import Message
# Local modules 
from pkg import mail, app
# Built-in modules 
from datetime import datetime as dt
from dateutil import tz

GMT_tz = tz.gettz(name="Africa/Accra")  # Set time-zone based IANA standards
today = dt.now(tz=GMT_tz)


def sendEmail(_name, _email, _body):
    """Function for sending emails
    
    Arguments:
        _name {[str]} -- name of person contacting the organisation
        _email {[str]} -- email address of person contacting the organisation
        _body {[str]} -- body of the message being sent to the organisation
    
    Returns:
        {[str]} -- OK
    """

    _mailer = app.config['MAIL_USERNAME']
    msg = Message("Contact Form", sender=('iSOLveIT Contact', f'{_mailer}'), recipients=[f'{_mailer}'])
    msg.body = f'''{_body}


Sender's Name: {_name}
Sender's Email: {_email}
Date Sent:  {dt.now(tz=GMT_tz).strftime('%B %d, %Y, %H:%M ') + 'GMT'}
'''
    mail.send(msg)
    return 'OK'


def replyMessage(_email, _name):
    """Function for replying emails
    
    Arguments:
        _email {[str]} -- email address of person contacting the organisation
        _name {[str]} -- name of person the organisation is sending the message to

    Returns:
        {[str]} -- OK
    """

    _mailer = app.config['MAIL_USERNAME']
    mesg = Message("Message Received", sender=('iSOLveIT Contact', f'{_mailer}'), recipients=[_email])
    mesg.body = f'''Hello {_name},
The message you sent to Randy has been received. 
Randy will contact you within 24 hours.
Thank you.

Regards,
Randy

Date Sent:  {dt.now(tz=GMT_tz).strftime('%B %d, %Y, %H:%M ') + 'GMT'}
'''
    mail.send(mesg)
    return 'OK'
