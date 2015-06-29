# hkosc2015-workshop

Files for HKOSC 2015 workshop on big data

## Agenda

June 26 (Fri) afternoon:

* Basic introduction of this workshop
* Hands-on Hadoop
* Hands-on Spark

June 27 (Sat) afternoon:

* Hands-on GraphLab
* Comparison between three platforms

## Dependencies

* VirtualBox: https://www.virtualbox.org
* Vagrant: https://www.vagrantup.com/

## GraphLab Create License

Apply a license by following instructions in page
<https://dato.com/download/>

Change the downloading link in `all/Vagrantfile` accordingly:

```
	sudo pip install --upgrade --no-cache-dir https://get.dato.com/GraphLab-Create/1.4.1/e-hkosc15@hupili.net/64CA-557D-92A5-F7D8-91A9-CC38-C9C3-BBB9/GraphLab-Create-License.tar.gz
```

## Preparation

* Download base image: `vagrant box add ubuntu/trusty64`
* `cd all`
* `vagrant up`

(This usually takes 5 to 20 minutes depending on your network)

## Next

Enjoy testing those platforms with the help of slides under `slides` folder.


