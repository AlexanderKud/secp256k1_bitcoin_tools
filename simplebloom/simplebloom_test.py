from simplebloom import BloomFilter

bf = BloomFilter(100_000_000)
bf += 'helloBloom'

with open('test.bf', 'wb') as fp:
    bf.dump(fp)

with open('address.bf', 'rb') as fp:
    bf = BloomFilter.load(fp)
    
print('helloBloomy' in bf)
