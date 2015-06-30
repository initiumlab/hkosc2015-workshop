from pyspark import SparkContext

if __name__ == "__main__":

    sc = SparkContext(appName="Simple Filter")

    numbers = sc.parallelize(range(1, 10000))
    even = numbers.filter(lambda n: n % 2 == 0)
    print even.take(5)

