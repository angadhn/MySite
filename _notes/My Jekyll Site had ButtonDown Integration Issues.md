# My Jekyll Site had ButtonDown Integration Issues
However, I was getting a 422 error at ButtonDown. Coulnd't figure out why but eventually Claude helped me
out that we were sending the wrong field name (not what Buttondown's API expects). The
javascript (`submission-created.js`) should have used { email_address: email } and not { email }. The blog
was also unclear about a few orther things. Some stand out ones are:
1. the need to install `node-fetch` by the following command: `npm init -y && npm install node-fetch`
2. Indicating the right build folder for a Jekyll website in the `netlfy.toml` and the right command for it
for netlify to deploy it.