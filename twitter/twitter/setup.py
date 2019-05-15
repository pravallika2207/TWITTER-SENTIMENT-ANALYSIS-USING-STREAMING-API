from setuptools import setup,find_packages

setup(name='twitter',
      version='0.1',
      description='Twitter Sentiment Analysis Using Streaming APi',
      url='https://github.com/Mrudula09/twitter',
      author='Mrudula Nudurupati',
      author_email='mrudula.nudurupati1997@gmail.com',
      packages=find_packages(),
      install_requires=[
        'emoji==0.5.1',
        'nltk==3.4',
        'matplotlib==2.1.2',
        'tweepy==3.7.0',
        'pandas==0.22.0',
        'numpy==1.14.0',
        'wordcloud==1.5.0',
      ],
      zip_safe=True)
