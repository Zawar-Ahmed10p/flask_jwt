from . import posts, token_db
from passlib.hash import pbkdf2_sha256 as sha256


class UserRepo():

    def __init__(self):
        pass

    def authenticate(self, post_data):
        print(post_data['Name'])

        search = posts.find({'Name': post_data['Name'], 'Pwd': post_data['Password']})
        # print (search)
        for it in search:
            if it['username'] == post_data['username'] and it['password'] == post_data['password'] and UserRepo.verify_hash(
                    post_data['password']):
                print(it['Id'])
                return it['Id']
        return False

    def signup_user(self, post_data):
        post_data['password'] = UserRepo.generate_pwd_hash(post_data['password'])
        result = posts.insert_one(post_data)
        if result.inserted_id:
            print('One post: {0}'.format(result.inserted_id))
            return result.inserted_id
        else:
            return False

    def save_user(self, post_data):
        result = posts.insert_one(post_data)
        if result.inserted_id:
            print('One post: {0}'.format(result.inserted_id))
            return True
        else:
            return False

    def update_user(self, id, post_data):
        update = posts.update_one({"Id": id}, post_data)
        print(update)
        return update

    def search_user(self, name):
        search = posts.find({'Name': name})
        '''for it in search:
            print(it)'''
        # print("ds",search)
        return search

    def delete_user(self, id):
        delete = posts.remove({"Id": id})
        return delete

    def get_all_users():
        all_data = posts.find({})
        return all_data

    @staticmethod
    def generate_pwd_hash(pwd):
        return sha256.hash(pwd)

    @staticmethod
    def verify_hash(pwd, hash):
        return sha256.verify(pwd, hash)


class RevokeUserToken():
    def __init__(self):
        pass

    @classmethod
    def check_jwt_list(cls, jti):
        try:
            query=token_db.find_one({'token': jti})

            print(query['token'])
            return query['token']
        except:
            pass
        #token_db.insert_one({'token': jti})

    def add_token(self, jti):
        token_db.insert_one({'token': jti})
