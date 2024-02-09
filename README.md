# LocalChatMessenger
ローカルシステム上でクライアントサーバシステムで動作するメッセージ送信システムです。

## 詳細
クライアント側：入力されたテキストメッセージをサーバ側に送信する
サーバ側：：クライアントからのメッセージを受け取り、fakerで生成された文章をクライアントに送り返す

## 開発環境
VirtualBox
Ubuntu 23.10
※Fakerモジュールをインストールするため、実行時はpython venvの環境をを使用しております

## 使用モジュール
Faker 0.7.4
