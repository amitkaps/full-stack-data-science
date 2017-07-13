# **Firefly**

## Deploying functions made easy!

---

# **The problem**

How to expose a function as an API for others to use?

---

# **Why?**

* To use it in a different environment
* Loose coupling

---

# **Use cases**

* Deploy a machine learning model
* preprocess an image
* live price check

---

# **Challenges**

* Requires writing a web application
* What about authentication?
* How to do data validation?
* How I need write a client library too?

---

# **Welcome to Firefly**

Deploying functions made easy!

---

# **Code**

Write your function:

	# sq.py
	def square(n):
		return n*n

---

# **Run**

Start web service:

	$ firefly sq.square
	[INFO] Starting gunicorn 19.7.1
	[INFO] Listening at: http://127.0.0.1:8000
	...

---

# **Use**

And use it with a client.

	>>> from firefly.client import Client
	>>> client = Client("http://127.0.0.1:8000")
	>>> client.square(n=4)
	16

--- 

B**ehind the scenes, it is a RESTful API.**

	$ curl -d '{"n": 4}' http://127.0.0.1:8000/square
	16

And supports any JSON-friendly datatype.	

---

# **More practical example**

Deploying a machine learning model.

	# model.py

	import pickle
	model = pickle.load('model.pkl')

	def predict(features):
    	result = model.predict(features])
    	return int(result[0])

---

Ru**n the server using:**

	$ firefly model.predict
	...

And use it in the client:

	>>> remote_model = Client("http://localhost:8080/")
	>>> remote_model.predict(features=[5.9, 3, 5.1, 1.8]))
	2

---

# **Authentication**

Firefly has built-in support for autentication.

	$ firefly --token abcd1234 sq.square
	...

The client must pass the same token to autenticate it.

	>>> client = Client("http://127.0.0.1:8000", auth_token="abcd1234")
	>>> client.square(n=4)
	16

---

# **Upcoming Features...**

- supporting other input and output content-types in addition to json. (for example, a function to resize an image)
- validation using type annotations
- caching support

---

# **It's open source!**

<https://github.com/rorodata/firefly>

To install:

	pip install firefly-python

---

# **Resources**

* <https://firefly-python.readthedocs.io/>
* <https://github.com/rorodata/firefly>

