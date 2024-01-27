# Design and test-drive a more complex function

## Paired Challenge

Follow the [design recipe](../resources/single_function_recipe_template.md) to
implement the following user stories in a project. This will be in a new, single
function.

```
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.
```

E.g. if today's date was 2022-11-01:

```
>>> age_checker("1960-10-21")
"Access granted!"
```

You may want to make use of the `datetime` and `dateutil` libraries here. It's
good practice - dates and/or times are necessary parts of many applications, as
are the calculations between pairs of them.

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fdesign_and_tdd_complex_function.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fdesign_and_tdd_complex_function.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fdesign_and_tdd_complex_function.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fdesign_and_tdd_complex_function.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fdesign_and_tdd_complex_function.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
