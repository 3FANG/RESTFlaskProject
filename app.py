import connexion


app = connexion.FlaskApp(__name__, specification_dir='./')

app.add_api('swagger.yml')


@app.route('/')
def main_page():
    return "<h1>It's Main page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
