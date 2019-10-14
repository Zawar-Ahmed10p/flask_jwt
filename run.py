#print (python.__version__)

from flask import Flask
from flask_restful import Api
import controller, repositories
from repositories.model import RevokeUserToken
import services.resources as resources
from flask_jwt_extended import JWTManager


app=Flask(__name__)
app.config['JWT_SECRET_KEY']='secret-string'
app.config['JWT_BLACKLIST_ENABLED']=True
app.config['JWT_BLACKLIST_TOKEN_CHECKS']=['access','refresh']

jwt = JWTManager(app)
api = Api(app)

api.add_resource(resources.user_registration,'/registration')
api.add_resource(resources.user_login,'/login')
api.add_resource(resources.all_users,'/users')
api.add_resource(resources.secured_resource,'/secured')
api.add_resource(resources.refresh_token,'/refresh')
api.add_resource(resources.user_logout_access,'/logout/access')

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokeUserToken.check_jwt_list(jti)