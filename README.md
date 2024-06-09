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
* We will start by creating two folders: :file_folder:hadoop and :file_folder:spark in your C:\
  * In the :file_folder:spark folder: first you need to go and download Apache Spark from this [link](https://spark.apache.org/downloads.html), select the release and package type and download the spark-3.5.1-bin-hadoop3.tgz file. You will then need to drag this into the C:\spark path and extract it in there.
  * In the :file_folder:hadoop folder: go to this [link](https://github.com/cdarlint/winutils) and select the hadoop version that is compatible with the previously selected package type when you were downloading Apache Spark (in my case it's for Hadoop 3.3 and later). Click on the folder that corresponds to your hadoop version and scroll down to find `winutils.exe`. You will download this and drag it into your C:\hadoop path.
