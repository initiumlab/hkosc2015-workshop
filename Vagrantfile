# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "hashicorp/precise32"
  
  # config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  
  config.vm.network "private_network", ip: "192.168.33.11"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  
  config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", privileged:false, inline: <<-SHELL 
    sudo apt-get -y update
  #   sudo apt-get install -y apache2
	sudo apt-get -y install openjdk-7-jdk
	wget http://ftp.cuhk.edu.hk/pub/packages/apache.org/spark/spark-1.3.1/spark-1.3.1-bin-hadoop2.6.tgz
	tar -zxf spark-1.3.1-bin-hadoop2.6.tgz
	ln -s spark-1.3.1-bin-hadoop2.6 spark

    # === Hadoop 2 setup ===


	#USER_HOME="/home/vagrant"
	wget 'http://apache.communilink.net/hadoop/common/hadoop-2.7.0/hadoop-2.7.0.tar.gz'
	tar -xzvf hadoop-2.7.0.tar.gz 

	export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-i386/jre/
	echo 'export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-i386/jre/' >> ~/.bashrc

	ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa
	cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
	export HADOOP\_PREFIX=/home/vagrant/hadoop-2.7.0
	ssh -o StrictHostKeyChecking=no localhost 'echo "ssh success"'

	cd hadoop-2.7.0

	cat << EOF > etc/hadoop/core-site.xml
<configuration>
<property>
<name>fs.defaultFS</name>
<value>hdfs://localhost:9000</value>
</property>
</configuration>
EOF

	cat << EOF > etc/hadoop/hdfs-site.xml:
<configuration>
<property>
<name>dfs.replication</name>
<value>1</value>
</property>
</configuration>
EOF

	./bin/hdfs namenode -format

	./sbin/hadoop-daemon.sh start datanode
	./sbin/hadoop-daemon.sh start namenode
	cd -

  SHELL
end
