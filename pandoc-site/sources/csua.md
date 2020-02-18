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