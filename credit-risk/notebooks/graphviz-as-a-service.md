# GraphViz as a service

It looks to be non-trivial to have graphviz working across various OS (Windows, MacOS, Linux).

We need graphviz to visualize the decision tree.

We will use graphviz-as-a-service ([link](https://github.com/ryanbrainard/gvaas)) to visualize the tree.

Once the dot files are generated in the notebook, goto the terminal and run the following commands

```
$ curl http://gvaas.herokuapp.com/dot -H 'Content-Type: text/vnd.graphviz' -H 'Accept: image/svg+xml' --data-binary @tree.dot > tree.html

$ open tree.html

```

Replace `tree.dot` with the appropriate dot file created in the notebook.

The above commands will convert the dot file to svg, and will open it in a browser.
