
import flask
import pywebio
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *    
from pywebio.session import *
from pywebio.pin import *


def main():
    name = input("What is your name?")
    greetings = 'Greetings',name,'!'
    popup('Greetings', greetings)
    toast('New message 🔔')

#start_server(main, port=8080, debug=True)
pywebio.platform.flask.webio_view(main, cdn=True, session_expire_seconds=None, session_cleanup_interval=None, allowed_origins=None, check_origin=None)
pywebio.platform.flask.start_server(main, port=8080, host='', cdn=True, static_dir=None, remote_access=False, allowed_origins=None, check_origin=None, session_expire_seconds=None, session_cleanup_interval=None, debug=False, max_payload_size='200M')