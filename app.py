from flask import Flask
app = Flask(__name__)
app.port = 5001

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/test')
def test():
   return 'Testing, testing!'

@app.route('/report/room/<int:room>/lamp/<int:lamp>/state/<state>')
def report_room(room, lamp, state):
   if state != 'on' and state != 'off':
      return f'Bad state {state}'
   with open("data.log", "a") as filehandle:
      filehandle.write(f"room {room} lamp {lamp} state {state}\n")
   return f'Report lamp {lamp} in room {room} is set {state}'

if __name__ == '__main__':
   app.run("0.0.0.0", 5001, True)