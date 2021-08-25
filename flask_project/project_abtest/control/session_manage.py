from model.mongodb import conn_mongodb
from datetime import datetime

class BlogSession():
    blog_page = {'A':'indexA.html', 'B':'indexB.html'}
    session_count = 0

    @staticmethod #접속에 관한 정보 저장
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")

        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'session_ip':session_ip
            ,'user_email':user_email
            ,'page':webpage_name
            ,'access_time':now_time
        })
        # session_ip / user_email / page / access_time

    @staticmethod  #인자 넣기 (force=None)
    def get_blog_page(blog_id=None):
        if blog_id == None:
            if BlogSession.session_count == 0:
                BlogSession.session_count = 1
                return BlogSession.blog_page['A']
            else:
                BlogSession.session_count = 0
                return BlogSession.blog_page['B']
        else:
            return BlogSession.blog_page[blog_id]
