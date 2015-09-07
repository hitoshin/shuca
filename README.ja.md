Shuca
====

## 概要
Shuca （朱夏）は自動要約プログラムです。2015年9月7日時点では単一文書要約のみに対応しています。

## 特徴
* Shuca は単一文書要約をナップサック問題とみなしています。

## 必要なツール
Shuca は JUMAN と KNP による前処理が行われた入力ファイルを想定しています。

* [JUMAN Ver.7.01](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN)
* [KNP Ver.4.14](http://nlp.ist.i.kyoto-u.ac.jp/index.php?KNP)

Shuca そのものは Python 2.7.10 で開発されています。

## インストール
特にインストールのための作業は必要ありません。内容物を適当なディレクトリに置いてください。

## 使い方
dic ディレクトリにサンプルファイルが含まれています。 `sample.snt.txt` は文分割済みの文書ファイル、 `sample.knp.txt` は当該ファイルを juman および knp で解析した後のファイルです。このファイルを以下のように実行してください。

    $ ./lib/Shuca.py < ./dat/sample.knp.txt


## 開発者
[hitoshin](https://github.com/hitoshin)
