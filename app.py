from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Marc Marshall! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/favorite-course')
def course():  # question one for module 8
    print('Subject: ' + request.args.get('subject'))
    print('Course Number: ' + request.args.get('course_number'))
    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():  # new route created for contact
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

@app.route('/greeting')
def greeting():  # put application's code here
    fun_courses = ['BMGT407', 'BMGT402', 'BMGT302', 'BMGT404']
    return render_template('greeting.html', courses=fun_courses)

if __name__ == '__main__':
    app.run()
