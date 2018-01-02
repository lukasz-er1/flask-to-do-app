from flask import render_template, flash, request
import sqlite3

baza = sqlite3.connect('baza.db', check_same_thread=False)


def wyswietl_dane():
	tablica = []
	with baza as connection:
		c = connection.cursor()
		c.execute("""SELECT * FROM todo ORDER BY date""")
		rows = c.fetchall()
		for value in rows:
			tablica.append({
				'id': value[0],
				'title': value[1],
				'desc': value[2],
				'date': value[3]
			})
		return tablica


def pobierz_dane():
	error = None
	try:
		if request.method == "POST":
			tytul = request.form['title']
			opis = request.form['desc']
			data = request.form['date']
			with baza as connection:
				c = connection.cursor()
			if tytul == "":
				flash("Please add title.")
			else:
				c.execute('INSERT INTO todo(title, desc, date) VALUES(?, ?, ?)', (tytul, opis, data))

			return render_template('dodaj.html')

		else:
			return render_template('main.html')

	except Exception as e:
		flash(e)
		return render_template('dodaj.html', error=error)
