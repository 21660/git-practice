"""Git 练习项目的演示程序。

刻意保持简单：这里只用一个 TodoList 来说明"代码会被反复修改"这件事，
从而让 Git 的每一次提交都有实际内容可记录。
"""


class TodoList:
    def __init__(self):
        self.items = []

    def add(self, title):
        self.items.append({"title": title, "done": False})
        return self.items[-1]

    def finish(self, index):
        self.items[index]["done"] = True

    def remove(self, index):
        return self.items.pop(index)

    def pending(self):
        return [it["title"] for it in self.items if not it["done"]]

    def summary(self):
        total = len(self.items)
        done = total - len(self.pending())
        return "已完成 %d / %d 项" % (done, total)


def main():
    todo = TodoList()
    todo.add("初始化 Git 仓库")
    todo.add("配置远程仓库")
    todo.add("完成分支实验")

    todo.finish(0)
    todo.finish(1)

    print("Git Practice Project")
    print("-" * 24)
    for i, item in enumerate(todo.items, 1):
        mark = "x" if item["done"] else " "
        print("[%s] %d. %s" % (mark, i, item["title"]))
    print("-" * 24)
    print(todo.summary())


if __name__ == "__main__":
    main()
