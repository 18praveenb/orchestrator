# Setting up SSH with GitHub

[Wonderful tutorial from Github itself](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

# How to set up CSUA

1. Create an account
2. Create a public/private SSH key pair [GitHub tutorial](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
3. Copy the public key. SSH to latte, create a `~/.ssh/authorized_keys' file and copy the public key there.
4. It should be possible to `ssh` into latte now. For convenience, you could add the following to your `~/.ssh/config` file so that `ssh csua` just works.
```
Host latte
  HostName latte.csua.berkeley.edu
  User YOUR_USER_NAME
  IdentityFile PATH/TO/PRIVATE_KEY
```

# How to set up Jupyter 

Open two terminal windows, A and B.

In window A, `ssh latte` (or `ssh username@latte.csua.berkeley.edu`) and then install jupyter.

Run `jupyter notebook --no-browser` and check which port it's using (in its terminal output).

There should be a line `http://localhost:8888/?token=088de52ac910000087c9c24a15de8a0c68665ab1c2ee0687` or something like that.

Then in window B, run `ssh -N -L [to]:localhost:[from] [username]@latte.csua.berkeley.edu`

**to** is the port you want to connect Jupyter to on your machine.
**from** is the port that Jupyter is running on CSUA (the number that you saw earlier).

Keep the ssh running. Now, in a browser, copy the line from above, but change the port number to **to**.

It should connect to Jupyter.