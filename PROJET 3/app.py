from flask import Flask, render_template

app= Flask(__name__)

produits=[
    {
        "nom":"Ecouteurs",
        "prix":"120.000 GNF",
        "image":"2.jpg",
        "whatsapp":"611476352",
    },
    {
        "nom":"Power bank",
        "prix":"180.000 GNF",
        "image":"8.jpg",
        "whatsapp":"611476352",
    },
    {
        "nom":"Ecouteurs pro",
        "prix":"250.000 GNF",
        "image":"4.jpg",
        "whatsapp":"611476352",
    },
    {
        "nom":"Power bank pro",
        "prix":"350.000 GNF",
        "image":"6.jpg",
        "whatsapp":"611476352",
    },
     {
        "nom":"Sio pacotille",
        "prix":"3.000 GNF",
        "image":"sio1.jpg",
        "whatsapp":"611476352",
    },
     {
        "nom":"sio mal",
        "prix":"1.000 GNF",
        "image":"sio2.jpg",
        "whatsapp":"611476352",
    },
     {
        "nom":"sio un peu",
        "prix":"500 GNF",
        "image":"sio3.jpg",
        "whatsapp":"611476352",
    }


]
#Route Principale

@app.route("/")
def index():
    return render_template("index.html",produits=produits)

if __name__=="__main__":
        app.run(debug=True)