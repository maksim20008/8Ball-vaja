from flask import Flask, render_template, request
import random
# pip install flask
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():

    return render_template("index.html")
    #return "<p>Hellooooooooo World!</p>"


@app.route("/8ball", methods = ["POST"])
def ball():
    tmp = dict(request.form)
    ime1 = tmp.get("ime1")
    mylist = ["Da", "Ne", "Mogoče", "Vprašaj kasneje", 
          "Seveda, zakaj pa ne?", 
          "Verjetno, ampak raje ne tvegam.",
          "Kdo ve? Morda sem tudi jaz v dilemi.",
          "To ni tvoja stvar.",
          "Nisem prepričan, poskusi z Googlom.",
          "Počakaj, da se planet premakne.",
          "Možno, ampak se moram najprej naspati.",
          "Nikoli ne veš, kaj bo jutri.",
          "Prekriži prste in si poželi nekaj!",
          "Če bi le vedela, kaj si želim tudi jaz!",
          "Bolj se pomeri, bolj te bo zmotil odgovor.",
          "Izberi svoj odgovor, jaz samo svetujem."]
    r = f"{ime1} = {random.choice(mylist)}"

    return render_template("index.html", rezultat = r)
    #return f"{ime1} + {ime2} = {random.randint(0,100)} %"


app.run(debug= True)