# Writing tests for a complex class

In this Paired Challenge, you should either reuse an existing pytest project or
[set up a new pytest project](../pills/setting_up_a_pytest_project.md).

## Paired Challenge

Add this file to your `lib` directory:

```python
# File: lib/most_often.py

class MostOften:
    def __init__(self, starting_list):
        self.starting_list = starting_list
    
    def add_new(self, new_item):
        self.starting_list.append(new_item)
    
    def get_most_often(self):
        # use set() to create a list of unique items
        unique_items = set(self.starting_list)
        
        # set up our highest recorded variables
        highest_count = 0
        highest_items = []
        
        for item in unique_items:
            # count the number of instances of that item in the list
            count = self.starting_list.count(item)
            # if we've found a new highest count...
            if count > highest_count:
                highest_count = count
                highest_items = [item]
            # but if we've found an equally high count...
            elif count == highest_count:
                highest_items.append(item)
        
        # if we have a clear winner, return it
        if len(highest_items) == 1:
            return highest_items[0]
        # otherwise we'll say there's "no clear winner"
        else:
            return "no clear winner"
```

In your pair, write tests for this class in a file `tests/test_most_often.py`.
Make sure to run pytest to check whether your tests are passing.

To help guide you, think about these questions in your pair:

* What functionality does each of the methods in the class have?
* What sorts of types in the list might be testable?
* If we were only ever dealing with integers (let's say), then what sorts of
  interesting list contents at instantiation and later on (after adding new)
  could be worth including in the tests?
* How many different outcomes are there that are testable, from
  `get_most_often()` and do you have tests for those?
* Do your tests cover at least all of the core functionality of the class, even
  if you aren't testing _every_ type in the list or every combination of inputs?

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_complex_class.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_complex_class.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_complex_class.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_complex_class.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_complex_class.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
