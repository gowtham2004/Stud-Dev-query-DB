from flask import Flask, request, session, jsonify
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'fasdgfdgdfg'


@app.route('/',methods=["POST","GET"])
def addrec():
   try:
      query = request.form['query']
      now = datetime.now()
      cur_time = now.strftime("%D:%H:%M:%S")
      with sql.connect("chat_data.db") as con:
         cur = con.cursor()
         cur.execute("INSERT INTO queries (time,query) VALUES (?,?)",(cur_time,query) )
         con.commit()
         msg = "Record successfully added!"
         con.close()
   except:
      con.rollback()
      msg = "error in insert operation"
      
   finally:
      return jsonify(msg)


if __name__ == '__main__':
   app.run(debug = True)