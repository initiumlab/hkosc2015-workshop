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

## Setup Hadoop+Spark: 

Method1: Build from base image
(This usually takes 2 to 10 minutes depending on your network)

* Download base image: `vagrant box add hashicorp/precise32`
* `cd method1`
* `vagrant up`

Method 2: Use our pre-built box

* `cd method2`
* Download pre-built image [workshop.box](https://www.dropbox.com/s/qp3jwxttg22akem/workshop.box?dl=0) to current folder: Also to be released over workshop via USB stick.
* `vagrant box add workshop.box --name workshop`
* `vagrant up`

## Setup GraphLab: 

Method1: Building from scratch:

* Download base image: `vagrant box add hashicorp/precise32`
* `cd graphlab`
* `vagrant up`

Method2: Copy the image+Vagrantfile from our USB sticks and do `vagrant up`.

## Next

Enjoy testing those platforms during the workshop


