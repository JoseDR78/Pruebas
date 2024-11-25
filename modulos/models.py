from modulos import db

class USUARIOS(db.Model):
    USUCLAVE = db.column(db.integer, primary_key = True)
    USUNICKNAME = db.column(db.String(50), unique = True, nullablle = False)
    USUPASSWORD = db.column(db.Text, nullablle = False)

    def __init__(self, USUNICKNAME, USUPASSWORD):
        self.USUNICKNAME = USUNICKNAME
        self.USUPASSWORD = USUPASSWORD

    def __repr__(self):
        return f'<USUARIOS: {self.USUNICKNAME}>'