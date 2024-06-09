# Spark-Standalone-Cluster-Setup :atom:
To facilitate the initial setup of Apache Spark, this repository provides a beginner-friendly, step-by-step guide on setting up a master node and two worker nodes. 

## Requirements :basecamp:
* `Apache-Spark`
* `Java JDK installation`
* `Java`
* `Pyspark`
* `winutils.exe`
* `Python`

## Instructions :page_with_curl:
* You want to install [Java JDK](https://www.oracle.com/java/technologies/downloads/#jdk22-windows) onto your computer by selecting the x64 installer. This installation will be located in the `C:\Program Files\Java\jdk-22` by default (this will be important in the following steps).<br><br>
* We will then create two folders: :file_folder:hadoop and :file_folder:spark in your `C:\` drive.<br><br>
  * In the :file_folder:spark folder: you need to go and download Apache Spark from this [link](https://spark.apache.org/downloads.html), select the release and package type and download the spark-3.5.1-bin-hadoop3.tgz file. You will then need to drag this into the `C:\spark` path and extract it in there.<br><br>
  * In the :file_folder:hadoop folder: create another folder called `bin`, then go to this [link](https://github.com/cdarlint/winutils) and select the hadoop version that is compatible with the previously selected package type when you were downloading Apache Spark (in my case it's for Hadoop 3.3 and later). Click on the folder that corresponds to your hadoop version and scroll down to find `winutils.exe`. You will download this into your `C:\hadoop\bin` path.<br><br>
* We now have to setup a bunch of system environment variables in order for all of this to work.<br> This can be accessed by going to :file_folder:`File Explorer` and then right-click on :desktop_computer:`This PC` and you will select `Properties`, you will have a :gear:`System About` windows open where you will locate `Advanced system settings` and finally, clicking on `Environment Variables`.<br><br>
  * **HADOOP_HOME**:
    * You will see two environment variables named as `Users` & `System` variables.
    * Make sure you're in the `System` variables section and select `New`.
    * The variable name will be `HADOOP_HOME` and the variable value will `C:\hadoop`.
    * You will then locate an existing system variable called `Path`, which you will click Edit and it will bring you to a new window.
    * From here you just need to click on `New` and put `%JAVA_HOME%\bin` which will link it to your \bin folder.<br><br>
  * **SPARK_HOME**:
    * You will do pretty much the exact same thing previously, variable name is `SPARK_HOME` the variable value for me is `C:\spark\spark-3.5.1-bin-hadoop3`.
    * Locate the system variable `Path`, click on Edit and, create new path and put `%SPARK_HOME%\bin`.<br><br>
  * **JAVA_HOME**:
    * Create new system vriable called `JAVA_HOME` and the variable value becareful it's actually located in your Program Files so for me it's `C:\Program Files\Java\jdk-22`.
    * Locate the system variable `Path`, click on edit and, create new path and put `%JAVA_HOME%\bin`.<br><br>
  * **Additional Python Paths**:
    * I ran into issues when trying to run my python scripts even when I had everything installed properly, I noticed I didn't setup the paths to my python environments properly
    * Please ignore this if the `python` or `python3` command works in your `Terminal`, mine didn't so I had to locate my python installation folder and add it to the `Path` System variable.
    * This involves clicking edit and add new path which for me was `C:\Users\User_Name\AppData\Local\Programs\Python\Python311` (it might be somewhere different for you)
    * ANOTHER System Path Variable I needed to add was my `pip` :hurtrealbad:, if you don't have pip installed please use this [link](https://www.youtube.com/watch?v=ENHnfQ3cBQM) as a resource.
    * In the end you will pretty much have a Path `C:\Users\User_Name\AppData\Local\Programs\Python\Python311\Scripts` in your systems variable that links to your `pip` installation so that you can pip install `pyspark`.<br><br>
  * **PYSPARK_PYTHON**:
    * So spark by default uses the `python3` command when I want to run a python script...this was not the case for me because the correct command that works is `python` for me.
    * I had go to my System variables section and click on New to add a variable name called `PYSPARK_PYTHON` and its corresponding value as `python`.
   
