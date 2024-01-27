# Writing tests for a simple class

In this Paired Challenge, you should either reuse an existing pytest project or
[set up a new pytest project](../pills/setting_up_a_pytest_project.md).

## Paired Challenge

Add this file to your `lib` directory:

```python
# File: lib/high_value.py

class HighValue:
    def __init__(self, value_first, value_second):
        self.value_first = value_first
        self.value_second = value_second
    def get_highest(self):
        if self.value_first > self.value_second:
            return "First value is higher"
        elif self.value_first < self.value_second:
            return "Second value is higher"
        else:
            return "Values are equal"
    def add(self, increase_by, selection):
        if selection == "first":
            self.value_first += increase_by
        elif selection == "second":
            self.value_second += increase_by
```

In your pair, write tests for this class in a file `tests/test_high_value.py`.
Make sure to run pytest to check whether your tests are passing.

__Note__: Don't forget that you can interactively load the file into the Python
REPL, if you want to try it out as a way of better understanding what it does
e.g.:

```
% python3 -i lib/high_value.py
>>> hv = HighValue(3, 7)
>>> hv.get_highest()
'Second value is higher'
```

To help guide you, think about these questions in your pair:

* What functionality does the class look like it has? What _type_ are the values
  being set, added to and compared?
* What test(s) can you add to check the two class attributes, set at the time a
  new object of type `HighValue` is instantiated?
* What are the three possible outcomes from get_highest() and can you write a
  separate test for each one?
* What parts of the `HighValue` object does add() affect? And what are the two
  different types of ways you could check that? (Hint: there's one method and
  one non-method way)

<details>
  <summary>We're stuck - can we have a list of test ideas to get us started?</summary>

  Only read through this if you really have to!

  Remember there's no "perfect" list of tests to add, or content for those tests
  to contain, so you could do things differently... but here's a list of test
  ideas you could consider covering with one separate pytest test for each:

  * Instantiation of `HighValue` and both class attributes
  * First value higher
  * Second value higher
  * Values equal
  * Add to first value, check class attribute has changed
  * Add to second value, check class attribute has changed
  * A sequence of events from instantiation to adding values, to checking which
    is now the highest (and different outcomes from that) i.e. a more complex
    case bringing together multiple bits of functionality
  * Handling of negative and/or zero values
</details>

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_simple_class.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_simple_class.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_simple_class.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_simple_class.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Ftesting_a_simple_class.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
