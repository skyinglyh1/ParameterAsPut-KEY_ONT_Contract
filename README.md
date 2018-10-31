把Put(ctx, _concatkey(testKey, 16), Serialize(a))中的16换为你传入的key参数 就没有问题了 

如果在合约内部用16作为KEY的一部分 底层处理的时候会转为bytearray 1000000000000000  

如果用传入的key参数作为KEY的一部分（比如integer 16），底层处理的时候会转为bytearray 10


当去get的时候，传入的key是16的时候， 底层处理的时候会转为bytearray 10，就能兑得上了 也能取出来了 

put的时候 KEY的产生应该是需要参数来构建的，就合理了