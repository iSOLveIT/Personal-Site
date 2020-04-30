# Local modules 
from .views import IndexEndpoint
from pkg import app


# Route for index
app.add_url_rule("/", view_func=IndexEndpoint.as_view("index"))
