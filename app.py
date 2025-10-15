# app.py

# Step 1: Import necessary modules
from fastapi import FastAPI, Request # Import Request to get client connection info
from fastapi.templating import Jinja2Templates # Import the template renderer

# Step 2: Create the FastAPI application instance
app = FastAPI()

# Step 3: Initialize Jinja2Templates
# This tells FastAPI where to find the HTML template files.
# The path is relative to where you run the application.
templates = Jinja2Templates(directory="templates")

# Step 4: Define an endpoint that serves the template
@app.get("/", summary="Home Page Endpoint", description="Renders the main index page with dynamic content.")
def home(request: Request):
   
    # Context dictionary: ALWAYS include 'request': request
    context = {
        "request": request, 
        "title": "Welcome to FastAPI Templates!",
        "content_message": "This content was passed from the Python backend."
    }
    
    # Render and return the template
    return templates.TemplateResponse("index.html", context)

# Command to run the app (for the blog post's conclusion):
# uvicorn app:app --reload