# from flask import Flask, request

# import json


# app= Flask(__name__)


# @app.get("/")

# def handle_home():
#     return " this is home route"


# @app.get("/students/<student_name>")

# def handle_students(student_name):
#     return {
#         "name":student_name,
#         "usn": "007"
#     }


# @app.get("/students/<student_name>/fav_food")

# def handle_food(student_name):
#     return ["paneer", "momo"]



# if __name__ =="__main__":
#     app.run(debug= True)

# from flask import Flask, request
# import requests
# import json

# app= Flask(__name__)

# @app.get("/")

# def get_home():

#     return " home page"


# URL = "https://dummyjson.com/products"

# response = requests.get(URL)
# data= response.json()

# @app.get("/products/<product_name>")

# def  get_products(product_name):
#  prod=[]
#  for i in data["products"]:
#     if i["category"]== product_name:
#        prod.append(i)


 


#  return prod   

# if __name__== "__main__":

#  app.run(debug= True)


# filter on basis of price 
# ?price/<category_type>/<min_price>/<max_price>
# furniture/10/200


# from flask import Flask, request
# import requests
# import json

# app= Flask(__name__)

# @app.get("/")

# def get_home():

#     return " home page"


# URL = "https://dummyjson.com/products"

# response = requests.get(URL)
# data= response.json()


# @app.get("/price/<category_type>/<min_price>/<max_price>")

# def get_prices(category_type,min_price,max_price):
#    prod=[]
#    category_type = category_type.lower()

#    for i in data["products"]:
#       if (i["category"]== category_type and
#           float(min_price) <= i.get("price", 0) <= float(max_price)):
#           prod.append(i)


#    return prod
# if __name__== "__main__":

#  app.run(debug= True)
       

# filter on the basis of avg review 
# /furniture/3
# all products wgere rating above or euqal to 3

from flask import Flask, request
import requests

app = Flask(__name__)


# Home route
@app.get("/")
def get_home():
    return "Welcome to Product Rating API"


# Test route
@app.get("/test")
def test():
    return {
        "status": "success",
        "message": "API is working!"
    }


# Product API
URL = "https://dummyjson.com/products"


@app.get("/<category_type>/<n>")
def get_ratings(category_type, n):

    response = requests.get(URL)
    data = response.json()

    prod = []

    for i in data["products"]:
        if (
            i["category"] == category_type
            and float(i.get("rating", 0)) >= float(n)
        ):
            prod.append(i)

    return prod


if __name__ == "__main__":
    app.run(debug=True)