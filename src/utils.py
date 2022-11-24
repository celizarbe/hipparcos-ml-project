import pandas as pd
import numpy as np

# Check abundance of missing values
# Credit to: Javi (https://github.com/javiabellan)
# https://github.com/javiabellan/machine-learning#exploratory-data-analysis
# =========================================================================

def check_missing(df):
  total = df.isnull().sum().sort_values(ascending = False)
  percent = (df.isnull().sum() / df.isnull().count() * 100).sort_values(ascending = False)
  return pd.concat([total, percent], axis = 1, keys = ['Total missing', 'Percent missing'])

#
#
#

# Check abundance of missing values
# Credit to: Javi (https://github.com/javiabellan)
# https://github.com/javiabellan/machine-learning#exploratory-data-analysis
# =========================================================================

def check_missing(df):
  total = df.isnull().sum().sort_values(ascending = False)
  percent = (df.isnull().sum() / df.isnull().count() * 100).sort_values(ascending = False)
  return pd.concat([total, percent], axis = 1, keys = ['Total missing', 'Percent missing'])


#
#
#

# Get a star's "base" spectral type consisting of
# 1 letter and 1 number following the Morgan-Keenan (MK)
# system to indicate the star's temperature class and sub-type
# ============================================================
def get_base_spectral_type(full_spectral_type):
  base_type = ''
  letters = []
  numbers = []
  for character in full_spectral_type:
    if character.isalpha():
      letters.append(character)
    if character.isnumeric():
      numbers.append(character)
  if len(letters) >= 1:
    base_type = base_type + '{}'.format(letters[0])
  if len(numbers) >= 1:
    base_type = base_type + '{}'.format(numbers[0])
  return base_type