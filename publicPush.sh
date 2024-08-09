python3 setup.py build_ext --inplace

docker compose up -d

rm -rf build ./**/*c ./**/*py
