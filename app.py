from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import sqlite3

#cur.execute('''CREATE TABLE IF NOT EXISTS Attendance
#    (count TEXT)''')
#cur.execute('''INSERT INTO Attendance (count)
#                VALUES (12)''')
#conn.commit()
#cur.close()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {} \n Technical Hub Team".format(msg))
    try:
        conn = sqlite3.connect('attendancereport.sqlite')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Attendance
                (id INTEGER PRIMARY KEY AUTOINCREMENT, count TEXT)''')
        cur.execute('''INSERT INTO Attendance (count)
                VALUES (?)''', (msg, ))
        conn.commit()
        cur.close()

    except:
        print(msg)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

