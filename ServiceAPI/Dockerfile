#---------------------------------------------------------------------------
#
#
# 
#---------------------------------------------------------------------------

FROM python:3.8

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app/serviseAPI
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT [ "python", "manage.py" ]
CMD ["runserver", "0.0.0.0:8000"]
