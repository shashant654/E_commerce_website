# echo "BUILD START"
# python3.9 -m pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
# echo "BUILD END "

echo "BUILD START"

# Ensure pip is installed
python3.9 -m ensurepip
if [ $? -ne 0 ]; then
    echo "Failed to install pip"
    exit 1
fi

# Install requirements
python3.9 -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install requirements"
    exit 1
fi

# Collect static files
python3.9 manage.py collectstatic --noinput --clear
if [ $? -ne 0 ]; then
    echo "Failed to collect static files"
    exit 1
fi

echo "BUILD END"
