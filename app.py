import sentry_sdk
from flask import Flask
from sentry_sdk import capture_message
from sentry_sdk import set_level

sentry_sdk.init(
     dsn="https://b30ac8693dddb0716e79ca41a94537c8@o4508288106823680.ingest.us.sentry.io/4508684110856192",
   
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    capture_message('Something went wrong')
    set_level("warning")
    return "<p>Hello, World!</p>"
