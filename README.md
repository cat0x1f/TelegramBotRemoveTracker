# TelegramBotRemoveTracker

一个电报的 bot，用于在分享链接的时候防止被追踪。比如，想要分享一个带追踪的链接到某频道时，可以通过先分享到此 bot，再由这个 bot 发送到频道，这样，发送到频道里的链接便是不带追踪的了。


## 直接运行

### 依赖

```bash
pip install pyTelegramBotAPI
```

### 运行

```bash
python3 main.py yourtoken
```

## 使用 Docker

### 拉取

```bash
docker pull ghcr.io/cat0x1f/telegrambotremovetracker:main
```

### Docker 运行

```bash
docker run --env BOTTOKEN=yourtoken ghcr.io/cat0x1f/telegrambotremovetracker:main
```

其中的 `yourtoken` 为从 @BotFather 获取的令牌。
