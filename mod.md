<IfModule mod_wsgi.c>
	<Directory /var/www/vhosts/blog.tomware.it/httpdocs/app>
		Require all granted
	</Directory>

	<Directory /var/www/vhosts/blog.tomware.it/httpdocs/app/static>
		Require all granted
	</Directory>

    <Directory /var/www/vhosts/blog.tomware.it/httpdocs/app/templates>
		Require all granted
	</Directory>


    <Directory /var/www/vhosts/blog.tomware.it/httpdocs/app/blueprints>
		Require all granted
	</Directory>

	WSGIScriptAlias /app /var/www/vhosts/blog.tomware.it/httpdocs/app/app_wsgi.py
	WSGIDaemonProcess blog user=u_blog group=psacln processes=2 threads=10 python-home=/var/www/vhosts/blog.tomware.it/venv-blog

	WSGIProcessGroup blog
	WSGIApplicationGroup %{GLOBAL}

</IfModule>