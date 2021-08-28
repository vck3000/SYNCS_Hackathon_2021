# SYNCS_Hackathon_2021

## Inspiration
[Crappy packing by Coles](https://www.news.com.au/lifestyle/food/shoppers-frustrated-over-coles-click-and-collect-bag-issue/news-story/161c9f8a4cf7fa03736b2d7b96317b25)

Automation is always the solution!

## What it does
Algorithmically determine the optimal packing arrangement.

## How we built it
We use a parallelised depth-first-search to generate all valid arrangements of items in a bag. We then use a multi-heuristic value function to determine the most optimal arrangement.

## Challenges we ran into
Conceptualising a suitable idea. One of our earlier ideas was to improve recorded audio quality using machine learning was infeasible due to insufficient time to secure a suitable dataset.

## Accomplishments that we're proud of
We bounced between a number ideas in the early stages and decided on algorithmic packing at noon on Saturday. With minimal time, we were able to learn some new things and implement a working prototype.

## What we learned
* Practical application of test-driven development process.
* Learnt about parallel computing.

## What's next for Optimal Stacking (Phat $tax)
* Integrating value function within the generation process, allowing for alpha-beta pruning.
* Improving the value function with additional/better heuristics.
* Generalise algorithm to 3D.
