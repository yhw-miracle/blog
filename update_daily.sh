#!/bin/bash

remove_dist() {
    cd yhw-miracle.github.io
    rm -rv css
    rm -rv editor-md
    rm -rv favicon.ico
    rm -rv images
    rm -rv index.html
    rm -rv js
    cd ..
}

# 更新 yhw-miracle
cd yhw-miracle && git checkout master && git commit -am "更新每日金句"
git push
cd ..

# 删除 yhw-miracle.github.io 旧文件
remove_dist

# 更新 blog_frontend 并打包
cd blog_frontend && npm run build && cp -r dist/* ../yhw-miracle.github.io/ && git checkout master && git commit -am "更新每日金句"
git push
cd ..

# 更新 yhw-miracle.github.io
cd yhw-miracle.github.io && git checkout master && git add . && git commit -m "更新每日金句"
git push
cd ..

# 更新主仓库
git add . && git commit -m "更新每日金句"
git push
