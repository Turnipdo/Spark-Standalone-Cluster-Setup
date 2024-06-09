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
* You want to install [Java JDK](https://www.oracle.com/java/technologies/downloads/#jdk22-windows) onto your computer by selecting the x64 installer. This installation will be located in the `C:\Program Files\Java\jdk-22` by default (this will be important in the following steps).
* We will then create two folders: :file_folder:hadoop and :file_folder:spark in your `C:\` drive.
  * In the :file_folder:spark folder: you need to go and download Apache Spark from this [link](https://spark.apache.org/downloads.html), select the release and package type and download the spark-3.5.1-bin-hadoop3.tgz file. You will then need to drag this into the `C:\spark` path and extract it in there.
  * In the :file_folder:hadoop folder: create another folder called `bin`, then go to this [link](https://github.com/cdarlint/winutils) and select the hadoop version that is compatible with the previously selected package type when you were downloading Apache Spark (in my case it's for Hadoop 3.3 and later). Click on the folder that corresponds to your hadoop version and scroll down to find `winutils.exe`. You will download this into your `C:\hadoop\bin` path.
* We now have to setup a bunch of system environment variables in order for all of this to work.
  * HADOOP_HOME
  * JAVA_HOME
  * SPARK_HOME
  * PYSPARK_PYTHON (in case it's python and not python3 cmd that works)
  * Setup a bunch of PATHS which includes:
    * C:\Program Files\Java\jdk-22\bin
    * %SPARK_HOME%\bin
    * %JAVA_HOME%\bin
    * C:\Users\ku_ch\AppData\Local\Programs\Python\Python311
    * C:\Users\ku_ch\AppData\Local\Programs\Python\Python311\Scripts (this is for pip installation another tangent we need to mention)
    * %HADOOP_HOME%\bin
