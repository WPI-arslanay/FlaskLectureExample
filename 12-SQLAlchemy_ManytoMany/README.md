

-----------------------
## Notes
-----------------------
 Add the `TeachingAssistant` model and create a *many-to-many* relationship from `Course` to `TeachingAssistant` using `assigned` association table. 

-----------------------
## Running the application
-----------------------

To run this example:
- Start the application with the following command:

    *  If the application environment is already configured:
        
        ```flask run```
    
    * otherwise 
        
        ```python app.py```
        
        OR
        
        Windows: ```set FLASK_DEBUG=1 && python -m flask run```
        Mac/Linux:  ```export FLASK_DEBUG=1 && python -m flask run```