# 机器人控制管理系统

当前仓库为父仓库，负责聚合公共文档、公共工具，以及 3 个子仓库：

- `repos/robot-cloud`：云端前后端
- `repos/robot-onboard`：机器狗本体端
- `repos/robot-phone`：手机端

## 目录结构

```text
robot-system/
  docs/
  tools/
  repos/
    robot-cloud/
    robot-onboard/
    robot-phone/
```

## 首次拉取

```bash
git clone --recurse-submodules <robot-system 仓库地址>
cd robot-system
```

如果你已经拉了父仓库，但还没初始化子模块：

```bash
git submodule update --init --recursive
```

## 日常更新

只同步父仓库记录的子模块版本：

```bash
git pull
git submodule update --init --recursive
```

如果你希望直接把 3 个子仓库都更新到各自当前分支的最新提交：

```bash
git submodule update --remote --merge
```

## 详细说明

详细操作说明见：

- `docs/3. 子仓库与拉取说明.md`
