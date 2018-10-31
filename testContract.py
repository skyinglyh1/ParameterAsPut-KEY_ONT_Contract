from boa.interop.System.Storage import GetContext, Get, Put, Delete
from boa.interop.System.Runtime import CheckWitness, GetTime, Notify, Serialize, Log

from boa.builtins import *

ctx = GetContext()
selfAddr = GetExecutingScriptHash()
testKey = 'testkey'
def Main(operation, args):
    if operation == 'put':
        key = args[0]
        return put(key)
    if operation == 'get':
        key = args[0]
        return get(key)
    return False

def put(key):
    a =  {'index':16, 'value':16}
    # c = 16
    # Notify([c])
    # Put(ctx, _concatkey(testKey, 16), Serialize(a))
    Put(ctx, _concatkey(testKey, key), Serialize(a))
    return True
def get(key):
    Notify([key])
    a =  Deserialize(Get(ctx, _concatkey(testKey, key)))
    Notify([key])
    return [a['index'], a['value']]
#concat key
def _concatkey(str1, str2):
    return concat(concat(str1, '_'), str2)
    