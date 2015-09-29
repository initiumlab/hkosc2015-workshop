from pyspark import SparkContext

if __name__ == "__main__":

    sc = SparkContext(appName="WordCount")

    log = sc.textFile("/home/vagrant/spark/101workshop/error_log")
    # Split lines into words
    word_cnt = log.flatMap(lambda line: line.split(" ")) \
    # Get rid of empty words
    .filter(lambda w: bool(w)) \
    # Each word appear once
    .map(lambda w: (w, 1)) \
    # For the same word, count the times it appears
    .reduceByKey(lambda wc1, wc2: wc1 + wc2) \
    # Switch the count and the word in the tuple
    .map(lambda w: (w[1], w[0])) \
    # Descendant sort in accordance with the count
    .sortByKey(False)

    # Logic graph of the transformations
    print word_cnt.take(5)

