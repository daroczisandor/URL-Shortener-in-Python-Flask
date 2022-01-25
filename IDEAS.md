Endpoints:
- Encoder: Will create a short URL by generating 5 random characters and putting the result into a dictionary
- Decoder: Will search for the given url in the dictionary, and redirect if found

But how to use the dictionary?

**Idea 1:** Use only one dictionary, e.g. in the form {short_url: long_url}.
But then determining if a long_url has already been encoded would take O(n) time,
since we would then have to search among the dict.values().

The same reasoning applies to the case {long_url: short_url}, since then
searching for a short_url would be O(n).

**Idea 2:** Use two dictonaries, one of the form {short_url: long_url},
and another of the form {long_url: short_url}.
Then, searching for both short and long urls will take O(1) time in average.
However, the drawback is that the memory usage doubles compared to
using a single dict.
But nevertheless, we will implement this idea.

