# from flask import Flask
# import json

# with open("./sample.json") as file:
#     data= json.load(file)

# app= Flask(__name__)

# # @app.route("/",methods=["GET","POST"]) # for multiple methods
# # def handle_home():
# #     return " hey shivnsu"


# # @app.route("/heyy")

# # def handle_hi():
# #     return " heyy there"


# @app.route("/")

# def getkitchen():

#  categories=[]

#  for i in data:
#   if i['product_category'] == "Kitchen":
#      categories.append(i['product'])
#     #categories[i["product"]] = i["product_category"]



# #  search_keyword = request.args['search_keyword']
#  return categories



# if __name__== "__main__":
#     app.run(debug = True)


#     #tere are 2 types of arameters 
#     #search params /query params -> valid for alll type of routes - eg -> hsdfhsd/search_keyword=....blah blah
#     # 2-> body params/data params-> valid for all except GET request

#create a flask API with 4 endpoints

# add items
# remove item
# returns all the data
# 4th endpoint returns n items from top from the databse.json

from flask import Flask, request

app= Flask(__name__)

import json

with open ("./database.json") as file:
    data= json.load(file)



datalist=data

@app.route("/add-data",methods=["POST"])




def addData():

   item= request.json 
   datalist.append(item)
   return datalist



@app.route("/get-data", methods=["GET"])
def getData():
 return datalist


@app.route("/remove-data", methods=["DELETE"])
def removeData():


 item= request.json
 datalist.remove(item)

 return datalist

@app.route("/get-ndata", methods=["GET"])
def getnData():

 n=2
 res=[]
 for i in range(0,n,1):
   
    res.append(datalist[i])

 return res
# #  @app.route("/get-top/<int:n>", methods=["GET"])
# # def getTop(n):

# #     return datalist[:n]

#  return datalist



if __name__== "__main__":

  app.run(debug= True)



   
   