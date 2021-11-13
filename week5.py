
import sqlite3
class DB_TEST:
    def __init__(self):
        #멤버변수 추가
        self.start()

    def start(self):
        id=input('아이디: ')
        pw=input('비번: ')
        conn=sqlite3.connect('test.db')
        cur=conn.cursor()
        
        cur.execute("SELECT * FROM user WHERE id = '" + id + "' and password = ' " + pw + " '")
        result=cur.fetchall()
        # cur.execute("SELECT * FROM user2")
        # self.data=cur.fetchall()
        
        
        #cur.execute("CREATE TABLE user2 (id TEXT PRIMARY KEY, pasword TEXT)")
        #cur.execute("DROP TABLE user")
        #cur.execute("CREATE TABLE user2 (id TEXT PRIMARY KEY, pasword TEXT)")
        #cur.execute("INSERT INTO user2 VALUES('testvf','1234')")
        #cur.execute("UPDATE user2 SET id='test' WHERE id='testid'")
        print(result)
        conn.commit()
        conn.close()
        if len(result)==0:
            print('로그인 실패')
        elif len(result)!=0:
            print('로그인 성공')
        
        
        




if __name__== "__main__":
    db=DB_TEST()

