from flask import Flask
fred = Flask(__name__)
@fred.route("/")
@fred.route("/bob")
@fred.route("/Desktop/Stuff")
def a():
    return __name__ + "I like chicken!"

if __name__ == '__main__':
    fred.run()
