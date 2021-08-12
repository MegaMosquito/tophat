
DOCKERHUB_ID:=ibmosquito
NAME:="tophat"
VERSION:="1.0.0"

default: build run

build:
	docker build -t $(DOCKERHUB_ID)/$(NAME):$(VERSION) .

dev: stop build
	docker run -it -v `pwd`:/outside \
	  --name ${NAME} \
	  --privileged \
	  -v /dev/spidev0.0:/dev/spidev0.0 \
	  -v /dev/spidev0.1:/dev/spidev0.1 \
	  $(DOCKERHUB_ID)/$(NAME):$(VERSION) /bin/sh

run: stop
	docker run -d \
	  --name ${NAME} \
	  --restart unless-stopped \
	  --privileged \
	  -v /dev/spidev0.0:/dev/spidev0.0 \
	  -v /dev/spidev0.1:/dev/spidev0.1 \
	  $(DOCKERHUB_ID)/$(NAME):$(VERSION)

test:
	@echo "test"

push:
	docker push $(DOCKERHUB_ID)/$(NAME):$(VERSION) 

stop:
	@docker rm -f ${NAME} >/dev/null 2>&1 || :

clean:
	@docker rmi -f $(DOCKERHUB_ID)/$(NAME):$(VERSION) >/dev/null 2>&1 || :

.PHONY: build dev run push test stop clean
