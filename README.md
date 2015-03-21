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



        hyphendeMacBook-Air:ucloud-python-sdk hyphen$ python shell.py  uhost-image-list
        +----------------------------------+---------------------------------+
        | ImageId                          | ImageName                       |
        +----------------------------------+---------------------------------+
        | 0163c0c5-7481-4319-9c            | CentOS 6.2 64位                 |
        | 0c05fb5a1dfde7912344c5545b8c74bc | CentOS 5.2 64位                 |
        | 11f0dbdeca350a066cb1d0d760782f43 | Ubuntu 10.04 32位               |
        | 1f150a6c8a025f2c0c8f7f676be498fa | Debian 7.0 32位                 |
        | 346d49057e64cddcc5443a09ef82a261 | Ubuntu 12.04 32位               |
        | 39b97c4b39de86c06ee25993ef7e7464 | CentOS 5.2 32位                 |
        | 459f8ad7111c8298482d3b4cec9655ed | Ubuntu 10.04 64位               |
        | 5992f44b90125471bb76741b380d722e | Ubuntu 13.04 32位               |
        | 6e450c42e83fed6dee3e85ffd89bccdb | UCloud Debian 6.0 64位          |
        | 71ef342362885a2426a7de938c94816f | UCloud Debian 6.0 32位          |
        | 748c0e4117f6e5b116c94f324d2deeb9 | CentOS 5.8 32位                 |
        | 8a2c50c71004baebb864077ed27e1099 | Ubuntu 13.04 64位               |
        | 9d1548645601c39349d0c2bbb66943f6 | CentOS 5.4 64位                 |
        | b2689fc412ee5fa108fa5b23ed2e00e6 | CentOS 5.8 64位                 |
        | c08fbcc3d463738f4cea02d19a977e25 | CentOS 5.4 32位                 |
        | c5c4f7f6e1be0ed7f5ae5e40bca8a82b | Ubuntu 11.10 64位               |
        | dc4dbe4d-e3b6-4573-a39           | CentOS 6.2 32位                 |
        | e36b3acf76663067684332055ade6bae | Ubuntu 12.04 64位               |
        | fdc9fa3c69617cb778158262cd17c296 | Ubuntu 11.10 32位               |
        | ffeb98512dbf8fba4f3b518aba7dd224 | Debian 7.0 64位                 |
        | uimage-2aadbx                    | openSUSE 11 64位                |
        | uimage-2ojypm                    | RHEL 6.3 32位                   |
        | uimage-32cs2q                    | Ubuntu 14.04 32位               |
        | uimage-34emui                    | Windows 2012 64位 EN            |
        | uimage-3gzxij                    | CentOS 6.5 32位                 |
        | uimage-4dqokn                    | Windows 2008 64位 EN            |
        | uimage-5yt2b0                    | CentOS 7.0 64位                 |
        | uimage-aapsg0                    | CentOS 6.4 32位                 |
        | uimage-auslq4                    | Ubuntu12.04 64位 UDDP专用镜像   |
        | uimage-d04q4f                    | RHEL 5.9 64位                   |
        | uimage-dovhra                    | SLES 10 32位                    |
        | uimage-eezagu                    | RHEL 6.3 64位                   |
        | uimage-f4nsmq                    | CentOS 6.3 32位                 |
        | uimage-hp3zss                    | CentOS 5.10 64位                |
        | uimage-ijftvj                    | RHEL 5.9 32位                   |
        | uimage-j4fbrn                    | Ubuntu 14.04 64位               |
        | uimage-l25zyf                    | Windows 2008 64位               |
        | uimage-lpjytu                    | SLES 10 64位                    |
        | uimage-m3ifgu                    | CentOS 6.4 64位                 |
        | uimage-ndj4jd                    | Windows 2012 64位               |
        | uimage-ogcmcv                    | CentOS 6.3 64位                 |
        | uimage-owxcei                    | RHEL 6.2 64位                   |
        | uimage-qiut5g                    | CentOS 6.5 64位                 |
        | uimage-qlo15u                    | Gentoo 2.2 64位                 |
        | uimage-qt4b4s                    | Windows 2008 32位               |
        | uimage-rsy4nb                    | Debian7.0 64位 UDDP专用镜像     |
        | uimage-t2qre5                    |  CentOS6.3（64位）+Ecshop企业版 |
        | uimage-vupx2p                    | RHEL 6.2 32位                   |
        | uimage-xgilfh                    | Debian 6.0 32位                 |
        | uimage-yq3cgy                    | RHEL 5.7 32位                   |
        | uimage-zclgng                    | CentOS6.5 64位 UDDP专用镜像     |
        | uimage-zehxpd                    | Debian 6.0 64位                 |
        | uimage-zkezxp                    | RHEL 5.7 64位                   |
        +----------------------------------+---------------------------------+


