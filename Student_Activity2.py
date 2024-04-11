from flask import Flask, render_template
app = Flask(__name__)

#Na função, retorne render_template(‘index.html’)

@app.route("/Student_Activity2")
def student_webpage():
    #Crie uma variável
    name = 'João'
    # Passe a variável no modelo
    return render_template('Student_Activity2.html', student_name = name)
app.run(debug=True)