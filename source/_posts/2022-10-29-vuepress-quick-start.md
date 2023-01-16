---
title: VurPress 快速开始
date: 2022-10-29
author: eleksbai
tags:
 - vuepress
location: Hangzhou
--- 

## 基础环境 nodejs 环境搭建

在ubuntu20.04下搭建vuepress开发环境.

```shell
# 系统 ubuntu 20.04
sudo apt install nodejs
sudo apt install npm
cnpm install -g vuepress
```

hyman@hyman-MS-7A37:~$ node -v
v10.19.0
hyman@hyman-MS-7A37:~$ npm -v
6.14.4

#### cnpm 包

```shell
sudo npm install -g cnpm --registry=https://registry.npmmirror.com
cnpm install --global yarn
sudo ln -s /opt/programs/nodejs/node-v16.17.1-linux-x64/bin/yarn /usr/local/bin/yarn
yarn config set registry https://registry.npmmirror.com
```

淘宝npm启用新域名了
https://developer.aliyun.com/article/801032

包管理还是应该使用yarn， 不然很可能使用的时候部署不起来

## 配置 docs/.vuepress/config.js

教程1中建议对配置进行切分， 我这里建议不需要。
这种东西等需要再去搞，而且大多数人等不要需要的哪个时候。
早期阶段保持简单即可。

## 插件安装

```shell
cnpm install @vuepress/plugin-back-to-top
cnpm install @vuepress/plugin-pwa
```

## 评论系统 vssue

[码云配置](https://vssue.js.org/guide/gitee.html)
[vuepress 配置](https://vssue.js.org/guide/vuepress.html#vuepress-plugin)
[评论系统demo](https://gitee.com/meteor_lxy/vssue-demo)
[码云第三方应用文档](https://gitee.com/api/v5/oauth_doc#/)
结合码云试试看， 不行以后切成gitee

```
cnpm install @vssue/vuepress-plugin-vssue
cnpm install @vssue/api-gitee-v5

# secret_example.js

```

配置平台密钥
secret.js

```js
const vssue_gitee ={
    platform: 'gitee',
    // all other options of Vssue are allowed
    owner: 'eleksbai', // 码云的用户名
    repo: 'blog', // 码云的仓库名
    clientId: 'YOUR_CLIENT_ID',
    clientSecret: 'YOUR_CLIENT_SECRET',
}
module.exports = {
    "vssue": vssue_gitee
}
```

在配置文件中引入
docs/.vuepress/config.js

```js
const secret =  require("./secret");
const vssue = secret.vssue
module.exports = { 
    // ....
    plugins:
        {
            '@vssue/vuepress-plugin-vssue': {
                // set `platform` rather than `api`
                platform: vssue.platform,
                owner: vssue.owner,
                repo: vssue.repo,
                clientId: vssue.clientId,
                clientSecret: vssue.clientSecret,
            },
            '@vuepress/back-to-top':{}
        },
    // ...
}
```

## 自动侧边栏

方便管理文章
[Vuepress Plugin Auto Sidebar](https://shanyuhai123.github.io/vuepress-plugin-auto-sidebar/zh/)

```shell
yarn add -D  vuepress-plugin-auto-sidebar
```

## 参考

1. [一个比较详细的建站过程（看到一半需要关注公众号才可以继续）](https://coder.itclan.cn/fontend/tools/vuepress-build-blog/#%E5%B1%95%E7%A4%BA%E6%AF%8F%E4%B8%AA%E9%A1%B5%E9%9D%A2%E7%9A%84%E4%BE%A7%E8%BE%B9%E6%A0%8F)
2. [官方文档中文版](https://www.vuepress.cn/guide/) 

