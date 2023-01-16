---
title: Hexo 快速开始
date: 2023-01-16 13:21:23
tags:
- blog
---

## 环境

在以下环境中部署:
系统: ubuntu 20.04
编辑器: WebStorm
node: v16.18.0
npm: v8.19.2

## 安装

```bash
# 全局安装hexo-cli 命令行工具
npm install -g hexo-cli
# 当前目录下初始化项目
hexo init
```

初始化的目录必须是一个空目录

## 创建新页面

文件名参考jekyll和VuePress的推荐格式, year-month-day-title.
修改`_config.yml`配置项, 使创建的文件名为上述格式:
```yaml
# 设置文件名格式
new_post_name: :year-:month-:day-:title.md
# 启用资源文件夹,方便以后copy, 不启用
# post_asset_folder: true
```
图片资源采用全局文件夹的形式,采用资源文件夹形式,主页上会请求不到资源,需要到具体页面里才能正常显示.
图片资源目前按年划分,正常应该也不会很多.

```bash
hexo new "Hexo quick start"
```

然后填写正文内容

## 配置文件
以下配置优先级从高到低, 高优先级覆盖低优先级.
1. `_config.yml`项目配置文件 
2. `_config.<theme_name>.yml`项目的主题配置文件
3. `themes/<theme_name>/_config.yml`主题默认配置文件

修改`_config.<theme_name>.yml`配置,需要重启服务才能生效

## 使用next主题
https://github.com/theme-next/hexo-theme-next
[next 主题设置教程](https://theme-next.js.org/docs/theme-settings/)
```bash
cd <hexo project>
# 这个部署方式容易出问题, 适合主题开发人员用, 采用npm部署
git clone https://github.com/theme-next/hexo-theme-next themes/next
# 采用npm安装主题
npm install hexo-theme-next
```

编辑`_config.yml`
```yml
theme: next
```
next的主要用法看`themes/next/_config.yml`里面的内容


## 本地测试

```bash
# 本地运行服务器
hexo server
```

## 一键部署到 github pages

修改`_config.yml`, 使支持一键部署到github

```bash
# Deployment
## Docs: https://hexo.io/docs/one-command-deployment
deploy:
  type: 'git'
  repo: 'git@github.com:eleksbai/eleksbai.github.io.git'
  branch: gh-pages
```

执行命令`hexo clean && hexo deploy`部署github上.

调整github项目下的page设置, 是github page显示的内容指向`gh-pages`分支,
Project(***.github.io) >> Settings >> Pages >> Branch >> gh-pages

## github.io项目从jekyll迁移到hexo

通过以下步骤完成博客框架的迁移:

1. 从github拉取***.io项目.
2. 在一个项目的目录创建新文件夹, 并初始化hexo项目.
3. 将***.io项目中_post文件的内容复制到hexo项目source/_posts下
4. 将***.io项目清空,仅留下.git目录
5. 将hexo项目内容完成复制到***.io目录下.

## 参考

[Documentation | Hexo](https://hexo.io/docs/)
