from app import db

class User(db.Model):

    def __init__(self, name, email):
      self.name = name
      self.email = email

    id = db.Column(db.Integer, primary_key=True)
    # uuid
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(50))
    phone_no = db.Column(db.String, unique=True)
    sms_confirmed = db.Column(db.Boolean)
    details = db.Column(db.String)
    user_photo = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    # userlockpwd = db.relationship('Userlogin', backref='user', lazy='dynamic')
    # usersession = db.relationship('Usersession', backref='user', lazy='dynamic')
    # userbusiness = db.relationship('Business', backref='user', lazy='dynamic')

#     @classMethos

def __repr__(self):
        return '<id {}>'.format(self.id)

class Userlogin(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    password_locked = db.Column(db.Boolean)
    temp_access_code = db.Column(db.String)
    created_at = db.Column(db.DateTime)

#     @classMethos

    def __repr__(self):
         return '<id {}>'.format(self.id)


class Usersession(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_token = db.Column(db.String)
    expired = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

#     @classMethos
    def __repr__(self):
         return '<id {}>'.format(self.id)

class Business:

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    description = db.Column(db.String)
    industry = db.Column(db.String)
    business_photo = db.Column(db.String)
    location = db.Column(db.String)
    expense_id = db.Column(db.Integer, db.ForeignKey('Expense_Type.id'))
    sales_id = db.Column(db.Integer, db.ForeignKey('Sales_Type.id'))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

#     @classMethos
    def __repr__(self):
         return '<id {}>'.format(self.id)

#
# class Expense_Type:
#
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
#
# #     @classMethos
#
#
# class Sales_Type:
#
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
#
# #     @classMethos
#
#
# class Business_Expense:
#
#     id = db.Column(db.Integer, primary_key=True)
#     business_id = db.Column(db.Integer, db.ForeignKey('Business.id'))
#     expense_id = db.Column(db.Integer, db.ForeignKey('Expense_Type.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
#     description = db.Column(db.String)
#     business_expense_photo = db.Column(db.String)
#     location = db.Column(db.String)
#     units = db.Column(db.Integer, default=1)
#     expense = db.Column(db.Integer)
#     business_expense_photo = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
#     updated_at = db.Column(db.DateTime)
#
# #     @classMethos
#
#
# class Business_Sale:
#
#     id = db.Column(db.Integer, primary_key=True)
#     business_id = db.Column(db.Integer, db.ForeignKey('Business.id'))
#     sale_id = db.Column(db.Integer, db.ForeignKey('Sales_Type.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
#     description = db.Column(db.String)
#     business_sale_photo = db.Column(db.String)
#     location = db.Column(db.String)
#     units = db.Column(db.Integer, default=1)
#     business_sale_photo = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
#     updated_at = db.Column(db.DateTime)
#
# #     @classMethos
#
#
# class Business_Transaction:
#
#     id = db.Column(db.Integer, primary_key=True)
#     business_id = db.Column(db.Integer, db.ForeignKey('Business.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
#     business_type_id = db.Column(db.Integer)
#     business_type = db.Column(db.String)
#     created_at = db.Column(db.DateTime)
#     updated_at = db.Column(db.DateTime)
#
# #     @classMethos