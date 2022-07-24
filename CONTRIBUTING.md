# Contributing
## Current Needs:
* Additional templates for Holidays.
  * Create a Holiday template using the most widely accepted date for a given holiday.
  * If the holiday has special or additional rules regarding its observance, create a derivative class that inherits from the generic.
  * If the holiday's criteria are specific to a country, suffix the primary with the 2 letter ISO Country Code
  * If the holiday's criteria is non-secular, use a suffix that best describes the origins if the holiday has shared meaning across different faiths.
  * Any holiday that is not widely known, must include a reference to documentation regarding it's origins and how the date is calculated.

## General fixes:
* If there is a defect in the code, please make a pull request with appropriate documentation. Documentation must include re-creation steps, applicable unit tests, and an explination why it is believed to be a defect.

## Best Practices:
* One voice - when editing the code, preserve the "voice" of the previous authors.
  * Follow the lead how things are named and formatted. If the naming conventions are snake case, continue with the same approach. Whitespace, as well.
* Disable or avoid using auto formatting tools. They can complicate code reviews and code merges
* Code should remain concise on a line, but do not enforce a max line length.
* Lines with comments should make a reasonable attempt to keep line length under 80 columns.
* Keep code approachable. Avoid using complex single line expressions.
* Be descriptive when naming objects. Avoid abbreviations, and give meaningful names to objects.
