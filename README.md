# Full Stack Data Science
---

> _"Jack of all trades, master of none, though oft times better than master of one."_

One of the common pain points that we have come across in big organizations is the last-mile delivery of data science applications. 

> You code, you test, you ship and you maintain

One common delivery vehicle is to create dashboards(BI). But the one, that's very useful and neglected more often than not, is to create APIs and provide seamless integration with other applications within the company. This requires you to have a basic understanding of machine learning, server-side programming and front-end application.

In this workshop, you would learn how to build a seamless end-to-end data driven application - Data Exploration, Machine Learning Model, RESTful API and Web Application - to solve a business prediction problem.

## Course Content  
1. Introduction to Data Science Process 
2. Introduction to Data Exploration
3. Introduction to Machine Learning
4. Overview of the case we will be solving in the workshop
5. A simple ML Model
6. Creating RESTful API
7. Persisting model output
8. Updating the model as more data comes in (batch only - no streaming)
9. A simple webpage front-end to visualise the results and interact with the API.
10. Creating a simple application that accomplishes this end-to-end

An advanced version of the workshop, taught over two days, will cover the following additional topics

1. Building data pipeline and models  
2. Deployment on cloud  
3. Automate the workflow (eg: using `airflow`) 


## Target Audience
- **A programmer but not a data science practioner**: A programmer with experience in server-side or front-end development and maybe has some familiarity with doing data analysis. You could be looking to transition in to building data driven products or a create a richer product experience with data.
- **A data science practioner but not a programmer**: A data science with some experience in doing data analysis, preferably in a scripting language (R/Python/Scala), but wants to get a deeper and a more applied perspective on creating data driven products.


##  Pre-requisites
- Programming knowledge is mandatory. Attendee should be able to write conditional statements, use loops, be comfortable writing functions and be able to understand code snippets and come up with programming logic.
- Participants should have a basic familiarity of Python. Specifically, we expect participants to know the first four sections from this: [http://anandology.com/python-practice-book/](http://anandology.com/python-practice-book/)
- Participants should also have some experience with using Python for Data Science. Specifically, participants should be able to work with the following python libraries
  - `jupyter`: For doing literate programming in notebooks
  - `numpy`: For scientific computation
  - `pandas`: For data wrangling and transformation of tabular data (dataframes)
  - `scikit-learn`: For building machine learning models

## Software Requirements

We will be using Python data stack for the workshop. Please install [Ananconda for Python 3.5 or 3.6][anaconda] for the workshop. Additional requirement will be communicated to participants.

Install the required packages using conda.

```
conda install numpy pandas matplotlib seaborn scikit-learn pydotplus flask flask-wtf
conda install -c ioam holoviews bokeh
```  

We'll also need a python library firefly-python that is not available as conda package. Install it using pip.

```
pip install firefly-python rorolite
```

[anaconda]: https://www.continuum.io/downloads

## Facilitators’ Profile

Anand Chitipothu has been crafting beautiful software since a decade and half. He's now building a data science platform, [rorodata](http://rorodata.com/), which he recently co-founded. He regularly conducts advanced programming courses through Pipal Academy. He is co-author of *web.py*, a micro web framework in Python. He has worked at Strand Life Sciences and Internet Archive. You can tweet him at [@anandology](https://twitter.com/anandology).

Amit Kapoor teaches the craft of telling visual stories with data. He conducts workshops and trainings on Data Science in Python and R, as well as on Data Visualisation topics. His background is in strategy consulting having worked with AT Kearney in India, then with Booz & Company in Europe and more recently for startups in Bangalore. He did his B.Tech in Mechanical Engineering from IIT, Delhi and PGDM (MBA) from IIM, Ahmedabad. You can find more about him at http://amitkaps.com/ and tweet him at [@amitkaps](https://twitter.com/amitkaps).

Bargava Subramanian is a practicing Data Scientist. He has 14 years of experience delivering business analytics solutions to Investment Banks, Entertainment Studios and High-Tech companies. He has given talks and conducted workshops on Data Science, Machine Learning, Deep Learning and Optimization in Python and R. He has a Masters in Statistics from University of Maryland, College Park, USA. He is an ardent NBA fan. You can tweet to him at [@bargava](https://twitter.com/bargava).
