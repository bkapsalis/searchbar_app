# searchbar_app
This app.py and toHtml.py were created to insert excel table data into the table body(tbody) of an index.html file. Code can be modified to insert csv file data into the table body of the index.html.

This uses flask. This is a development solution. To use:

* If not done already, clone repository to your desk top.
* Delete previous data.xlsx. Add new data.xlsx to this directory.
* From the bash/terminal navigate to this directory.
* Run 'python app.py', the flask server should start. It should
say '* Running on http://127.0.0.1:5000/', the server is running. 
* Copy and paste http://127.0.0.1:5000/ to a chrome browser.
* The code should insert the new data into the table(tbody) in the index.html and the table should appear.  The search box should still be functional.  


* Libares flask, re and pandas may need to be pip installed. * 
