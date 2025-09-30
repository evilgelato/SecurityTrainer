#!/usr/bin/env bash
set -e
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get -y upgrade
apt-get -y install python3 python3-pip netcat-openbsd curl ca-certificates
# Helpers: create a demo directory for serving/testing
mkdir -p /home/vagrant/www && chown -R vagrant:vagrant /home/vagrant/www
echo "Hello from target Ubuntu VM" > /home/vagrant/www/index.html
cat > /home/vagrant/start_listeners.sh <<'EOS'
#!/usr/bin/env bash
# Start a simple HTTP server on 8000 and a netcat listener on 9001
# Run this manually inside the VM for labs (foreground processes).
echo "Starting python3 -m http.server 8000 in /home/vagrant/www"
cd /home/vagrant/www && python3 -m http.server 8000 &
echo "Starting nc -l 9001"
nc -l -p 9001
EOS
chmod +x /home/vagrant/start_listeners.sh
echo "Provisioning complete. To start demo listeners: 'bash ~/start_listeners.sh'"
