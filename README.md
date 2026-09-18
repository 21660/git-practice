# Git Practice Project

用于《岗位实践》实验一（代码和项目管理软件）的 Git 练习仓库。

## 项目简介

这是一个刻意保持简单的演示项目，目的是把注意力放在 Git 的版本控制流程上，
而不是代码本身的复杂度。项目通过命令行完成本地仓库建立、文件提交、版本回退、
分支创建与合并、远程仓库同步等操作。

## 目录结构

```
git-practice/
├── README.md         项目说明
├── .gitignore        忽略规则
└── src/
    └── main.py       演示程序
```

## 实验目的

- 理解工作区、暂存区（Index）与版本库（Repository）三者之间的关系
- 掌握 commit / push / pull 等常用版本同步操作
- 掌握分支的创建、切换与合并
- 理解 Fork 与 Pull Request 的协作流程

## 运行方式

```bash
python src/main.py
```


## 运行与协作说明

本节内容直接在 GitHub 网页端编辑并提交，用于演示从远程仓库拉取更新的
`git pull` 操作。命令行下的版本记录与网页端的提交最终都汇合到同一个
`main` 分支上。
