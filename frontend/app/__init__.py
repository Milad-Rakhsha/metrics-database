from flask import Flask


app = Flask(__name__)
app.config.from_object('config')



from app import views

#if __name__ == '__main__':
   # manager.run()