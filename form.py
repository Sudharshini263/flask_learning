from flask import Flask, render_template, url_for, request, redirect

app= Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    return render_template("form.html")


@app.route("/welcome", methods=["POST"])
def user():
    if request.method == 'POST':
        name = request.form.get("uname")
        
        if request.form.get("pass") == "1234":
            return render_template("msg.html", name=name)
        
        return redirect(url_for('home'))
 

if __name__=='__main__':
    app.run(debug=True)
    