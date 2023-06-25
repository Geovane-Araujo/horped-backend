from flask import Flask, request

from config.database import new_connections_sqlite
from exceptions.exception import hubExcept
from service import room_service, room_message_service
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(hubExcept)
cnn = new_connections_sqlite()


@app.route('/')
def hello_world():
    return 'no authorized'

@app.route('/room', methods = ['POST'])
def create_room():
    return room_service.create_room(request,cnn)

@app.route('/authenticate_room', methods = ['POST'])
def authenticate_room():
    return room_message_service.verify_room(request,cnn)

@app.route('/send_message', methods = ['POST'])
def send_message():
    return room_message_service.send_message(request,cnn)

@app.route('/get_message', methods = ['POST'])
def get_message():
    return room_message_service.get_message(request,cnn)










if __name__ == '__main__':
    app.run()
