class Config:
    DEBUG = True
    MONGOALCHEMY_DATABASE = 'testMongo'


    THREADS_PER_PAGE = 2
    CSRF_ENABLED     = True
    CSRF_SESSION_KEY = "mongoAPP@SECRET#321$123@456"
    SECRET_KEY = "mongoAPP@SECRET#321$123@456"
    static_folder = "static"
