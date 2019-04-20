DataScience Project
==============================

A project based on some estimations of the populations of different countries (Kuwait, USA, etc..).

The following datasets have been used:

1st dataset --> Population and other demographic estimatations and projections from 1960 to 2050. Link: https://datasource.kapsarc.org/explore/dataset/population-estimates-and-projections-1960-2050/information/?disjunctive.country&disjunctive.series

2nd dataset --> Bahrain Population Projections for 2018-2032. Link: https://datasource.kapsarc.org/explore/dataset/population-projections/information/

3rd dataset --> Kuwait Population estimation. Link: https://datasource.kapsarc.org/explore/dataset/kuwait-population-estimates/information/?disjunctive.age_group_name&disjunctive.date&disjunctive.frequency&disjunctive.nationality_name&disjunctive.sex_name

4th dataset --> US Regional Annual Population estimates. Link: https://datasource.kapsarc.org/explore/dataset/u-s-regional-annual-population-estimates/information/?disjunctive.date&disjunctive.frequency&disjunctive.region_name&disjunctive.variable_name

5h dataset --> World urbanization prospects from 1950 to 2018. Link: https://datasource.kapsarc.org/explore/dataset/world-urbanization-prospects-the-2018-revision-population/information/?disjunctive.country_name&disjunctive.date&disjunctive.frequency&disjunctive.variable_name&disjunctive.variable_unit

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
