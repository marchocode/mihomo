# Clash-Merger
> Clash 多订阅合并器。

## Features

1. 自部署订阅合并工具
2. 默认使用 [Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules) 分流规则集
3. 一个链接包含所有订阅

## Get Start
创建一个配置文件 `config.yaml`.

```yaml
mihomo:
  # 可选的token配置，用户token,用于认证
  token: your_token_here (generate uuid here)
  # 配置多个订阅链接，必须要支持clash-verge
  subs:
    - name: "Main"
      url: https://xxxx
    - name: "Backup"
      url: https://xxxx
```

```sh
docker run -d --name clash-merger -p "8080:8080" marchocode/clash-merger:latest

# 获得你的订阅链接
http://ip:port/subs/<your_token_here>
```

## Links
- [Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules)
- [core](https://wiki.metacubex.one/)
- [OpenClash](https://github.com/vernesong/OpenClash)