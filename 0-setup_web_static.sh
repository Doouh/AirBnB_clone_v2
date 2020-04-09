#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.
apt-get -y install nginx
mkdir -p /data/web_static/{shared,releases/test}
touch /data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -Rh ubuntu:ubuntu /data/*
sed -i '/server_name _;/a location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
service nginx restart
