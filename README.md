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
  * Once everything is installed like `python`, `pip`, `pyspark` and everything is configured you can now test the following commands in a terminal window (I've included the .txt files and the outputs from my terminal window):<br>
 ```bash
$ java -version
java version "22.0.1" 2024-04-16
Java(TM) SE Runtime Environment (build 22.0.1+8-16)
Java HotSpot(TM) 64-Bit Server VM (build 22.0.1+8-16, mixed mode, sharing)

$ javac -version
javac 22.0.1

$ echo %SPARK_HOME%
C:\spark\spark-3.5.1-bin-hadoop3

$ echo %JAVA_HOME%
C:\Program Files\Java\jdk-22

echo %HADOOP_HOME%
C:\hadoop
```

  * You can then use the following command `pyspark` in your terminal window to start a spark session, navigate to http://localhost:4040 to check the Spark Web UI.<br>
 ```bash
$ pyspark
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/06/10 04:23:32 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.5.1
      /_/

Using Python version 3.11.0 (main, Oct 24 2022 18:26:48)
Spark context Web UI available at http://DESKTOP-RVG77MU.mshome.net:4040
Spark context available as 'sc' (master = local[*], app id = local-1718007813499).
SparkSession available as 'spark'.
>>> 24/06/10 04:23:46 WARN GarbageCollectionMetrics: To enable non-built-in garbage collector(s) List(G1 Concurrent GC), users should configure it(them) to spark.eventLog.gcMetrics.youngGenerationGarbageCollectors or spark.eventLog.gcMetrics.oldGenerationGarbageCollector
```
  ### Setting up the master and worker nodes using command prompts + running the python file:
  * We can now create a master node:
    * First open a command prompt window and `cd %SPARK_HOME%`.
    * Use the following command: `bin\spark-class2.cmd org.apache.spark.deploy.master.Master`
    * This will deploy the master node, you can verify this by navigating to localhost:8080 (this web page is important because you will need to extract the URl of the master)<br>
 ```bash
$ cd %SPARK_HOME%

$ bin\spark-class2.cmd org.apache.spark.deploy.master.Master
Using Spark's default log4j profile: org/apache/spark/log4j2-defaults.properties
24/06/10 04:31:28 INFO Master: Started daemon with process name: 38244@DESKTOP-RVG77MU
24/06/10 04:31:28 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
24/06/10 04:31:28 INFO SecurityManager: Changing view acls to: ku_ch
24/06/10 04:31:28 INFO SecurityManager: Changing modify acls to: ku_ch
24/06/10 04:31:28 INFO SecurityManager: Changing view acls groups to:
24/06/10 04:31:28 INFO SecurityManager: Changing modify acls groups to:
24/06/10 04:31:28 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: ku_ch; groups with view permissions: EMPTY; users with modify permissions: ku_ch; groups with modify permissions: EMPTY
24/06/10 04:31:28 INFO Utils: Successfully started service 'sparkMaster' on port 7077.
24/06/10 04:31:28 INFO Master: Starting Spark master at spark://172.19.160.1:7077
24/06/10 04:31:28 INFO Master: Running Spark version 3.5.1
24/06/10 04:31:29 INFO JettyUtils: Start Jetty 0.0.0.0:8080 for MasterUI
24/06/10 04:31:29 INFO Utils: Successfully started service 'MasterUI' on port 8080.
24/06/10 04:31:29 INFO MasterWebUI: Bound MasterWebUI to 0.0.0.0, and started at http://DESKTOP-RVG77MU.mshome.net:8080
24/06/10 04:31:29 INFO Master: I have been elected leader! New state: ALIVE
```
   * Create the first worker node:
     * Open another command prompt window and `cd %SPARK_HOME%`.
     * Use the following command: `bin\spark-class2.cmd org.apache.spark.deploy.worker.Worker -c 1 -m 4G spark://YOUR_IP_ADDRESS:7077`
     * Notice that the `-c 1` indicates I want to assign 1 core to this worker and `-m 4G` which is 4 GB of memory, replace `spark://YOUR_IP_ADDRESS:7077` with the URL you obtained from your spark webpage.
     * You can now navigate to localhost:8081 to view this worker node.<br>
 ```bash
$ cd %SPARK_HOME%

$ bin\spark-class2.cmd org.apache.spark.deploy.worker.Worker -c 1 -m 4G spark://YOUR_IP_ADDRESS:7077
0.1:7077
Using Spark's default log4j profile: org/apache/spark/log4j2-defaults.properties
24/06/10 04:33:45 INFO Worker: Started daemon with process name: 12924@DESKTOP-RVG77MU
24/06/10 04:33:46 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
24/06/10 04:33:46 INFO SecurityManager: Changing view acls to: ku_ch
24/06/10 04:33:46 INFO SecurityManager: Changing modify acls to: ku_ch
24/06/10 04:33:46 INFO SecurityManager: Changing view acls groups to:
24/06/10 04:33:46 INFO SecurityManager: Changing modify acls groups to:
24/06/10 04:33:46 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: ku_ch; groups with view permissions: EMPTY; users with modify permissions: ku_ch; groups with modify permissions: EMPTY
24/06/10 04:33:46 INFO Utils: Successfully started service 'sparkWorker' on port 62741.
24/06/10 04:33:46 INFO Worker: Worker decommissioning not enabled.
24/06/10 04:33:46 INFO Worker: Starting Spark worker 172.19.160.1:62741 with 1 cores, 4.0 GiB RAM
24/06/10 04:33:46 INFO Worker: Running Spark version 3.5.1
24/06/10 04:33:46 INFO Worker: Spark home: C:\spark\spark-3.5.1-bin-hadoop3
24/06/10 04:33:46 INFO ResourceUtils: ==============================================================
24/06/10 04:33:46 INFO ResourceUtils: No custom resources configured for spark.worker.
24/06/10 04:33:46 INFO ResourceUtils: ==============================================================
24/06/10 04:33:46 INFO JettyUtils: Start Jetty 0.0.0.0:8081 for WorkerUI
24/06/10 04:33:46 INFO Utils: Successfully started service 'WorkerUI' on port 8081.
24/06/10 04:33:47 INFO WorkerWebUI: Bound WorkerWebUI to 0.0.0.0, and started at http://DESKTOP-RVG77MU.mshome.net:8081
24/06/10 04:33:47 INFO Worker: Connecting to master 172.19.160.1:7077...
24/06/10 04:33:47 INFO TransportClientFactory: Successfully created connection to /172.19.160.1:7077 after 29 ms (0 ms spent in bootstraps)
24/06/10 04:33:47 INFO Worker: Successfully registered with master spark://172.19.160.1:7077
```
   * Create the second worker node:
     * Open another command prompt window and `cd %SPARK_HOME%`.
     * Use the following command: `bin\spark-class2.cmd org.apache.spark.deploy.worker.Worker -c 1 -m 4G spark://YOUR_IP_ADDRESS:7077`
     * Again notice I've assigned 1 core to this worker and `-m 4G` which is 4 GB of memory, replace `spark://YOUR_IP_ADDRESS:7077` with the URL you obtained from your spark webpage.
     * Navigate to localhost:8082 to view the second worker node.<br>
  ```bash
$ cd %SPARK_HOME%

$ bin\spark-class2.cmd org.apache.spark.deploy.worker.Worker -c 1 -m 4G spark://YOUR_IP_ADDRESS:7077
0.1:7077
Using Spark's default log4j profile: org/apache/spark/log4j2-defaults.properties
24/06/10 04:39:01 INFO Worker: Started daemon with process name: 29608@DESKTOP-RVG77MU
24/06/10 04:39:01 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
24/06/10 04:39:01 INFO SecurityManager: Changing view acls to: ku_ch
24/06/10 04:39:01 INFO SecurityManager: Changing modify acls to: ku_ch
24/06/10 04:39:01 INFO SecurityManager: Changing view acls groups to:
24/06/10 04:39:01 INFO SecurityManager: Changing modify acls groups to:
24/06/10 04:39:01 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: ku_ch; groups with view permissions: EMPTY; users with modify permissions: ku_ch; groups with modify permissions: EMPTY
24/06/10 04:39:02 INFO Utils: Successfully started service 'sparkWorker' on port 62776.
24/06/10 04:39:02 INFO Worker: Worker decommissioning not enabled.
24/06/10 04:39:02 INFO Worker: Starting Spark worker 172.19.160.1:62776 with 1 cores, 4.0 GiB RAM
24/06/10 04:39:02 INFO Worker: Running Spark version 3.5.1
24/06/10 04:39:02 INFO Worker: Spark home: C:\spark\spark-3.5.1-bin-hadoop3
24/06/10 04:39:02 INFO ResourceUtils: ==============================================================
24/06/10 04:39:02 INFO ResourceUtils: No custom resources configured for spark.worker.
24/06/10 04:39:02 INFO ResourceUtils: ==============================================================
24/06/10 04:39:02 INFO JettyUtils: Start Jetty 0.0.0.0:8081 for WorkerUI
24/06/10 04:39:02 WARN Utils: Service 'WorkerUI' could not bind on port 8081. Attempting port 8082.
24/06/10 04:39:02 INFO Utils: Successfully started service 'WorkerUI' on port 8082.
24/06/10 04:39:02 INFO WorkerWebUI: Bound WorkerWebUI to 0.0.0.0, and started at http://DESKTOP-RVG77MU.mshome.net:8082
24/06/10 04:39:02 INFO Worker: Connecting to master 172.19.160.1:7077...
24/06/10 04:39:02 INFO TransportClientFactory: Successfully created connection to /172.19.160.1:7077 after 32 ms (0 ms spent in bootstraps)
24/06/10 04:39:02 INFO Worker: Successfully registered with master spark://172.19.160.1:7077
```
   * Download the python file and change the paramters accoridngly based on the comments I've provided:
     * Open a new command prompt.
     * Run the following command `python C:/Users/UserName/Desktop/example_spark.py` or link the relative path to where you've saved your python file.<br>
  ```python
import findspark
findspark.init('C:\spark\spark-3.5.1-bin-hadoop3')

from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('spark://172.19.160.1:7077')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)

data = [1,2,3,4,5,6,7,8,9,10]

dist_data = sc.parallelize(data, numSlices=2)

result = dist_data.map(lambda x: x*x).collect()

print(result)
```
  ```bash
$ python C:/Users/UserName/Desktop/example_spark.py
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/06/10 04:40:40 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

...

SUCCESS: The process with PID 43040 (child process of PID 36296) has been terminated.
SUCCESS: The process with PID 36296 (child process of PID 30976) has been terminated.
SUCCESS: The process with PID 30976 (child process of PID 2108) has been terminated.
```
![Spark Web UI master + two workers](https://github.com/Turnipdo/Spark-Standalone-Cluster-Setup/blob/main/Images/Master%20%2B%20Worker%20images/spark%20web%20ui%20with%20two%20workers.png)<br><br>

## Next Steps + Improvements :electron:
* In order to improve repeatability, the cluster should be deployed using Docker containerization.
* This will also also ensure that the cluster can be reliably recreated with the same configuration.


   
      
 
  

  
  
