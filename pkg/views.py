# Third-party modules 
from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash
# Local modules 
from .contact import sendEmail, replyMessage
from .email_verify import emailVerifier

# Standard library imports
from functools import lru_cache


# View for Index Route
class IndexEndpoint(MethodView):
    """View for Index Route
    
    Arguments:
        MethodView -- If you implement a request method (like GET), it will be used to handle GET requests.
    
    Returns:
        get() and post() methods
    """
    @lru_cache(maxsize=32)
    def get(self):
        """This function executes when request method for this route = get
        
        Returns:
            html template -- renders html template
        """

        return render_template('index.html')

    @lru_cache(maxsize=32)
    def post(self):
        """This function executes when request method for this route = post
        
        Returns:
            index.html -- redircet to the contact-secetion of index route 
        """

        fullname = request.form['nameInput']
        email = request.form['emailInput']
        body = request.form['bodyInput']
            
        # Verify Email Address
        verify_email = emailVerifier(email) 
        if verify_email['status_code'] == 200:
            # Return message for success
            sendEmail(fullname, email, body)   # Message from customer to organization
            replyMessage(email, fullname)   # Message from organization to customer
            flash(message=verify_email['message'], category='success')
            return redirect(url_for('index', _anchor='contact-alert'))

        # Return the message for the error
        flash(message=verify_email['message'], category='danger')
        return redirect(url_for('index', _anchor='contact-alert'))
