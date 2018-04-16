import auth

auth.authenticator.add_user("Howard", "howard1234")
auth.authrizor.add_permission("test")
auth.authrizor.add_permission("change")
auth.authrizor.add_permission("root")
auth.authrizor.permit_user("test", "Howard")
auth.authrizor.permit_user("root", "Howard")

class Editor:
    def __init__(self):
        self.uname = None
        self.cmds = {
            "login": self.login,
            "logout": self.logged_out,
            "test": self.test,
            "change": self.change,
            "add_user": self.add_user,
            "permit_user": self.permit_user,
            "quit": self.quit
        }

    def add_user(self):
        success = False
        while not success:
            print("Add user:")
            uname = input("username: ")
            pwd = input("password: ")

            try:
                auth.authenticator.add_user(uname, pwd)

            except auth.UserNameAlreadyExist:
                print(f"{uname} already exits.")

            except auth.PassWordTooShort:
                print(f'password should be at least 6 digit.')

            else:
                print(f"Add User: {uname}")
                success = True

    def permit_user(self):

        try:
            is_permit = auth.authrizor.check_permission("root", self.uname)

        except auth.NotLoggedInError:
            print("User not login.")

        except auth.PermissionError as e:
            print(e)

        except auth.NotPermittedError:
            print('Only root user and use this function.')

        else:
            if is_permit:
                success = False
                while not success:
                    perm_name = input("permission: ")
                    uname = input("username: ")

                    try:
                        auth.authrizor.permit_user(perm_name, uname)

                    except auth.PermissionError as e:
                        print(e)

                    except auth.InvalidUserName:
                        print("User is not exist")
                        self.add_user()

                    else:
                        print(f'Permit {uname} {perm_name} success!')
                        success = True

    def login(self):
        logged_in = False

        while not logged_in:
            uname = input("username: ")
            pwd = input("password: ")

            try:
                logged_in = auth.authenticator.login(uname, pwd)

            except auth.InvalidUserName:
                print("Sorry, the user don't exist.")

            except auth.InvalidPassword:
                print("Sorry, the password is incorrect.")

            else:
                self.uname = uname
                print(auth.authenticator.users[uname])

    def is_permitted(self, perm_name):
        try:
            auth.authrizor.check_permission(perm_name, self.uname)

        except auth.NotLoggedInError:
            print(f'{self.uname} is not logged in.')
            return False

        except auth.PermissionError as e:
            print(e)
            return False

        except auth.NotPermittedError:
            print(f'{self.uname} can not {perm_name}')
            return False

        else:
            return True

    def test(self):
        if self.is_permitted("test"):
            print("Testing progam now...")

    def change(self):
        if self.is_permitted("change"):
            print("Change program now...")

    def logged_out(self):
        if not self.uname:
            raise auth.NotLoggedInError(self.uname)

        try:
            auth.authenticator.logout(self.uname)

        except Exception as e:
            print(e)

        else:
            print(f'{self.uname} logged out.')
            print(auth.authenticator.users[self.uname])
            self.uname = None


    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            cmd = None
            while True:
                print(
                    '''
                Please enter a command:
                login: Login
                logout: Logout
                test: Test the program
                change: Change the program
                add_user: Add new user
                permit_user: Permit user
                quit: quit
                ''')

                cmd = input(">").lower()

                try:
                    func = self.cmds[cmd]

                except KeyError:
                    print("Command not found.")

                else:
                    try:
                        func()
                    except auth.NotLoggedInError:
                        print("User not login.")

        finally:
            print("Program exit.")

edit = Editor()

if __name__ == '__main__':
    edit.menu()