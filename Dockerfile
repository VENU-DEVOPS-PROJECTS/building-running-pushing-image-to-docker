FROM python:3
ADD clock-script.py /
CMD ["python","./clock-script.py"]
