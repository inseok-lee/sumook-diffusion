# Diffusion text-to-image  
- [한국 전통 수묵화 화풍별 제작 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71380)으로 학습한 Diffusion text-to-image 모델
- [Huggingface Diffusers Library](https://github.com/huggingface/diffusers)
- Inference with streamlit
  
## Default working directory
contrainer 생성시 기본 WORKDIR는 /root 이다. 프로젝트는 이 root 폴더 내에서 진행된다.  

## Prepare python environment 
1. contrainer 생성
```shell
docker run -dit -p {ex-port}:{in-port} --gpus all --shm-size=16G --name {name} pytorch/pytorch:2.1.0-cuda11.8-cudnn8-devel
```
  
2. 리눅스 패키지 설치
```shell
apt update
apt install -y git
```
  
3. Git clone
```shell
git clone https://github.com/inseok-lee/sumook-diffusion.git
cd sumook-diffusion
```
  
4. Conda 가상환경 생성
```shell
conda create -n diffusion python=3.10
conda init
source ~/.bashrc
conda activate diffusion
```
  
5. 파이썬 패키지 설치
```shell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install --upgrade diffusers[torch]
pip install -r requirements.txt
```
  
6. huggingface login
huggingface에 로그인 후 access token 준비  
```shell
huggingface-cli login
```
  
## Generate Sumook Painting example with streamlit
```shell
cd app
streamlit run Home.py --server.port={port}
```