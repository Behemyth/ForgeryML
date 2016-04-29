# ForgeryML

Project for Introduction to Artificial Intelligence, RPI Spring 2016

#What It Does

Given input files that are known to be attributed to a specific person, this program then presents a yes or no answer to the question of an unknown document being attributed to the same person.

#How To Use

#Dependencies:
  pybrain (and in turn, scipy)
  installation:
    start by installing Python setuptools: https://pypi.python.org/pypi/setuptools
    now, we're gonna need to install scipy, to do so:
      >easy_install scipy
      if this gives you an error, go ahead and fix it depending on the ERROR
      if you are on unix and it says something about permission denied, use:
      >sudo easy_install scipy
      if it says something about missing lapack/blas resources, install them. For example,
      on linux you would type:
      > sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran
      into the terminal, then try to easy_install scipy again

      This will take like 30 minutes to finish
    Once scipy is installed
      > sudo easy_install pybrain

    And you should be done


  **NOTE**: 
    1) instructions may vary for windows/mac slightly, but should be fairly simple.
    2) make sure you are located one level up from the directory containing the 
	files before calling easy_install


N/A at the moment
<test>
