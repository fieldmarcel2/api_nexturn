from flask import Flask, request,jsonify
import requests
import json

app= Flask(__name__)

menu = [
    {"name": "Margherita Pizza", "price": 299},
    {"name": "Chicken Biryani", "price": 249},
    {"name": "Paneer Butter Masala", "price": 199},
    {"name": "Veg Burger", "price": 129},
    {"name": "Masala Dosa", "price": 99},
    {"name": "Cold Coffee", "price": 79}
]



orders=[]


@app.get("/menu")

def get_items():

    return jsonify(menu)


@app.get("/menu/<name>")
def singleitems(name):

    for i in menu:
        if i["name"].lower() == name.lower():
            return jsonify(i)

    return jsonify({"error": "Item not found"}), 404


@app.post("/orders")

def orderitem():
    data= request.get_json()


    for i in data:
     i["status"]= "ongoing"

     orders.append(i)
    return jsonify(data), 201


@app.get("/orders/ongoing")

def getongoing():

    res=[]

    for i in orders:
        if i["status"]== "ongoing":
          res.append(i)  
    return jsonify(res)



@app.patch("/orders/<orderId>/complete")

def complete_order(orderId):

    for order in orders:

        if order["orderId"] == orderId:

            if order["status"] == "completed":
                return jsonify({
                "error": "Order already completed"
                }), 409

            order["status"] = "completed"

            return jsonify(order)


    return jsonify({
        "error": "Order not found"
    }), 404


if __name__== "__main__":

    app.run(debug= True)