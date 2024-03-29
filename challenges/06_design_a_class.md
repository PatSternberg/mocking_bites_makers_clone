# Design a Single-Class Program

_**This is a Makers Vine.** Vines are designed to gradually build up
sophisticated skills. They contain a mixture of text and video, and may contain
some challenge exercises without proposed solutions. [Read more about how to use
Makers
Vines.](https://github.com/makersacademy/course/blob/main/labels/vines.md)_

Learn to design a single-class program.

## Introduction

To design single-class programs we need to update our design recipe. Here is the
updated recipe:

> # Single-Class Programs Design Recipe
> 
> ## 1. Describe the Problem
> 
> Typically you will be given a short statement that does this called a user
> story. In industry, you may also need to ask further questions to clarify
> aspects of the problem.
> 
> ## 2. Design the Class Interface
> 
> The interface of a class includes:
> 
> * The name of the class.
> * The design of its initializer, the parameters it takes, and their data types
> * The design of any properties the user will need to read or write, and their
>   data types
> * The design of its public methods, including:
>   * Their names and purposes
>   * What parameters they take and the data types
>   * What they return and that data type
>   * Any other side effects they might have
> 
> Steps 3 and 4 then operate as a cycle.
> 
> ## 3. Create Examples as Tests
> 
> These are examples of the class being used with different initializer
> arguments, method calls, and how it should behave.
> 
> For complex challenges you might want to come up with a list of examples first
> and then test-drive them one by one. For simpler ones you might just dive
> straight into writing a test for the first example you want to address.
> 
> ## 4. Implement the Behaviour
> 
> For each example you create as a test, implement the behaviour that allows the
> class to behave according to your example.
> 
> At this point you may wish to apply small-step test-driving to manage the
> complexity. This means you only write the minimum lines of the example to get
> the test to fail (red), then make it pass (green) and refactor, before adding
> another line to the test until it fails, then continue.
> 
> Then return to step 3 until you have addressed the problem you were given. You
> may also need to revise your design, for example if you realise you made a
> mistake earlier.

Copy and fill out [this
template](../resources/single_class_recipe_template.md) for each of the
below exercises.

## Demonstration

[A video demonstration](https://youtu.be/OjrhRL4i1kc?t=0s)

<!-- OMITTED -->

## Exercise

Follow the design recipe to implement the following user stories in your
project. Both of these will be within a single class.

> As a user  
> So that I can keep track of my tasks  
> I want a program that I can add todo tasks to and see a list of them.

> As a user  
> So that I can focus on tasks to complete  
> I want to mark tasks as complete and have them disappear from the list.

Don't worry about user input & output here.

<details>
  <summary>:confused: I keep getting `TypeError: 'list' object is not callable`</summary>

  Note that your methods and instance variables (e.g. `self.list`) can't be
  named the same thing. 
  
  An easy way to go right is to name your instance variables with a leading
  underscore (e.g. `self._list`).

  If you keep having trouble, feel free to refer to the video or discuss with
  your coach.
</details>

[Example Solution](https://youtu.be/OjrhRL4i1kc?t=1805s)


[Next Challenge](07_intermezzo_debugging_2.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F06_design_a_class.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F06_design_a_class.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F06_design_a_class.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F06_design_a_class.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F06_design_a_class.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
