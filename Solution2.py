from boa.interop.System.Storage import GetContext, Get, Put, Delete
from boa.interop.System.Runtime import CheckWitness, GetTime, Notify, Serialize, Log

from boa.builtins import *

ctx = GetContext()
selfAddr = GetExecutingScriptHash()
testKey = 'testkey'

def Main(operation, args):
    if operation == 'put':
        return put(args[0])
    if operation == 'get':
        key = args[0]
        return get(key)
    return True

def put(key):
    a =  {'index':16, 'value':16}
    # base_ = 0xffffffff
    base_ = 4294967295
    c = key + base_
    # c = 4294967296
    Put(ctx, _concatkey(testKey, c), Serialize(a))
    Notify(["111", c])
    return True

    
def get(key):
    key1 = key + 4294967295
    a =  Get(ctx, _concatkey(testKey, key1)) #Deserialize(
    c = Deserialize(a)
    Notify(["222", key1])
    Notify([c['index'], c['value']])
    return True
    #return [a['index'], a['value']]
    
#concat key
def _concatkey(str1, str2):
    return concat(concat(str1, '_'), str2)
    