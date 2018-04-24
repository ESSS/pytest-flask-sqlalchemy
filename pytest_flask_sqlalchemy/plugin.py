import pytest


@pytest.fixture(scope='session')
def db_engine(flask_app):
    """
    Setup the database for a test session and drop all tables after the
    session ends. It is not intended to be used on tests functions,
    use `db_session` instead.
    """
    db = flask_app.extensions['sqlalchemy'].db
    with flask_app.app_context():
        db.create_all()
        yield db.engine
        db.drop_all()


@pytest.fixture()
def db_session(flask_app, db_engine, request):
    """
    Creates a new database transaction for the test and roll it back
    when the test is completed
    """
    db = flask_app.extensions['sqlalchemy'].db
    connection = db_engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def finalize():
        db.session.close()
        transaction.rollback()
        connection.close()

    request.addfinalizer(finalize)
    return session
