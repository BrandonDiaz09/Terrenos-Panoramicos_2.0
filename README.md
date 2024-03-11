# TerrenosPanoramicos
Proyecto del desarrollo de una aplicación de consultas de terrenos

### Server Restart Guide
To effectively restart your web server, consider following these general steps based on the operations you've been performing. This guide assumes you are using a Linux-based environment, Gunicorn to run Django web applications, Nginx as a web server/reverse proxy, and systemctl to manage services.

1. **Activate the virtual environment**:
   - Make sure you are in the directory where your virtual environment is located. If in doubt, you can use the command `source ~/venv/bin/activate` to activate the virtual environment.

2. **Update the code (optional)**:
   - If you need to update your code from a Git repository, use `git pull origin master` or change `master` to the specific branch you need to update.

3. **Install dependencies (optional)**:
   - If there are changes in dependencies, run `pip3 install -r requirements.txt` to ensure all necessary dependencies are installed.

4. **Run migrations**:
   - To apply migrations to your database, use `python3 manage.py migrate`.

5. **Collect static files**:
   - Use `python3 manage.py collectstatic --noinput` to collect the necessary static files for your project.

6. **Restart Gunicorn**:
   - If you are managing Gunicorn with a systemd service, you can use `sudo systemctl restart gunicorn.service` to restart the Gunicorn service.

7. **Restart Nginx (optional)**:
   - If you have made changes that affect Nginx, or just as a precautionary measure, you can restart Nginx with `sudo systemctl restart nginx`.

