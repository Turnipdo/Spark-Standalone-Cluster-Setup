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
* We now have to setup a bunch of system environment variables in order for all of this to work.<br> This can be accessed by going to :file_folder:`File Explorer` and then right-click on :desktop_computer:`This PC` and you will select `Properties`, you will have a :gear:`System About` windows open where you will locate `Advanced system settings` and finally, clicking on `Environment Variables`.<br><br> ![Environment variables](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/Environment%20variables.png) <br><br>
  * **HADOOP_HOME**:
    * You will see two environment variables named as `Users` & `System` variables.
    * Make sure you're in the `System` variables section and select `New`.
    * The variable name will be `HADOOP_HOME` and the variable value will `C:\hadoop`.
    * You will then locate an existing system variable called `Path`, which you will click Edit and it will bring you to a new window.
    * From here you just need to click on `New` and put `%JAVA_HOME%\bin` which will link it to your \bin folder.<br><br> ![HADOOP_HOME](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/HADOOP_HOME.png) <br><br>
  * **SPARK_HOME**:
    * You will do pretty much the exact same thing previously, variable name is `SPARK_HOME` the variable value for me is `C:\spark\spark-3.5.1-bin-hadoop3`.
    * Locate the system variable `Path`, click on Edit and, create new path and put `%SPARK_HOME%\bin`.<br><br> ![SPARK_HOME](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/SPARK_HOME.png) <br><br>
  * **JAVA_HOME**:
    * Create new system vriable called `JAVA_HOME` and the variable value becareful it's actually located in your Program Files so for me it's `C:\Program Files\Java\jdk-22`.
    * Locate the system variable `Path`, click on edit and, create new path and put `%JAVA_HOME%\bin`.<br><br> ![JAVA_HOME](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/JAVA_HOME.png) <br><br>
  * **Additional Python Paths**:
    * I ran into issues when trying to run my python scripts even when I had everything installed properly, I noticed I didn't setup the paths to my python environments properly
    * Please ignore this if the `python` or `python3` command works in your `Terminal`, mine didn't so I had to locate my python installation folder and add it to the `Path` System variable.
    * This involves clicking edit and add new path which for me was `C:\Users\User_Name\AppData\Local\Programs\Python\Python311` (it might be somewhere different for you)
    * ANOTHER System Path Variable I needed to add was my `pip` :hurtrealbad:, if you don't have pip installed please use this [link](https://www.youtube.com/watch?v=ENHnfQ3cBQM) as a resource.
    * In the end you will pretty much have a Path `C:\Users\User_Name\AppData\Local\Programs\Python\Python311\Scripts` in your systems variable that links to your `pip` installation so that you can pip install `pyspark`.<br><br> ![ALL_PATHS](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/Path_system_variable_edit.png)<br><br>
  * **PYSPARK_PYTHON**:
    * So spark by default uses the `python3` command when I want to run a python script...this was not the case for me because the correct command that works is `python` for me.
    * I had go to my System variables section and click on New to add a variable name called `PYSPARK_PYTHON` and its corresponding value as `python`.<br><br> ![PYSPARK_PYTHON](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/PYSPARK_PYTHON.png)<br><br>
  * **Verify the host machine firewall settings if they're allowing connections:** :earth_americas::bricks: <br>
    * Go to `Control-Panel`.
    * Click on `System and Security`.
    * Find and Click `Windows Defender Firewall`.
    * Click on `Allow an app or feature through Windows Defender Firewall`.
    * Locate `Java(TM) Platform SE binary` and ensure that both checkboxes Private and Public networks are allowed.<br><br>
  * **Create an inbound rule for the Spark Web UI:** :earth_americas::shield: <br>
    * Go to `Control-Panel`.
    * Click on `System and Security`.
    * Find and Click `Windows Defender Firewall`.
    * Click on `Advanced Settings` :arrow_right: `Inbound Rule` :arrow_right: `New Rule`
    * Choose `Port` and click `Next`
    * Select `TCP` and specify port `4040`
    * Allow the connection and click `Next`
    * Select when this rule applies (I selected all three `Domain`, `Private`, `Public`)
    * Name the rule as Spark Web UI and hit finish.<br><br>
  * Once everything is installed like `python`, `pip`, `pyspark` and everything is configured you can now test the following commands in a terminal window (I've included the .txt files and the outputs from my terminal window):
    * `java -version`
    * `javac -version`
    * `echo %SPARK_HOME%`
    * `echo %JAVA_HOME%`
    * `echo %HADOOP_HOME%`<br><br>
  * You can then use the following command `pyspark` in your terminal window to start a spark session, navigate to http://localhost:4040 to check the Spark Web UI.
 
  ### Setting up the master and worker nodes using command prompts + running the python file:
  * We can now create a master node:
    * First open a command prompt window and `cd %SPARK_HOME%`.
    * Use the following command: `bin\spark-class2.cmd org.apache.spark.deploy.master.Master`
    * This will deploy the master node, you can verify this by navigating to localhost:8080 (this web page is important because you will need to extract the URl of the master)<br><br>
    ![Master](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/Master%20%2B%20Worker%20images/Master%20Node.png)<br><br>
   * Create the first worker node:
     * Open another command prompt window and `cd %SPARK_HOME%`.
     * Use the following command: `bin\spark-class2.cmd org.apache.spark.deploy.worker.Worker -c 1 -m 4G spark://YOUR_IP_ADDRESS:7077`
     * Notice that the `-c 1` indicates I want to assign 1 core to this worker and `-m 4G` which is 4 GB of memory, replace `spark://YOUR_IP_ADDRESS:7077` with the URL you obtained from your spark webpage.
     * You can now navigate to localhost:8081 to view this worker node.<br><br>
     ![First Worker](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/Master%20%2B%20Worker%20images/First%20Worker.png)<br><br>
   * Create the second worker node:
     * Open another command prompt window and `cd %SPARK_HOME%`.
     * Use the following command: `bin\spark-class2.cmd org.apache.spark.deploy.worker.Worker -c 1 -m 4G spark://YOUR_IP_ADDRESS:7077`
     * Again notice I've assigned 1 core to this worker and `-m 4G` which is 4 GB of memory, replace `spark://YOUR_IP_ADDRESS:7077` with the URL you obtained from your spark webpage.
     * Navigate to localhost:8082 to view the second worker node.<br><br>
     ![Second Worker](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/Master%20%2B%20Worker%20images/Second%20Worker.png)<br><br>

   * Download the python file and change the paramters accoridngly based on the comments I've provided:
     * Open a new command prompt.
     * Run the following command `python C:/Users/UserName/Desktop/example_spark.py` or link the relative path to where you've saved your python file.<br><br>
     ![terminal Output from Python script](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/Master%20%2B%20Worker%20images/Output%20from%20the%20execution%20of%20python%20script.png)<br><br>
     ![Spark Web UI master + two workers](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/Master%20%2B%20Worker%20images/spark%20web%20ui%20with%20two%20workers.png)<br><br>

## Next Steps + Improvements :electron:
* In order to improve repeatability, the cluster should be deployed using Docker containerization.
* This will also also ensure that the cluster can be reliably recreated with the same configuration.


   
      
 
  

  
  
