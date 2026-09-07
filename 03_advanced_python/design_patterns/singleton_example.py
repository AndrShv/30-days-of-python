class DBAccessClass:
    _saved = None
    _init_done = False
    user:str = "admin"
    password:str = ""

    def __new__(cls, *args, **kwargs):
        if cls._saved is None:
            cls._saved = super().__new__(cls)
        return cls._saved

    def __init__(self, user:str, password:str):
        if DBAccessClass._init_done:
            return
        self.user = user
        self.password = password
        DBAccessClass._init_done = True


fst_db = DBAccessClass(user="admin", password="secret")
snd_db = DBAccessClass(user="admin", password="secret")

print(fst_db is snd_db)