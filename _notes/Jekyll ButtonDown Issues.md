---
title: ButtonDown Integration Issues with a Jekyll static website
published: 2025-01-24
tags: [site]
---
Once I was done [following the instructions to integrate ButtonDown with Netlify and Jekyll](https://buttondown.com/blog/netlify), I was getting a 422 error on ButtonDown. I couldn't figure out why but eventually Claude helped me figure out that I was sending the wrong field name to Buttondown (not what it's API expects). The javascript (`submission-created.js`) should have used { email_address: email } and not { email }, as described in the guidance.

The instructions were also unclear about a few other things. Some standout ones were:
1. the need to install `node-fetch` by the following command: `npm init -y && npm install node-fetch`
2. Indicating the right build folder for a Jekyll website in the `netlfy.toml` and the right command for it. In my case, the site was in `_site` and not `public` and the right build command for netlify to build/deploy the Jekyll site is `jekyll build`. 

So, again, worth revising for those who post those instructions specific to a Jekyll website (but it is possible that I am missing something). But for now, this website is up and running without any ButtonDown issues.