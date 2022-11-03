# ! Don't install the version alpine that cause many difficult

# * However, some teams are moving away from alpine because these images can cause
# * compatibility issues that are hard to debug. Specifically, if using python
# * images, some wheels are built to be compatible with Debian and will
# * need to be recompiled to work with an Apline-based image.

FROM redis:7.0.5
WORKDIR /redis
#COPY redis.conf ./redis.conf
COPY . .
CMD [ "redis-server", "./redis.conf" ]