# Third-party modules 
from flask_mail import Message
# Local modules 
from pkg import mail
# Built-in modules 
from datetime import datetime as dt


def sendEmail(_name, _email, _body):
    """Function for sending emails
    
    Arguments:
        _name {[str]} -- name of person contacting the organisation
        _subject {[str]} -- subject of the message being sent to the organisation
        _email {[str]} -- email address of person contacting the organisation
        _body {[str]} -- body of the message being sent to the organisation
    
    Returns:
        {[str]} -- OK
    """

    _recipient = 'isolveitgroup@gmail.com'
    _subject = 'Enquiry'
    msg = Message(_subject, sender=('iSOLveIT Contact', 'isolveitgroup@gmail.com'), recipients=[_recipient])
    msg.body = f'''{_body}


Sender's Name: {_name}
Sender's Email: {_email}
Date Sent:  {dt.now().strftime('%B %d, %Y, %H:%M ') + 'GMT'}
'''
    mail.send(msg)
    return 'OK'


def replyMessage(_email, _sender):
    """Function for replying emails
    
    Arguments:
        _email {[str]} -- email address of person contacting the organisation
        _sender {[str]} -- name of person the organisation is sending the message to

    Returns:
        {[str]} -- OK
    """

    _subj = 'Message Received'
    mesg = Message(_subj, sender=('iSOLveIT Contact', 'isolveitgroup@gmail.com'), recipients=[_email])
    mesg.body = f'''Hello {_sender},
The message sent by {_sender} to iSOLveIT has been received. iSOLveIT will contact you within 24 hours.

Thank you,
iSOLveIT Team.

Date Sent:  {dt.now().strftime('%B %d, %Y, %H:%M ') + 'GMT'}
'''
    mail.send(mesg)
    return 'OK'
