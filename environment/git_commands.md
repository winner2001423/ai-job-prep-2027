# Git 常用命令速查

## 基础操作
```bash
git init                    # 初始化仓库
git status                  # 查看状态
git add <file>              # 暂存单个文件
git add .                   # 暂存所有更改
git commit -m "msg"         # 提交
git log --oneline           # 查看简洁历史
git log --oneline --graph --all   # 查看分支图
git diff                    # 查看未暂存改动
git diff --staged           # 查看已暂存改动

# 分支
git branch                  # 查看分支
git switch -c feature       # 创建并切换分支
git switch main             # 切换到 main
git merge feature           # 合并 feature 到当前分支
git branch -d feature       # 删除分支
# 远程仓库
git remote -v                                        # 查看远程
git remote add origin git@github.com:user/repo.git   # 关联远程
git push -u origin main                              # 首次推送
git push                                             # 后续推送
git pull                                             # 拉取
git clone git@github.com:user/repo.git               # 克隆
# 回退与撤销
git reset --hard HEAD^      # 回退到上一个提交
git reset --soft HEAD^      # 回退但保留改动
git revert <commit>         # 生成一个反向提交
git reflog                  # 查看所有操作记录
git checkout -- <file>      # 撤销工作区改动
git restore <file>          # 新版撤销命令
#ssh配置
~/.ssh/config:
Host github.com
  HostName ssh.github.com
  Port 443
  User git
#测试ssh
ssh -T git@github.com