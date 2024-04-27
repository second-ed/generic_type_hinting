# The Problem
Trying to find the generic type of multiple possible arguments for type hinting and enforcing.

#### Example:
A function adds two arrays of numbers together but we want to be explicit about what type it can take and raise any errors if the wrong type is entered. As well as numpy arrays it should be able to take pandas series, lists and dictionary keys. However we still want to catch when a user inputs an int.

# Solution
## Using dunders to categorise
By using the `mro()` feature of all objects we could trace back to `object` to find where in the inheritance tree the objects start to match, however this normally always results in `object` being the first point where they match. 

Instead by using the `__dunder__` methods that the object implements we can trace up the inheritance tree to find where there is a generic classification that all objects satisfy. To do this I used the map found in Fluent Python by Luciano Ramalho (pictured below).

![Fluent Python map of generic collection types](https://www.oreilly.com/api/v2/epubs/9781492056348/files/assets/flpy_0102.png)

We walk up this inheritance tree until all possible argument types have a group of dunder methods that they agree on, and return that as the type that the type hint should show and the `isinstance` should check for (in important cases).


# Examples
Here we want the generic type that would satisfy taking a list, dict, set, pd.Series and np.ndarray

```python
gth = GenericTypeHinter()
gth.analyse_group([[], {}, set(), pd.Series(), np.ndarray])
```
this returns:
```
[collections.abc.Collection,
 collections.abc.Sized,
 collections.abc.Iterable,
 collections.abc.Container,
 object]
```
the 0th element in that list is the lowest common element (imagining an inheritance tree with object at the top etc), in this case its `Collection` and we can see if there was no earlier common element we'd eventually reach `object` (which would be a useless and uninformative type hint, and even more useless test)

by finding this lowest common element we can make the functions more flexible by not only having to recieve a list etc but not sacrifice our ability to test the type on entry to the function
