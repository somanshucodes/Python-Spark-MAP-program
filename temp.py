from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("Temperature")
sc = SparkContext(conf = conf)

def fun(line):
    fields = line.split(',')
    station = fields[0]
    e_type = fields[2]
    temp = float(fields[3])
    return (station,e_type, temp)
    

lines = sc.textFile("file:///SparkCourse//1800.csv")
rdd = lines.map(fun)
weather=rdd.filter(lambda x : "TMIN" in x[1])
x = weather.map(lambda x : (x[0],x[2]))
y = x.reduceByKey(lambda x,y : min(x,y))


#rdd = lines.map(fun)
results = y.collect();
for result in results:
    print(result)