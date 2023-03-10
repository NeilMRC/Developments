from flask import Flask, render_template, jsonify, request
from sympy import *
from math1 import solveforx, derivative, integration

app = Flask(__name__)
Company="NMRC"



@app.route("/")
def hello_world():
  # jobs = get_jobs_from_db()
  return render_template("home.html", company_name=Company)

@app.route("/calculator",methods=['post','get'])
def calculator():
  def toggle_button():
    print("Toggle buttton")
    # el = document.querySelector('.content_section')
    # if el.style.visibility == 'hidden' :
    #   el.style.visibility == 'visible'
    # else:
    #   el.style.visibility == 'hidden'
  
  method = request.method
  print("\nrequest method: ",method)
  data = request.form
  if method=='POST':
    print("data is:",data)
    
  
  return render_template("calculator.html", company_name = Company, method = method)

@app.route('/calculator/<int:id>',methods=['post'])
def calculator_result(id):
  # Get the data from the form
  eq1 = request.form.get('eq1')
  var1 = request.form.get('var')
  if id==1:
    eq1 = request.form.get('eq1')
    var1 = request.form.get('var')
    result = solveforx(eq1)
    print("Result:",result,"type of result:",type(result))

    return render_template("resolve.html", eq1 = eq1, var1 = var1, res = result, id = id)
  elif id == 2:
    result = derivative(eq1)
    return render_template("resolve.html", eq1 = eq1, var1 = var1, res = result, id = id)
    
  elif id == 3:
    result = integration(eq1)
    return render_template("resolve.html", eq1 = eq1, var1 = var1, res = result, id = id)
    
@app.route('/foo', methods=['post','get']) 
def foo():
    data = request.json
    return jsonify(data)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)