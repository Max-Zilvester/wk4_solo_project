from flask import Flask, render_template

from controllers.event_controller import events_blueprint
from controllers.member_controller import members_blueprint

app = Flask(__name__)

app.register_blueprint(events_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)