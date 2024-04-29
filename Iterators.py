"""
Python Iterators:
    An iterator is an object that contains a countable number of values
    
    An iteator is an object that can be iterated upon, meaning that you can traverse through all the values.
    
    Technically, in python . an iterator is an object which implements the iterator protocol, which consist of the methods iter() and next().
    
    """

#list

for i in (1, 2, 3, 4, 5):
    print(i)

#string

for char in "python":
    print(char)


#dictionary

for k in {"x" : 1,
          "y" : 2}:
    print(k)


#set

for l in { 1, 2, 3, 4, 5, 6 }:
    print(l)


#tuples

for m in (1, 2, 3, 4, 5 ):
    print(m)



'''
    
    Iterating through an iterator: 

        - The iter() function (which in turn calls the iter() method) returns an iterator from them.
        - We use the next() function to manually iterate through all the items of an iterator.
        - When we reach the end and there is no more data to be returned it will raise the StopIteraion Exception,
    
    '''
my_list = [1, 2, 3, 4, 5 ]

# create an iteratior object from that iterable

item_obj = iter(my_list)

#infinite loop

while True:
    try:
        #get the next item
        element = next(item_obj)
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from look
        break


'''
    - So internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable
    
    - Ironically, this for loop is actually an infinite whilr loop.
    
    - Inside the loop, it calls next() to get the next element and executes the body of the for loop with this value. After all the items exhaust, StopIteration is raised which is internally caught and the loop ends.
        
        -- Note that any other kind of exception will pass through '''

