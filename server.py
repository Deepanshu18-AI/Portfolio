import csv

from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def my_home():
   # print(url_for('static', filename = 'favicon.ico'))
    return render_template ('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#to write on a file instead of csv file:
#def write_to_file(data):
    #with open ('database.txt', mode='a') as database:
        #email = data["email"]
        #subject = data["subject"]
        #message = data["message"]
        #file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open ('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
          data = request.form.to_dict()
          write_to_csv(data)
          return redirect('/thankyou.html')
        except:
          return 'did not save to database'
    else:
        return 'something went wrong. Try again!'



#example for individual pages:

#@app.route('/works.html')
#def work():
   # return render_template('works.html')

#@app.route('/contact.html')
#def contact():
    #return render_template('contact.html')

