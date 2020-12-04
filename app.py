from flask import Flask, jsonify, session, redirect, url_for, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import flask_login
from sqlalchemy.orm import relationship, backref

# store password in env variable
app = Flask(__name__)
app.secret_key='9f17ddrfa|bdb7dawe60eM95u'
engine = create_engine('mysql://admin:Admin12345@ctni.cmuad72yozvs.us-east-1.rds.amazonaws.com:3306/ctni', convert_unicode=True, echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class Account(Base):
    __table__ = Base.metadata.tables['account']

class CoilDetails(Base):
    __table__ = Base.metadata.tables['coildetails']

class CoilTest(Base):
    __table__ = Base.metadata.tables['coiltest']

class Groups(Base):
    __table__ = Base.metadata.tables['groups']

class Preference(Base):
    __table__ = Base.metadata.tables['preference']

class Profile(Base):
    __table__ = Base.metadata.tables['profile']

class Projects(Base):
    __table__ = Base.metadata.tables['projects']

class Reconstruction(Base):
    __table__ = Base.metadata.tables['reconstruction']

class Registration(Base):
    __table__ = Base.metadata.tables['registration']

class Roi(Base):
    __table__ = Base.metadata.tables['roi']

class Scan(Base):
    __table__ = Base.metadata.tables['scan']

class Study(Base):
    __table__ = Base.metadata.tables['study']


@app.route('/users',methods=['GET'])
def users():
    from sqlalchemy.orm import scoped_session, sessionmaker, Query
    db_session = scoped_session(sessionmaker(bind=engine))
    return(jsonify(db_session.Account.query.all()))
    item_list=[]
    for item in db_session.query(Account.User_ID, Account.Username,Account.Role).all():
        item_list+=item
    return(jsonify(item_list))

@app.route('/scans',methods=['GET'])
def scans():
    from sqlalchemy.orm import scoped_session, sessionmaker, Query
    db_session = scoped_session(sessionmaker(bind=engine))
    # return(jsonify(db_session.Account.query.all()))
    item_list = db_session.query(Scan.Scan_ID, Scan.SliceOrient).all()
    items = []
    #
    for item in item_list:
        items.append({'Scan_ID:' : item.Scan_ID, 'SliceOrient' : item.SliceOrient})

    return(jsonify({'scan' : items}))
    # return jsonify(item_list)
    # return jsonify(Scan.metadata.tables['scan'].columns.keys())

@app.route("/login", methods=["GET", "POST"])
def login():
    """For GET requests, display the login form.
    For POSTS, login the current user by processing the form.

    """
    print db
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data)
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("bull.reports"))
    return render_template("login.html", form=form)