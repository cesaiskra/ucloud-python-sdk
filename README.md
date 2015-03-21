this is a python sdk for ucloud,as well as a CLI tools for ucloud in linux bash
env.

1. sdk usage:


        from ucloud-python-sdk import client as uclient
        cl=uclient(base_url, public_key, private_key)
        result=cl.uhost.create(region="cnnorth-03",imageId="uimageqiut5g",loginMode="Password",
                            password="yanheventest",tag="Group1",type="BD")


2. command-line usage:

        hyphendeMacBook-Air:ucloud-python-sdk hyphen$ python shell.py
        usage: ucloud [--debug] [--timings] <subcommand> ...

        Command line interface for ucloud

        Positional arguments:
          <subcommand>
            uhost-create    boot a host
            uhost-image-list
                            list all images
            uhost-list      list uhosts
            uhost-show      show a uhost
            bash-completion
                            Prints all of the commands and options to stdout so that
                            the ucloud.bash_completion script doesn't have to hard
                            code them.
            help            Display help about this program or one of its subcommands.

        Optional arguments:
          --debug           Print debugging output
          --timings         Print call timing info

        See "ucloud help COMMAND" for help on a specific command.