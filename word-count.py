from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///sparkCourse/Book.txt")
rdd = lines.flatMap(lambda x: x.split())
wc = rdd.countByValue()

for word, count in wc.items():
    cleanWord = word.encode('ascii','ignore')
    if(cleanWord):
        print(cleanWord, count)
