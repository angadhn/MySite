---
title: Buttondown Newsletter Setup
---

Used this [post](https://buttondown.com/blog/netlify) to setup newsletter on my blog.

However, it should have spelled out more clearly two things that were bugs for me:
1. the need to install `node-fetch` by the following command: `npm init -y && npm install node-fetch`
2. Creating a `success.html` file in the `_includes` folder and adding the following to the `_layouts/default.html` file.

I saw Steph Ango has it and this [blog](https://michaelsoolee.com/buttondown-newsletter-5-reasons/) made it sound nice too.