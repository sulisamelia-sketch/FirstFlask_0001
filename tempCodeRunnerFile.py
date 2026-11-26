from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    hasil_pesan = None
    nama_input = ""

    if request.method == "POST":
        nama_input = request.form.get("nama", "").strip()
        if nama_input:
            hasil_pesan = f"Halo, {nama_input}! Data berhasil diterima lewat method POST."
        else:
            hasil_pesan = "Silakan isi kolom teks terlebih dahulu."

    return render_template("index.html", hasil=hasil_pesan, nama=nama_input)


if __name__ == "__main__":
    app.run(debug=True)