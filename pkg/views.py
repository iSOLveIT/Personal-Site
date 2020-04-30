# Third-party modules 
from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash
# Local modules 
from .contact import sendEmail, replyMessage
from .email_verify import emailVerifier


# View for Index Route
class IndexEndpoint(MethodView):
    """View for Index Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        get() and post() methods
    """

    def get(self):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """

        return render_template('index.html'), 200


    def post(self):
        """This function executes when request method for this route = post
        
        Returns:
            index.html -- redircet to the contact-secetion of index route 
        """

        fullname = request.form['nameInput']
        subject = request.form['subjInput']
        email = request.form['emailInput']
        body = request.form['bodyInput']
            
        # Verify Email Address
        verify_email = emailVerifier(email) 
        if verify_email['status_code'] == 400:
            # Return the message for the error
            message = verify_email['message']
            flash(message=message, category='danger')

        elif verify_email['status_code'] == 500:
            # Return the message for the error
            message = verify_email['message']
            flash(message=message, category='danger')

        elif verify_email['status_code'] == 200:
            # Return message for success
            sendEmail(fullname, subject, email, body)   # Message from customer to organization
            replyMessage(email, fullname)   # Message from organization to customer
            message = verify_email['message']
            flash(message=message, category='success')

        return redirect(url_for('index', _anchor='contact-section'))
