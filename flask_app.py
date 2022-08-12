from app import create_app

app = create_app()
app.config["TEMPLATES_AUTO_RELOAD"] = True # make sure templates are auto reloaded

if __name__ == '__main__':
    app.run(debug=True)