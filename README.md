# FOCUSED-CRAWLER

 Implement your own web crawler which Performing category : focused crawling
Description: Crawling the documents: 
A. Start with the following seed URL from Wikipedia: 
https://en.wikipedia.org/wiki/Tropical_cyclone. 
B. Your crawler has to respect the politeness policy by using a delay of at least one second 
between your HTTP requests.
C. Your crawler must assume that the earlier the hyperlink appears in a page, the more important 
it is (and hence must be crawled first) and that shallower depths are more important than deeper 
pages.
D. Follow the links with the prefix https://en.wikipedia.org/wiki that lead to articles only (avoid 
administrative links containing :) Also, make sure to properly treat URLs with # which basically 
denotes a section within the (same) page and not a different one. Non-English articles, external 
links, main Wikipedia page, navigations and marginal/side links must not be followed. You may 
ignore formulas, images, and non-textual media. 
E. Crawl to depth 6. The seed page is the first URL in your frontier and thus counts for depth 1. 
F. Stop once you’ve crawled 100-500 unique URLs. Keep a list of these URLs in a text file. You 
should handle redirected pages to avoid duplicates



Only 250 unique url are crawled
