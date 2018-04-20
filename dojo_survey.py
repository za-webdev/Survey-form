from flask import Flask ,render_template,request,redirect,session,flash
import re
app=Flask(__name__)

app.secret_key = "vsdkjnfskj/nsknjscdckj"


@app.route('/')
def user():

	return render_template('index.html')

@app.route('/process', methods=['post'])
def process():

	valid = True
	if len(request.form["name"]) < 1:
		flash("Name field is required!")
		valid = False
	elif len(request.form["name"]) < 2:
		flash("Name must be 2 characters or longer")
		valid = False


	if len(request.form["comment"])<1:
		flash("Comment field is required")
		valid=False
	elif len(request.form['comment'])>120:
		flash("Comment must be less than 120 chracters")
		valid=False
	if not valid:
		print("there was an error")
		return redirect("/")
		
	
	return render_template('result.html',data=request.form)



app.run(debug=True)


