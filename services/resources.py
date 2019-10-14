from flask_restful import Resource,reqparse
from repositories.model import UserRepo,RevokeUserToken
from bson.json_util import dumps
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)
from logger import log
from logger import log,Print_log

#print("hello")
#log = get_logger(__name__)
parser = reqparse.RequestParser()
parser.add_argument('username',help="Required Field",required=True)
parser.add_argument('password',help="Required Field",required=True)


class user_registration(Resource):
    def post(self):
        data = parser.parse_args()
        #print(data)
        data_id=UserRepo().signup_user(data)

        access_token=create_access_token(identity=data['username'])
        refresh_token=create_refresh_token(identity=data['username'])

        response={'message':'User created {'.format(data['username']),
                  'access_token':access_token,
                  'refresh_token':refresh_token
                  }

        return response
        #return {'message':'User Registraton'}


class user_login(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()
        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])

        response = {'message': 'Logged in as {}'.format(data['username']),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                    }
        return data
        #return {'message':'User Login'}


class all_users(Resource):
    def post(self):
        data=dumps(UserRepo.get_all_users())
        print(data)
        return data

class secured_resource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer':42
        }

class refresh_token(Resource):
    @jwt_refresh_token_required
    def post(self):
        secured_user=get_jwt_identity()
        access_token=create_access_token(identity=secured_user)
        return {'access_token':access_token}

class user_logout_access(Resource):
    @jwt_required
    def post(self):
        jti=get_raw_jwt()['jti']
        try:
            revoked_token=RevokeUserToken(jti=jti)
            print(revoked_token)
            #RevokeUserToken.add_token(revoked_token)
            return {'message': 'Access token has been revoked'}
        except Exception as e:
            print(e)
            return {'message': 'Something wrong'}