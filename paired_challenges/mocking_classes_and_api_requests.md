# Mocking classes and API requests

## Paired Challenge

Two classes called `TimeZone` and `TimeHandler` have been written, along with
some valuable unit tests for `TimeZone`.

The tests for `TimeHandler` currently rely upon two things - having the
`TimeZone` class correctly written and available to use, and an external API
which returns a JSON representation of the current date and time in GMT
(Greenwich Mean Time).

### Code

The required `lib`, `tests` and `Pipfile` are all in
[mocking_challenge_code](./mocking_challenge_code/). Note that you'll need to
build a new virtual environment from the `Pipfile`, as it'll contain the
necessary libraries.

You can check everything is working OK so far by activating your virtual
environment with `pipenv shell` then running `pytest` - you should see 5 passed
tests and 2 skipped.

### Challenge

Your challenge is to rewrite the tests for `TimeHandler` using mocks for:

* The `TimeZone` class
* The API call to http://worldtimeapi.org

We'd suggest you start by spending some time looking through the existing code,
to understand what it currently does and how it works. If you want to look at
the API call, run this at your command line:

```
% curl "http://worldtimeapi.org/api/timezone/GMT"
```

You can choose to update the existing tests or create a new test file. Don't
forget that you can run Pytest on a specific test file with something like:

```
% pytest tests/test_my_filename.py
```

### Checking your work

If you want to prove that you've mocked everything that's required, try

* Commenting out all the code in `TimeZone`
* Making sure there's no `from lib.time_zone import *` line in your new test
  file
* Changing the URL for http://worldtimeapi.org in `TimeHandler` to something
  that doesn't exist
* Running Pytest on just your new file of tests - all five should pass, if it's
  no longer relying on `TimeZone` nor a working call to the World Time API

### Stuck?

<details>
  <summary>We're really stuck on the second part...</summary>

  Note that the second part of mocking will also require some changes to the
  `TimeHandler` class as well, so that you're able to mock the API request and
  response. Refer to the curriculum if you aren't sure - the answers _are_ in
  there!
</details>

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fmocking_classes_and_api_requests.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fmocking_classes_and_api_requests.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fmocking_classes_and_api_requests.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fmocking_classes_and_api_requests.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=paired_challenges%2Fmocking_classes_and_api_requests.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
