import pymysql


class mysql_api:

    def connect_wxremit_db(self):
        return(pymysql.connect('106.12.22.3', 'weiqing', '550312171', 'weiqing'))

    def insert_file_rec(self, dbname, listname, url):
        con = self.connect_wxremit_db()
        cur = con.cursor()
        # sql_str = ("INSERT INTO url (geturl)" + "VALUES ('%s')" % (url))
        sql_str = ("INSERT INTO %s" % (dbname) + "(%s)" %
                   (listname) + "VALUES ('%s')" % (url))
        try:
            cur.execute(sql_str)
            con.commit()
        except:
            con.rollback()
        finally:
            cur.close()
            con.close()

    def insert_file_recs(self, dbname, url,url2,url3):
        con = self.connect_wxremit_db()
        cur = con.cursor()
        sql_cha = ("SELECT uname FROM %s" % (dbname) + " WHERE uname = '%s'" % (url))
        cur.execute(sql_cha)
        result = cur.fetchall()
        result = str(result)
        if (result == "()"):
            sql_str = ("INSERT INTO %s" % (dbname) + "(uname,utel,kecheng)" + "VALUES ('%s','%s','%s')" % (url,url2,url3))
            try:
                cur.execute(sql_str)
                con.commit()
            except:
                con.rollback()
            finally:
                cur.close()
                con.close()


        

    def random_geturl(self):
        con = self.connect_wxremit_db()
        cur = con.cursor()
        sql_sele = ("SELECT * FROM url WHERE id >= (SELECT floor( RAND() * ((SELECT MAX(id) FROM url)-(SELECT MIN(id) FROM url)) + (SELECT MIN(id) FROM url)))  ORDER BY id LIMIT 1;")
        cur.execute(sql_sele)
        results = cur.fetchall()
        return (results[0][1])
        
    def SelectPhone(self,name):
        con = self.connect_wxremit_db()
        cur = con.cursor()
        sql_str = ("SELECT utel FROM `ims_ypuk_tchk_usercontact` WHERE uname = '%s'" % (name))
        cur.execute(sql_str)
        result = cur.fetchall()
        return result

    def getname(self,name):
        con = self.connect_wxremit_db()
        cur = con.cursor()
        sql_str = ("SELECT * FROM `ims_ypuk_tchk_kecheng` WHERE uname = '%s'" % (name))
        cur.execute(sql_str)
        result = cur.fetchall()
        return result



sql = mysql_api()
