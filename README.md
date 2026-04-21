# 机器人控制管理系统

当前仓库为父仓库，负责聚合公共文档、公共工具，以及 4 个子仓库：

- `repos/robot-cloud`：云端前后端
- `repos/robot-onboard`：机器狗本体端
- `repos/robot-phone`：手机端
- `repos/robot-pc`：电脑端工作站

## 目录结构

```text
robot-system/
  docs/
  tools/
  repos/
    robot-cloud/
    robot-onboard/
    robot-phone/
    robot-pc/
```

## 首次拉取

```bash
git clone --recurse-submodules git@github.com:sakurakugu/robot-system.git
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

如果你希望直接把 4 个子仓库都更新到各自当前分支的最新提交：

```bash
git submodule update --remote --merge
```

## 详细说明

详细操作说明见：

- `docs/2. 应用程序目录结构.md`
- `docs/3. 子仓库与拉取说明.md`
- `docs/4. 全端链路流程图.md`

## 其他

该仓库是拆分自 https://github.com/sakurakugu/Robot-System-Old 仓库（已归档）。
然后如果提交消息是 `重构: [xxx] xxx`, `新增: [xxx] xxx` 这种，而不是 `重构: xxx`, `新增: xxx` 这种， 就是从旧仓库迁移过来的。
