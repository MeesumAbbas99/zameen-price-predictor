In this project, We firstly scrapped data from zameen.com using beautifulSoup (scrapper.ipynb)
Then we did preprocessing of that scrapped data and trained a ML model on 4 features of it(model.ipynb)
we pickel the model file using pickle library in python.
Then we made a API on that model using flask(main.py) and using fastapi(main2.py)
then we tested that api through thunder client, you can either use Postman or anyother api testing software.
In db.py file we are storing the data into mongodb database using pymongo


to get response of model you have to start the flask server, even if you are trying to hit an api through html page