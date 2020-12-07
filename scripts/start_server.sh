cd /home/ubuntu/ctni
nohup gunicorn --bind 0.0.0.0:8000 wsgi > /home/ubuntu/output.txt 2> /home/ubuntu/erro.txt &