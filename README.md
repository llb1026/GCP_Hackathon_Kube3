# GCP Study Hackathon

## Kube3 팀

:sparkles: 김서준 / 이지윤 / 서준용 / 강홍석 / 주태영 :sparkles:

### Description

2018 Google Cloud Platform Study Jam Hackathon Project

### How to run

1. Clone this repository

```
$ git clone https://github.com/llb1026/GCP_Hackathon_Kube3.git
$ cd GCP_Hackathon_Kube3
```

2. Set up

```
$ pip install image
$ pip install tensorflow
$ pip install keras
```

3. Run

```
$ python3 main.py
```

then open http://127.0.0.1:5000

### How to deploy

GCR(Google Container Registry)에 넣기 위한 이미지 생성을 위해 사용 (cloud shell에서 도커 이미지를 구우면 너무 오래걸리더라구요)

```
# vm
gcloud docker -- push gcr.io/gdkim20180919/test:v1
# shell
gcloud docker -- pull gcr.io/gdkim20180919/test:v1
gcloud docker --help
gcloud docker -- pull gcr.io/gdkim20180919/test:v1
gcloud container clusters create hello-world \ --num-nodes 2 \ --machine-type n1-standard-1 \ --zone us-central1-f
gcloud container clusters create hello-world --num-nodes 2 --machine-type n1-standard-1 --zone us-central1-f
gcloud auth login
gcloud container clusters create hello-world --num-nodes 2 --machine-type n1-standard-1 --zone us-central1-f
kubectl run hello-node \ --image=gcr.io/gdkim20180919/test:v1 \ --port=5000
kubectl run hello-node --image=gcr.io/gdkim20180919/test:v1 --port=5000
kubectl expose deployment hello-node --type="LoadBalancer"
```

kubernetes 이슈는 사용자 인증 정보 json파일 다운로드 후 shell에서 업로드 하시면 됩니다 ㅎㅎ