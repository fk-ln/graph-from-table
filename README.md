##Numelody
CSVから取得したデータをいい感じで補正した後音階に当てはめてMIDIファイルに出力する。
Numerical  Melody的な感じで適当に付けてたけどそれっぽいのでそのまま採用

##使い方
numelody.pyをダウンロードして任意のフォルダに置く。
そのディレクトリにCSVファイルを作成し1列目に順に数値を入力して保存。正の数であれば上限も無いし小数でも大丈夫...なはず。
行名も列名も要らないです。
以下の通り実行するとmelody.midが作られます。
```python
python numelody.py (CSVファイル名)
```
###例
```
python numelody.py sample
```
リポジトリにあるsample.csvは東京都の新規感染者数の推移です。お試しにどうぞ。

##必要要件
-python 3.6.10
-pretty_midi 0.2.8
-pands 1.0.5

##その他
Windowsだとダブルクリックで普通にMIDIファイルが再生可能なはず。Macだと大変？
オンラインでMIDIからmp3，wavに変換するのあるのでその辺を使うのもありかも。

##作者
[fk-ln](https://github.com/fk-ln)