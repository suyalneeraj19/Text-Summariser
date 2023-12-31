from flask import Flask,render_template,request
from text_summary import summariser

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze',methods=["GET","POST"])

def analyze():
        if request.method=="POST":
            rawtext=request.form['rawtext']
            summary,orignal_txt,len_orig_txt,len_summary=summariser(rawtext)
        return render_template('summary.html',summary=summary,orignal_txt=orignal_txt,len_orig_txt=len_orig_txt,len_summary=len_summary)
if __name__=="__main__":
        app.run(debug=True)