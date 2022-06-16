#!/bin/bash

cd blog_admin && python3 get_blog_data
cp -r blog_data ../blog_frontend/ && cd ../blog_frontend/ && npm run build
cp -r dist/* ../yhw-miracle.github.io/

