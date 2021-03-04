from flask import Flask,render_template
app=Flask(__name__)#creating new flask object

@app.route("/")

def main():
	return "My First Flask Web App"

@app.route("/demo")

def demo1():
	return "Demo Page"

@app.route("/admin")

def demo2():
	return "Admin Page"

@app.route("/user")
def demo3():
	return "User Page"

@app.route("/user/<name>")
def demo4(name):
	return "Hello %s" %name

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/demo_1")
def demo_1():
	return render_template("demo_1.html")

@app.route("/About")
def About():
	return render_template("About.html")

@app.route("/demo_2")
def demo_2():
	return render_template("demo_2.html")

@app.route("/demo_3")
def demo_3():
	return render_template("demo_3.html")

@app.route("/demo_4")
def demo_4():
	return render_template("demo_4.html")

@app.route("/sample")
def sample():
	return render_template("sample.html")

if(__name__)=='__main__':
	app.run(debug=True)
