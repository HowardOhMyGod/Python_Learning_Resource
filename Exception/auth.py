import hashlib

class User:
    def __init__(self, uname, pwd):
        self.uname = uname
        self.pwd = self.encript_pwd(pwd)
        self.login = False

    def __str__(self):
        return f'({self.uname}, {self.login})'

    def encript_pwd(self, pwd):
        hash_string = self.uname + pwd
        hash_string = hash_string.encode('utf8')

        return hashlib.sha256(hash_string).hexdigest()

    def check_pwd(self, pwd):
        encrypted = self.encript_pwd(pwd)
        return encrypted == self.pwd

class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, uname, pwd):
        if uname in self.users:
            raise UserNameAlreadyExist(uname)
        if len(pwd) < 6:
            raise PassWordTooShort(uname)

        self.users[uname] = User(uname, pwd)

    def login(self, uname, pwd):
        try:
            user = self.users[uname]
        except KeyError:
            raise InvalidUserName(uname)

        if not user.check_pwd(pwd):
            raise InvalidPassword(uname)

        user.login = True
        return True

    def logout(self, uname):
        if not self.is_login(uname):
            raise NotLoggedInError(uname)

        try:
            user = self.users[uname]

        except KeyError:
            raise InvalidUserName(uname)

        else:
            user.login = False

    def is_login(self, uname):
        if uname in self.users:
            return self.users[uname].login

        return False

authenticator = Authenticator()

class Authrizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()

        else:
            raise PermissionError("Permission already exist")

    def permit_user(self, perm_name, uname):
        try:
            perm_set = self.permissions[perm_name]

        except KeyError:
            raise PermissionError("Permission do not exist")

        else:
            if uname not in self.authenticator.users:
                raise InvalidUserName(uname)

            perm_set.add(uname)

    def check_permission(self, perm_name, uname):
        if not self.authenticator.is_login(uname):
            raise NotLoggedInError(uname)

        try:
            perm_set = self.permissions[perm_name]

        except KeyError:
            raise PermissionError("Permission do not exist")

        else:
            if uname not in perm_set:
                raise NotPermittedError(uname)
            else:
                return True
authrizor = Authrizor(authenticator)



class AuthException(Exception):
    def __init__(self, uname, user=None):
        super().__init__(uname, user)
        self.uname = uname
        self.user = user

class UserNameAlreadyExist(AuthException):
    pass

class PassWordTooShort(AuthException):
    pass

class InvalidUserName(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class NotPermittedError(AuthException):
    pass

class NotLoggedInError(AuthException):
    pass

class PermissionError(Exception):
    pass

