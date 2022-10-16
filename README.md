<!-- # COVID Scouter 
## Pre-requisite
0. Check vid [HERE]()
1. Download Anaconda from the [Anaconda Site](https://www.anaconda.com/products/distribution)
2. Install Anaconda (Don't forget to include PATH in Setting)
3. Open Anaconda Prompt and create your own Anaconda Environment
    - conda env create -f environment.yml
4. Get the Twitter API Key from [HERE](https://developer.twitter.com/en/portal/dashboard)

## Set Up 

2. Download Git Repository or using Git Clone to download the file 
3. Change the config.ini file to be your api in YOUR FIELD
4. Open folder on your CMD location
5. On your terminal/command line type
    - conda activate  -->

# 前提条件

0. 動画で確認 [HERE]()
1. Anaconda をダウンロード [Anaconda Site](https://www.anaconda.com/products/distribution)
2. Anacanda をインストール  (環境変数の追加を忘れないでください)
3. Anaconda Prompt を開き、Anaconda Environmentを作成
    - conda create -n twitter-api-test
4. Twitter API key を取得 [リンク](https://developer.twitter.com/en/portal/dashboard)

# セットアップ 

2. Git リポジトリのダウンロードもしくはgit cloneでファイルをダウンロード
3. `config.ini`をYOUR FIELDのapiに変更
4. コマンドライン上でダウンロードしたフォルダを開く
5. コマンドライン上で以下を実行
    - ``` conda activate twitter-api-test ```
    - ``` pip install tweepy pandas configparser ```

# pythonファイルのメンテ

## 設定ファイル
1. `config_template.txt`をコピーしてconfig.iniを作成
2. `config.ini`に取得したtwitterAPIのAPIkey情報を入力

## キーワード設定
* リスト ```search_words```の要素を追加、削除することで検索キーワードを変更できる  
検索キーワードのフォーマット  
　 ``` [キーワード] min_faves:[最小いいね数] until:[検索終了日] since:[検索開始日]  ```  
　例：```コロナ min_faves:100 until:2022-9-27 since:2022-09-20```

## 保存ファイル名設定
* 変数```file```の文字列を変更することで保存するファイル名を変更できる
