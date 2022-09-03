cd "$(dirname "$0")"

bash ./build_documentation.sh
bash ./compile_for_pypi.sh
