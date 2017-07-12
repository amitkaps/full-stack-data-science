theme: Olive Green, 8
autoscale: true

# [fit] **Machine Learning as a Service**


<br>
*Amit Kapoor*
[amitkaps.com](http://amitkaps.com)

<br>
*Anand Chitpothu*
[anandology.com](http://anandology.com)

---

# **Getting Started**
- Download the Repo: [https://github.com/amitkaps/full-stack-data-science](https://github.com/amitkaps/full-stack-data-science)
- Finish installation
- Run `jupyter notebook` in the console

---

# **Motivation**

- Solve a business problem.
- Understand the end-to-end process
- Build a Machine Learning application

---

> "Jack of all trades, master of none, though oft times better than master of one."

---

# **Approach**

- Simple approach
- Go wide vs. go deep
- Practical and scalable 

---


# **Schedule**

1. **Introduction, Setup** (10 mins)
2. **ML Process, Frame** - *Conceptual* (20 mins)
3. **Acquire, Refine, Explore** - *Coding* (30 mins)
4. **Transform, Model** - *Coding* (40 mins)
 -- Break (15 mins)--
5. **Building an ML Application** - *Conceptual* (10 mins)
6. **Deploy the ML Model as Service** - *Coding* (20 mins)
7. **Wiring the Model** - *Coding* (20 mins)
8. **Wrap-up** (15 mins)

---

# **Data-Driven Lens**

> "Data is a clue to the End Truth"
-- Josh Smith

---

# **Metaphor**

- A start-up providing loans to the consumer 
- Running for the last few years
- Now planning to adopt a data-driven lens 

What are the **type of questions** you can ask?

---

# **Type of Questions**
- What is the trend of loan defaults?
- Do older customers have more loan defaults?
- Which customer is likely to have a loan default?
- Why do customers default on their loan?

---

# **Type of Questions**
- Descriptive
- Inquisitive
- Predictive
- Causal

---

# **Data-driven Analytics**
- **Descriptive**: Understand Pattern, Trends, Outlier
- **Inquisitive**: Conduct Hypothesis Testing
- **Predictive**: Make a prediction
- **Causal**: Establish a causal link

---

# **Prediction Challenge**

> It’s tough to make predictions, especially about the future.
-- Yogi Berra

---

# **How to make a Prediction?**
- **Human Learning**: Make a *Judgement*
- **Machine Programmed**: Create explicit *Rules* 
- **Machine Learning**: Learn from *Data*

---

# **Machine Learning (ML)**

> [Machine learning is the] field of study that gives computers the ability to learn without being explicitly programmed.
-- *Arthur Samuel*

<br>

> Machine learning is the study of computer algorithm that improve automatically through experience
-- *Tom Mitchell*

---

# **Machine Learning: Essense**

- A pattern exists
- It cannot be pinned down mathematically
- Have data on it to learn from

> "Use a set of observations (data) to uncover an underlying process"

---

# **Machine Learning Approach**
```
FRAME  ——← ACQUIRE  ——← REFINE ——←  
                                  \
                                TRANSFORM →——
                                    ↑          ↘  
                                    |        EXPLORE
                                    ↓          ↗
                                  MODEL   →——
                                  /      
INTERACT →——  BUILD →—— DEPLOY →—— 

```


--- 

# **ML Theory: Data Types**

- What are the types of data on which we are learning?
- Can you give example of say measuring temperature?

---

# **Data Types e.g. Temperature**

- **Categorical** 
    - *Nominal*: Burned, Not Burned
    - *Ordinal*: Hot, Warm, Cold
- **Continuous**
    - *Interval*: 30 °C, 40 °C, 80 °C 
    - *Ratio*: 30 K, 40 K, 50 K 

---

# **Data Types - Operations**

- **Categorical** 
  - *Nominal*: = , !=
  - *Ordinal*: =, !=, >, <
- **Continuous**
  - *Interval*: =, !=, >, <, -, % of diff 
  - *Ratio*: =, !=, >, <, -, +, %

---

# **Case: Loan Default Prediction**

*Application Attributes*
- **age**: age of the applicant
- **income**: annual income of the applicant
- **year**: no. of years of employment
- **ownership**: type of house owned
- **amount** : amount of loan requested by the applicant

*Behavioural Attributes*:
- **grade**: credit grade of the applicant

*Question* - whether the applicant will **default** or not?

---

# **Historical Data**

```
 age   income   years  ownership 	 grade   amount
 ---   -------  -----  ---------  ------- -------
 31	    12252    25.0      RENT      C      2400
 24	    49200    13.0      RENT      C     10000
 28	    75000    11.0       OWN      B     12000
 27    110000    13.0  MORTGAGE      A      3600
 33	    24000    10.0      RENT      B      5000

```

---

# **Data Types**

- **Categorical**
    - *Nominal*: home owner [rent, own, mortgage] 
    - *Ordinal*: credit grade [A > B > C > D > E]
- **Continuous**
    - *Interval*: approval date  [20/04/16, 19/11/15]
    - *Ratio*: loan amount [3000, 10000]

---

# **ML Terminology**

**Features**: $$\mathbf{x}$$
   - `age`, `income`, `years`, `ownership`, `grade`, `amount`


**Target**: $$y$$ 
    - `default`

**Training Data**: $$ (\mathbf{x}_{1}, y_{1}), (\mathbf{x}_{2}, y_{2}) ... (\mathbf{x}_{n}, y_{n}) $$
    - historical records

---

# **ML Paradigm: Supervised**

Given a set of **feature** $$\mathbf{x}$$, to predict the value of **target** $$y$$ 

Learning Paradigm: **Supervised**

- If $$y$$ is *continuous* - **Regression**
- If $$y$$ is *categorical* - **Classification**

---

# **ML Theory: Formulation**
- **Features** $$\mathbf{x}$$ *(customer application)*
- **Target** $$y$$ *(loan amount)*
- **Target Function** $$\mathcal{f}: \mathcal{X} \to \mathcal{y}$$ (ideal formula)
- **Data** $$ (\mathbf{x}_{1}, y_{1}), (\mathbf{x}_{2}, y_{2}) ... (\mathbf{x}_{n}, y_{n}) $$ *(historical records)*
- **Final Hypothesis** $$\mathcal{g}: \mathcal{X} \to \mathcal{y}$$ (formula to use)
- **Hypothesis Set** $$ \mathcal{H} $$ (all possible formulas)
- **Learning Algorithm** $$\mathcal{A}$$ (how to learn the formula)


---

# **ML Theory: Formulation**

$$\text{unknown target function}$$
$$\mathcal{f}: \mathcal{X} \to \mathcal{y}$$     
$$ | $$
$$\text{training data}$$
$$ (\mathbf{x}_{1}, y_{1}), (\mathbf{x}_{2}, y_{2}) ... (\mathbf{x}_{n}, y_{n}) $$    
$$ | $$
$$\text{hypothesis set} \quad \rightarrow \quad \text{learning algorithm} \qquad \qquad \qquad \qquad $$
$$ \mathcal{H} \qquad  \qquad \qquad \qquad \qquad \mathcal{A} \qquad \qquad \qquad \qquad \qquad $$
$$ | $$
$$\text{final hypothesis}$$
$$\mathcal{g} \to \mathcal{f}$$

---

# **ML Theory:  Learning Model**

The Learning Model is composed of the two elements

- The Hypothesis Set:  $$ \mathcal{H} = \{\mathcal{h}\} \qquad \mathcal{g} \in \mathcal{H} $$
- Learning Algorithm: $$ \mathcal{A} $$ 

---

# **ML Theory: Formulation (Simplified)**

$$\text{unknown target function}$$
$$ y = \mathcal{f}(\mathbf{x})$$     
$$ | $$
$$\text{training data}$$
$$ (\mathbf{x}_{1}, y_{1}), (\mathbf{x}_{2}, y_{2}) ... (\mathbf{x}_{n}, y_{n}) $$    
$$ | $$
$$\text{hypothesis set} \quad \rightarrow \quad \text{learning algorithm} \qquad \qquad \qquad \qquad $$
$$ \{ \mathcal{h}(\mathbf{x})\}  \qquad \qquad \qquad \qquad \mathcal{A} \qquad \qquad \qquad \qquad \qquad $$
$$ | $$
$$\text{final hypothesis}$$
$$\mathcal{g}(\mathbf{x}) \to \mathcal{f}(\mathbf{x})$$

---


# **Machine Learning Process**

- *Frame*: Problem definition
- *Acquire*: Data ingestion 
- *Refine*: Data wrangling
- *Transform*: Feature creation 
- *Explore*: Feature selection 
- *Model*: Model creation & assessment
- *Insight*: Solution Insight
- *Communicate*: Dashboard or Story

---

# **Frame**

**Variables**
   - `age`, `income`, `years`, `ownership`, `grade`, `amount`, `default` and `interest`

- What are the **Features**: $$\mathbf{x}$$ ?
- What are the **Target**: $$y$$ 

---

# **Frame**

**Features**: $$\mathbf{x}$$
   - `age` 
   - `income` 
   - `years` 
   - `ownership` 
   - `grade`
   - `amount` 

**Target**: $$y$$ 
    - `default`


---

# **Acquire**

- Simple! Just read the data from `csv` file

---

# **Refine - Missing Value**

- **REMOVE** - NAN rows
- **IMPUTATION** - Replace them with something? 
    - Mean 
    - Median
    - Fixed Number - Domain Relevant
    - High Number (999) - Issue with modelling
- **BINNING** - Categorical variable and "Missing becomes a category*
- **DOMAIN SPECIFIC** - Entry error, pipeline, etc.

---

# **Refine - Outlier Treatment**

- What is an outlier?
- Descriptive Plots
    - Histogram
    - Box-Plot 
- Measuring 
    - Z-score
    - Modified Z-score > 3.5
    where modified Z-score = 0.6745 * (x - x_median) / MAD 

---

# **Explore**

- Single Variable Exploration
- Dual Variable Exploration
- Multi Variable Exploration 

---

# **Transform**

Encodings
- One Hot Encoding 
- Label Encoding

Feature Transformation
- Log Transform
- Sqrt Transform

---

# **Model - Linear Regression**

**Parameters**
- fit_intercept
- normalization

**Error Measure**
- mean squared error

---


# **Real-World Challenge - Noise**

- The "target function" $$f$$ is not always a *function*
- Not unique target value for same input
- Need to add noise $$N(0,\sigma)$$

$$ y = f(\mathbf{x}) + \epsilon(\mathbf{x}) $$

---

# **Noise Implication**

The best model we can create will have an expected error of $$\sigma^2$$

If Noise ($$\sigma$$) is large, that means feature set does not capture large enough factors in the underlying process
    - Need to create **better features**
    - Need to find **new features**

---

# **When are we learning?**

Learning is defined as $$g≈f$$, which happens when

(1) Can we make $$E_{out}(g)$$ is close enough to $$E_{in}(g)$$?

$$E_{out}(g)≈E_{in}(g)$$

(1) Can we make $$E_{in}(g)$$ small enough?

$$E_{in}(g)≈0$$

---

# **ML Theory: Generalisation**

![right 100%](img/generalisation_error.png)

For Learning, $$E_{out}(g)≈E_{in}(g)$$

To find the generalisation error, we need to split our data into training and test samples

Given large $$N$$, the expected generalisation error should be zero

---

# **ML Theory: Generalisation**

For Learning, $$E_{in}(g)≈0$$

**Complex Model**: Better chance of approximating $$f$$
**Simple Model**: Better chance of generalising $$E_{out}$$

Lets try by increasing the model complexity - More features through interaction effect

---

# **ML Theory: Model Complexity**

![90% original inline](img/simple_complex.png)

---

![right 100%](img/bias_variance.png)
# **ML Theory: Bias-Variance**

For Learning, $$E_{in}(g)≈0$$

Given large $$N$$, the expected error should be the bias

- **Bias** are the simplifying assumptions made by a model to make the target function easier to learn.
- **Variance** is the amount that the estimate of the target function will change if different training data was used.

---

# **ML Theory: Bias-Variance Tradeoff**

![inline](img/model_complexity.png)

---

![right 100%](img/overfitting.png)

# **ML Theory: Overfitting**

- Simple Target Function
- 5th data point - noisy
- 4th order polynomial fit

$$E_{in}=0$$, $$E_{out}$$ is large

*Overfitting* - Fitting the data more than warranted, and hence **fitting the noise**

---

# **ML Theory: Addressing Overfitting**

$$E_{out}(h) = E_{in}(h) + \text{overfit penalty}$$

- **Regularization**: Not letting the weights grow
    - Ridge: add $$||w||^2$$ to error minimisation
    - Lasso: add $$||w||$$ to error minimisation
- **Validation**: Checking when we reach bottom point

---

# **Regularization - Ridge**

$$ Minimize \quad E_{in}(w) + \frac{\lambda}{N}||w||^2 $$

![inline](img/regularization.png)

---

![right 100%](img/validation.png)

# **Validation** 

Validation set: $$K$$
Training set: $$N-K$$

Rule of Thumb: $$N = \frac{K}{5}$$

Note: The validation set is used for learning

---

# **Cross Validation**

Repeats the process 5-times

![fit inline](img/cross_validation.png)

---

![right 100%](img/model_selection.png)

# **Model Selection**

How to choose between competing model? 

Choose the function $$g_{m}$$ with 
lowest cross-validation error $$E_{m}$$

--- 

# **Applied ML**
- **Theory**: Formulation, Generalisation, Bias-Variance, Overfitting
- **Paradigms**: Supervised - Regression
- **Models**: Linear - OLS, Ridge, Lasso
- **Methods**: Regularisation, Validation
- **Process**: Frame, Acquire, Refine, Transform, Explore, Model 


---

## **Classification Problem**

*Context*: Loan Default

*Customer Application*
- **age**: age of the applicant
- **income**: annual income of the applicant
- **year**: no. of years of employment
- **ownership**: type of house owned
- **grade**: credit grade for the applicant
- **amount**: loan amount given
- **interest**: interest rate of loan

*Question* - Who is likely to  **default**?

---

# **Linear Models**

$$ s = \sum_{i=1}^d w_{i} x_{i} $$


![inline original](img/linear_models.png)

---

# **Logit Function**

### $$ \theta (s)={\frac {e^{s}}{e^{s}+1}}={\frac {1}{1+e^{-s}}}$$

![inline](img/logistic-curve.png)

---

# **Logistic Relationship**

Find the $$ w_{i} $$ weights that best fit:
$$ y=1 $$  if $$ \sum_{i=1}^d w_{i} x_{i} > 0$$
$$ y=0$$, otherwise

Follows:

$$ \theta(y_i)={\frac {1}{1+e^{-(\sum_{i=1}^d w_{i} x_{i})}}} $$

---

# **Error - Likelihood / Probabilities**

Where, $$h(\mathbf{x}) =  \sum_{i=1}^d w_{i} x_{i} $$

Minimise the **log-likelihood** values

$$E(\mathbf{h}) = - \frac{1}{N} ln \left( \prod_{i=1}^N \theta (y_i h(\mathbf{x})) \right)$$



---

# **Learning Algorithm - Logistic**

- Logistic Regression algorithm aims to minimise $$ E_{in}(h)$$ 
- **Iterative Method** -> Solves to give $$g(\mathbf{x})$$

$$g(\mathbf{x}) = \hat{y} $$

$$ E_{in}(g) = \frac{1}{N} \sum_{i=1}^N ln( 1 + e^{-y_i \hat{y_i}})$$


---

# **Error Metric - Confusion Matrix**

![inline](img/confusion_matrix2.png)

---

# **Model Evaluation** 

**Classification Metrics**

![fit right](img/precision_recall.png)

Recall (TPR) = TP / (TP + FN)
<br>
Precision = TP / (TP + FP)
<br>
Specificity (TNR) =  TN / (TN + FP)

---

# **Model Evaluation**

**Receiver Operating Characteristic Curve** 

Plot of TPR vs FPR at different discrimination threshold
 
![100% right](img/roc-curves.png)

---

# **Decision Tree**

Example: Survivor on Titanic

![right fit](img/tree_titanic.png)

---

# **Decision Tree**

- Easy to interpret
- Little data preparation
- Scales well with data
- White-box model
- Instability – changing variables, altering sequence
- Overfitting

---

# **Bagging**

- Also called bootstrap aggregation, reduces variance
- Uses decision trees and uses a model averaging approach

---

# **Random Forest**

- Combines bagging idea and random selection of features.
- Similar to decision trees are constructed – but at each split, a random subset of features is used. 

![inline ](img/random_forest.png)

---

> If you torture the data enough, it will confess.
-- Ronald Case

---

# **Challenges**
- Data Snooping
- Selection Bias
- Survivor Bias 
- Omitted Variable Bias
- Black-box model Vs White-Box model
- Adherence to regulations

---


# **Applied ML**
- **Theory**: Formulation, Generalisation, Bias-Variance, Overfitting
- **Paradigms**: Supervised - Regression & Classification
- **Models**: Linear Models, Tree Models
- **Methods**: Regularisation, Validation, Aggregation
- **Process**: Frame, Acquire, Refine, Transform, Explore, Model 


---
