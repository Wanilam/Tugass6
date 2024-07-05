from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def beranda():
    return render_template("beranda.html")

@app.route("/login", methods =["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = "nilam"
        password = "1234"
        
        input_username = request.form.get("username")
        input_password= request.form.get("password")
        
        if input_username == username and input_password == password :
            return redirect(url_for("produk"))
        else :
             return redirect(url_for("login"))



@app.route("/produk")
def produk():
    return render_template("produk.html")

@app.route("/detail_produk")
def detail_produk():
    return render_template("detail_produk.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/pesanan_dikirm")
def pesanan_dikirm():
    return render_template("pesanan_dikirm.html")