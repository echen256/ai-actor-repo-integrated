The frontend folder houses the chrome extension. Install it as a loose extension and activate it. If it is installed properly, you should see an item in your right click context menu that
that gives you the option of generating a cover letter based on the page content. Note that the cover letter will be copied directly to your clipboard and will take a while.

The backend folder contains the server that forwards your requests to the Open AI API. It requires that you store your API key in a .env file located in the root of the backend folder.

Before you start the server, be sure to add a resume.txt file to backend/files
This file will be used for the prompt generation.

To start up the backend, enter the command 

.\run.bat  

This is only tested on Windows machines.
