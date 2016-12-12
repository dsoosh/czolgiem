import json

from flask import Flask, request

app = Flask(__name__)


class Directions(object):
    Stay = None
    Up, Down, Right, Left = range(4)


class Actions(object):
    Check, Bomb, Fire = range(3)


class Tiles(object):
    Empty, Reuglar, Fortified, Indestructible = range(4)


@app.route('/info')
def info():
    return {
        'Name': 'Czolgiem',
        'AvatarUrl': 'http://localhost/img/avatar.jpg',
        'Description': 'Uwaga szczelam',
        'GameType': 'TankBlaster'
    }


@app.route('/performnextmove', methods=['POST'])
def move():
    move = Directions.Down
    action = Actions.Fire
    fire_at = Directions.Left
    return json.dumps({
        'Direction': move,
        'Action': action,
        'FireDirection': fire_at
    })

if __name__ == '__main__':
    app.run()
