from flask import Flask
from flask_restful import Api,Resource,reqparse

app = Flask(__name__)
api = Api(app)

class CrearUsuario(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('correo', type=str, help='Correo Electronico')
            parser.add_argument('passwd', type=str, help='Contraseña')
            args = parser.parse_args()
            _correo = args['correo']
            _passwd = args['passwd']
            return {'correo' : args['correo'], 'password': args['passwd']}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(CrearUsuario, '/usuario')

if __name__ == '__main__':
    app.run(debug=True)