from flask import Flask, render_template, request, redirect, url_for,flash
import mysql.connector 

app = Flask(__name__)
app.secret_key = 'lkjh76'

conn = mysql.connector.connect(
    host='localhost',       
    database='portfolio_website', 
    user='root',            
    password=''     
)
if conn.is_connected():
    print("Successfully connected to MySQL database")
else:
    print("MySQL database connection failed")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['full_name']
        email_id = request.form['email_id']
        mobile_no=request.form['mobile_no']
        email_subject=request.form['email_subject']
        message=request.form['message']
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name,email_id,mobile_no,email_subject,message) VALUES (%s, %s,%s,%s,%s)", (name,email_id,mobile_no,email_subject,message))
        conn.commit()
        cursor.close()
        msg= "Form submitted successfully!"
    else:
        msg="An error occurred while submitting the form. Please try again."
        
    return render_template('msg.html',msg=msg)

@app.route('/')
def index():
    return render_template('p_index1.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)
