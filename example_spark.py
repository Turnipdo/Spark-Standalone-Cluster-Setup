import findspark
findspark.init('C:\spark\spark-3.5.1-bin-hadoop3')

from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('spark://172.19.160.1:7077') #This will change depending on what the URL is for your master node when you open up the web[age localhost:8080
conf.setAppName('spark-basic') #Name it whatever you'd like
sc = SparkContext(conf=conf)

data = [1,2,3,4,5,6,7,8,9,10] #Create an RDD

dist_data = sc.parallelize(data, numSlices=2) #Split the data into two partitions and the master node will assign it accordingly to the workers

result = dist_data.map(lambda x: x*x).collect() #Simply doing a power of two (square) operation on the data.

print(result)

