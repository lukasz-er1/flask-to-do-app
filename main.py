from flask import Flask, render_template, flash
import sqlite3
from baza_danych import wyswietl_dane, pobierz_dane

todo = Flask(__name__)
todo.secret_key = "super secret key"


@todo.route('/')
def main():
    zadania = wyswietl_dane()
    return render_template('main.html', zadania=zadania)


@todo.route('/dodaj/', methods=["GET", "POST"])
def dodaj():
    pobierz_dane()
    return render_template('dodaj.html')


@todo.route('/usun/<string:nr>', methods=["GET", "POST"])
def usun(nr):
    baza = sqlite3.connect('baza.db', check_same_thread=False)
    with baza as connection:
        c = connection.cursor()
        polecenie = "DELETE FROM todo WHERE id={}".format(nr)
        c.execute(polecenie)
    flash("task deleted.")
    zadania = wyswietl_dane()
    return render_template('/main.html', nr=int(nr), zadania=zadania)


if __name__ == "__main__":
    todo.debug = True
    todo.run()
