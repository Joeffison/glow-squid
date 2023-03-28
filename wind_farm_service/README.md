# Considerations

1. Nomenclature: I am not happy with some of the names here. I tried to be as close as possible to
the language used in the challenge description to respect the ubiquitous language but I was already
confused from the start by the choice of names in the description
(example: why calling "Wind Farms" by "Projects") but due to the lack of an onboarding into this
context, I tried to respect that language as YOU are the domain experts.
In a work environment, I would have the time/scope to ask.

2. At development time, the order of the fields in the models was preserved from the csv files.
Usually, I would write the fields/properties in alphabetic order but due to the interview already
next Tuesday, I thought it might be easier to compare the results if we could easily map the fields
and columns to the csv format during the demo.

3. I used django as it was required in the project but I would otherwise have used Flask or FastPI
because I have not worked with Django since at least 5 or 6 years.

4. The management commands could easily extend a class with all the methods to import the models
and have a mapping ("csv column" to "model fields") to deserialize the input.

5. Typically, the import commands would not import the IDs to avoid problems with the
auto generated IDs mechanism. For the sake of the demo, I opted to keep it.

6. Add more human-readable errors specially to the import command

7. Add tests (I would have otherwise created them during development time but it was not possible
in such a short time to deliver )
