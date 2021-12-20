set -e
mkdir -p $PWD/data

docker build -q . -t otodom > /dev/null
docker run -v ${PWD}/data:/var/app/data otodom:latest python3 main.py

echo "Fresh links are below"
echo "-----------------------------------"
cat data/fresh.txt