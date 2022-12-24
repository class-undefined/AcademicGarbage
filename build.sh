docker build --no-cache -t academic_garbage_image .
docker run --gpus all -d -p 8000:8080 -p 5001:5001 --name academic_garbage academic_garbage_image
