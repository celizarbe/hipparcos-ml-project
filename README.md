# Classification of stars from the Hipparcos Catalogue
Course: Data Science (29780) - Coderhouse

## Preface
This project is for **educational purposes _only_**.

This project's objectives are:
* To apply and asses the performance of different classification algorithms using data from stars in the Hipparcos Catalogue.
* To find the best-performing algorithm and optimize its hyperparameters.

Importantly, for simplicity's sake, this project **will not** explore astronomical, astrometrical, photometrical or otherwise related concepts **in any depth**, except _succintly_ when necessary to justify feature selection decisions.

## Introduction
This project utilizes data from the Hipparcos Catalogue, published by the the European Space Agency (ESA) in 1997.

The Hipparcos astrometry mission had the primary objective of determining accurate astrometric data - positions, annual proper motions and absolute trigonometric parallaxes - with the Hipparcos satellite, which was launched on 8 August 1989 and operated between November 1989 and March 1993. The mission produced two major astrometric catalogues, the Hipparcos Catalogue (of 118 218 stars) and the Tycho Catalogue (of more than one million stars), as a result.

Further information on both Catalogues can be found in ESA's [dedicated page](https://www.cosmos.esa.int/web/hipparcos/catalogues).

The data has been obtained from [this](https://www.kaggle.com/datasets/konivat/hipparcos-star-catalog) Kaggle dataset.

The data fields are described in [The Hipparcos and Tycho Catalogues Vol  1](https://www.cosmos.esa.int/documents/532822/552851/vol1_all.pdf/99adf6e3-6893-4824-8fc2-8d3c9cbba2b5) § 2.1 (p. 105 - 137).

## Project organization
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
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
