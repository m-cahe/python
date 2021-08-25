import pymongo

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))

def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        #오류발생. MONGO_CONN이라고 같은 변수 지정하면 위의 변수가 인정이 안됌
        MONGO_CON = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CON.blog_session_db.blog_db
    return blog_ab