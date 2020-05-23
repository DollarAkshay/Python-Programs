import os

os.system("python -m pip install --upgrade pip")

package_list = [
    'wheel',

    'beautifulsoup4',
    'gym',
    'ipywidgets',
    'jupyter',

    'matplotlib',
    'numpy',
    'opencv-python',
    'pandas',
    'pygame',

    'requests',
    'scikit-learn',
    'seaborn',
    'tensorflow',
    # 'tensorflow-gpu==1.15',
    'xgboost',
]

for package in package_list:
    os.system("python -m pip install -U {}".format(package))
