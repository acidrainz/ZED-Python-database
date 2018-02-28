import MySQLdb
import sys


class DB():

  def __init__(self):
    self.query = ""

    try:
      self.db = MySQLdb.connect(host='localhost', user='root', password='', db='python')

    except Exeption as e:
      sys.exit('connection error check your connection data')

  def table(self, table):
    self.table = str(table)
    return self

  def all(self):
    if hasattr(self, 'table'):
        try:
          self.cursor = self.db.cursor()
          query = "SELECT * FROM " + self.table
          self.cursor.execute(query)
          self.result = self.cursor.fetchall()
          return self.result
        except Exception as e:
          print(e)
        finally:
          self.cursor.close()
          self.db.close()
          self.table = ""
          self.query = ""
    else:
      print("No Table Selected")

  def where(self, key, value):
    self.query = ""
    self.query += ' WHERE ' + str(key) + '=' + "'" + str(value) + "'"
    return self

  def orWhere(self, key, value):
    self.query += ' OR ' + str(key) + '=' + "'" + str(value) + "'"
    return self

  def whereNot(self,key,value):
    self.query = ""
    self.query += ' WHERE NOT ' + str(key) + '=' + "'" + str(value) + "'"
    return self

  def get(self):
    query = 'SELECT * FROM ' + self.table + self.query
    print(query)
    if hasattr(self, 'table'):
      try:
        self.cursor = self.db.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        return self.result
      except Exception as e:
        print(e)
      finally:
        self.cursor.close()
        self.db.close()
        self.table = ""
        self.query = ""
    else:
      print("No Table Selected")
  def orderBy(self, key, value):
    self.query += ' ORDER BY ' + str(key) + ' ' + str(value)
    return self

  def limit(self,count):
    self.query += ' LIMIT '+str(count)
    return self

  def update(self,data):
    dict(data)
    prms = ()
    args = ""
    x = list(prms)
    for k in data.keys():
      args += k+"= %s,"
      x.append("'"+data[k]+"'")

    z = tuple(x)
    y = args[:-1]
    query = ""
    query += "UPDATE `"+self.table+"` SET "
    query += y
    try:
      query += self.query
      self.cursor = self.db.cursor()
      self.cursor.execute(query % z)
      self.db.commit();
      return self.cursor.rowcount
    except TypeError as e:
      print(e)
    finally:
      self.cursor.close()
      self.db.close()
      self.table = ""
      self.query = ""

  def create(self,data):
    dict(data)
    args = ""
    x = ""
    args += "("
    for k in data.keys():
      args += k + ","
      x += "'" + data[k] + "',"

    y = args[:-1]
    z = x[:-1]
    y += ")"
    query = ""
    query += "INSERT INTO `" + self.table + "` "
    query += y
    query += " VALUES "
    query += "("+z+")"
    try:
      self.cursor = self.db.cursor()
      self.cursor.execute(query)
      self.db.commit();
      return self.cursor.rowcount
    except TypeError as e:
      print(e)
    finally:
      self.cursor.close()
      self.db.close()
      self.table = ""
      self.query = ""
  def find(self,id):
    self.query += "WHERE id = "+str(id)
    return self
  def delete(self):
    query = "DELETE FROM `"+self.table+"`"+self.query
    try:
      self.cursor = self.db.cursor()
      self.cursor.execute(query)
      self.db.commit()
      return self.cursor.rowcount
    except Exception as e:
      print(e)
    finally:
      self.cursor.close()
      self.db.close()
      self.table = ""
      self.query = ""
  def query(self,query):
    try:
      self.cursor = self.db.cursor()
      self.cursor.execute(query)
      self.result = self.cursor.fetchall()
      return self.result
    except Exception as e:
      print(e)
    finally:
      self.cursor.close()
      self.db.close()


DB().table('users').find(3).delete()