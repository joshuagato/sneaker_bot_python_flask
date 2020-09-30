from app import app


if __name__ == "__main__": 
    app = app.run(debug=True, use_reloader=True, threaded=True)