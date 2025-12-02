
def dic_basics():
    """ Demonstrates basic dictionary operations. """
    dic1 = {'a': 1, 'b': 2, 'c': 3}
    dic2 = dict(d=4, e=5, f=6)
    
    # Accessing values
    print(f"dic1['a']={dic1['a']}")
    print(f"dic2.get('d')={dic2.get('d')}")

    # The get() method will return None (or the default value) if the key doesn't exist
    print(f"dic2.get('k', 'Key not found')={dic2.get('k', 'Key not found')}")
    
    # Adding key-value pairs
    dic1['d'] = 4
    print(f"After adding, dic1={dic1}")
    
    # Updating values
    dic2['e'] = 10
    print(f"After updating, dic2={dic2}")
    
    # Removing key-value pairs
    removed_value = dic1.pop('b')
    print(f"Removed 'b' with value {removed_value}, now dic1={dic1}")

    not_existing = dic1.pop('k', "key not exists")

    # delete a key-value pair using del
    del dic1['a']
    print(f"Removed 'a, now dic1={dic1}")
    
    # Iterating through dictionary
    for key, value in dic2.items():
        print(f"Key: {key}, Value: {value}")
    
    # Iterating through keys first option
    for key in dic1.keys():
        print(f"Key in dic1: {key}")

    # Iterating through keys second option
    for key in dic1:
        print(f"dic1[{key}]={dic1[key]}")

    # Iterating through values
    for value in dic2.values():
        print(f"Value in dic2: {value}")

    # dictionary equality
    dic3 = {"name": "qikun", "age": 32 }
    dic4 = {"name": "qikun", "age": 34 }
    print(f"{dic3}=={dic4} = {dic3 == dic4}")
    print(dic3 | dic4)
    dic3.update(dic4)
    print(dic3)
    print(f"{dic3}=={dic4} = {dic3 == dic4}")

def advanced_dictionaries():
    pass 
    


if __name__ == "__main__":
    dic_basics()