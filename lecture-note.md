AWS로 이미지 업로드 서비스 만들어보기


참여조건
- AWS Free tier 계정 혹은 강의 시간동안 사용되는 요금을 스스로 부담
- 쉘을 사용할 수 있는 환경
	- bash를 기준으로 작업
	- zsh과 같은 다른 쉘을 사용하는 경우 진행 중 실행하는 명령어를 알아서 고쳐 써야 함
- ssh를 사용할 수 있는 환경
	- EC2에 ssh를 열 수 있어야 진행 가능
	- 우분투와 같은 리눅스 환경을 듀얼 부팅으로 설치해오거나 가상 머신으로 설치해올 것
	- 윈도우라면 putty 사용 혹은 윈도우 10 레드스톤부터 제공되는 리눅스 서브 시스템 업데이트를 해서 bash와 git을 사용 가능하게 준비할 것
- 아주 기본적인 수준에서의 vi 사용법 숙지
	- EC2에 ssh를 열어서 파일 수정을 할 수 있어야 함
- 웹 서비스 개발 환경 준비
	- 진행 중간 중간 스스로 프로젝트 상태 및 DB 확인을 위해 필요
	- 파이썬 IDE로 Pycharm, DB 툴로 MySQL Workbench를 추천하며, 그 외 emacs나 vi, mysql-cli와 같은 본인이 선호하는 툴이 있으면 대체 가능
		- Pycharm과 MySQL Workbench는 윈도우, 우분투에서 사용 가능하므로 추천


기능명세
- 이미지를 S3에 업로드
- 메인 페이지에서 최근 업로드된 이미지 순으로 리스트 보여줌
	- pagination 없이 그냥 최근 8개만 보여주기
- 데이터베이스는 RDS 사용


진행 순서
1. AWS에 대한 간략한 설명
	- EC2 개념
	- S3의 필요성
	- RDS의 필요성
2. EC2 인스턴스 생성
	- Region을 서울로 설정
	- AMI(Amazon Machine Image) 개념 설명, Ubuntu Server 16.04 LTS로 설정
	- Instance Type 개념 설명, t2.micro로 생성
	- Security Group 개념 설명, 추가할 port는 SSH, HTTP, Custom TCP Rule(테스트용, 8080)
	- EBS(Elastic Block Store) 개념 설명, 기본 사이즈인 8GB로 진행
		- 스냅샷
		- 다른 EBS로 바꿔 끼우기
	- Private Key File 개념 설명, 반드시 다운로드 후 권한 설정(chmod 0400 keyfile)
	- 생성 후 초기화 하는데 시간이 조금 걸림. 잠깐 휴식.
	- Public IP 설명 후, EC2 인스턴스 Stop, Start 하여 Public IP가 바뀌는 것 보여주고 Elastic IP 설정
3. EC2에 개발환경 설정
	- 필요한 패키지 설치
		- sudo apt-get update
		- sudo apt-get install git gcc make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils libxml2-dev libxslt1-dev python-dev uwsgi-plugin-python3
	- sudo service nginx start
	- pyenv 설치
		- git clone https://github.com/yyuu/pyenv.git ~/.pyenv
		- echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
		- echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
		- echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
	- python 3.4.3 설치, 이거 시간이 좀 걸리니까 따로 돌려놓고 브라우저로 nginx 기본 hello world 페이지 확인
		- pyenv install 3.4.3
		- pyenv global 3.4.3
	- 프로젝트 clone
		- pyvenv venv
		- source venv/bin/activate
		- pip install
		- git checkout helloworld
		- python server.py
		- 브라우저로 포트 번호(8080) 명시하여 접속 후 웹 애플리케이션의 hello world 페이지 확인
4. S3, RDS 설정
	- S3 bucket 생성
		- S3에 파일 올려보기
		- S3에 올린 파일 권한 수정
		- 서비스 로고를 S3에 있는 이미지의 링크로 변경하여 확인해보기
	- RDS 인스턴스 생성
		- 스크린샷 따라서 생성
		- MySQL Workbench로 접속 확인
			- Standard TCP로 endpoint 설정하고 username, password 입력
5. 서비스 세팅 후 확인
	- IAM로 Secret Key 획득
	- 설정 파일에 Secret Key 반영
	- uwsgi uwsgi.ini 으로 서버 다시 켜서 업로드 확인
	- nginx랑 uwsgi 연결
	- 80 포트를 통해 서비스 접근이 잘 되는 것 확인
	- 이미지 업로드하여 S3에 파일이 올라가고 RDS에 모델이 생성되는 것 확인
	- PROFIT!