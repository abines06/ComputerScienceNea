from website import create_app
#importing the create_app function from __init__.py file in website 

app = create_app()
#creating an instance of a website 

if __name__ == '__main__': #checks if the code is being run directly from the main.py file
    app.run(debug= True)   #if so it runs the website with debugging on 

