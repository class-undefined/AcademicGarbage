#!/bin/sh
source ~/.bashrc
source ~/.zshrc

# 安装nvm(node管理工具)
setup_nvm() {
    if [ -z $NVM_DIR ];then
        echo "⛏ 没有找到nvm管理工具, 准备安装..."
        bash -c "$(curl -fsSL https://gitee.com/RubyKids/nvm-cn/raw/master/install.sh)"
        source ~/.bashrc
        source ~/.zshrc
        if [ -z $NVM_DIR ];then
            echo "⚠️ nvm安装失败"
            exit
        else
            echo "🚀 nvm安装成功, path: $NVM_DIR"
            return
        fi
    else
        echo "✅ 找到nvm管理工具, path: $NVM_DIR"
        return
    fi
    return
}

# 使用指定node版本 use_node <node_version>
use_node() {
    _NODE_VERSION=$1 # 第一个参数为使用指定的node版本
    CUR_NODE_VERSION=$(node -v) # 获取当前node版本
    echo "🔦 所需node版本: $_NODE_VERSION, 当前node版本为$CUR_NODE_VERSION"
    if [ $CUR_NODE_VERSION = $_NODE_VERSION ];then
        echo "✅ node版本一致"
    else
        echo "⛏  node版本不一致, 准备安装指定版本"
        NVM_NODEJS_ORG_MIRROR=https://npmmirror.com/mirrors/node nvm install $_NODE_VERSION
        nvm alias default $_NODE_VERSION
        if [ $(node -v) = $_NODE_VERSION ];then
            echo "🎉 安装node $_NODE_VERSION成功~"
        else
            echo "⛈ 安装node $_NODE_VERSION失败"
            exit
        fi
    fi
    npm config set registry https://registry.npmmirror.com # npm切换国内源
}

# 安装依赖 install
install() {
    echo "⚙️ 准备安装nvm (node管理工具)..."
    setup_nvm
    NODE_VERSION=v16.14.2 # 指定node版本
    use_node $NODE_VERSION
    echo "⚙️ 准备安装pnpm..."
    npm install pnpm -g
    echo "⚙️ 更换pnpm镜像源为: https://registry.npmmirror.com"
    pnpm config set registry https://registry.npmmirror.com
    echo "🛫 nodejs安装完毕, 请另开终端输入\"node -v\" 查看能否输出node版本号以确认是否安装成功"
}
install