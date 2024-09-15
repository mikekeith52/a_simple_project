# A simple Project
This is an example repository to show how to manage a simple project.

## Description
This project helps you learn how a real data analytics project may be organized following good practices. A project like this helps you get results out fast and modify key parameters with minimal chance of introducing human error. It works by reading a query, pivoting the query results, and outputting the end result into an Excel file. A project like this may be considered an "ETL (Extract Transform Load)" project.

## Delivered To
Here is where I would describe the intended audience of my analysis. Who needs these results and why?

## Installation Instructions
You need to have Python installed, as well as the third-party libraries listed in the [`requirements.txt`](requirements.txt) file. You can automatically install those librarires by running `pip install -r requirements.txt` from command line.

## Refresh Instructions
1. Download the code locally to your computer.
2. Open `config.py` and change the `dates` paramter. The first element in this tuple is the start date and the second is the end date.
3. Run `python main.py` on the command line. Or import it into a Jupyter notebook (`import main`) and run it from there (`main.main()`)

## Maintenance
Here is where I would describe what future updates may cause this project to break, how to fix it if it breaks (what probably went wrong), and what future enhancements could make the project even better.

## Caveats
Unfortunately, this project is just an example and can never be run successfully because the line of code that imports the `conn` object is just an example. The query is also just an example.