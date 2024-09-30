# 環境構築手順

このプロジェクトでは、`pipenv`を使用してPythonの仮想環境を管理します。以下の手順に従って環境を構築してください。

## 前提条件

- Python3.11がインストールされていること
- `pip`がインストールされていること

## 手順

1. **pipenvのインストール**

    ```sh
    pip install pipenv
    ```

2. **仮想環境**

    ```sh
    pipenv --python 3.11
    ```

3. **仮想環境の作成と依存関係のインストール**

    ```sh
    pipenv install
    ```
    または
    ```sh
    pipenv -r install ./requrements.txt
    ```

4. **仮想環境のアクティベート**

    ```sh
    pipenv shell
    ```

5. **依存関係の追加**

    新しいパッケージを追加する場合は、以下のコマンドを使用します。

    ```sh
    pipenv install <パッケージ名>
    ```

6. **仮想環境のデアクティベート**

    仮想環境を終了する場合は、以下のコマンドを使用します。

    ```sh
    exit
    ```

7. **仮想環境の削除**

    仮想環境を削除する場合は、以下のコマンドを使用します。

    ```sh
    pipenv --rm
    ```

## 注意事項

- `Pipfile`と`Pipfile.lock`はプロジェクトのルートディレクトリに配置してください。
- 依存関係を更新する場合は、`pipenv update`を使用してください。

以上で環境構築は完了です。

## 利用方法


1. **スクリプトの実行**

    仮想環境内でスクリプトを実行するには、以下のコマンドを使用します。

    ```sh
    pipenv run python <スクリプト名>.py produce
    ```

    ```sh
    pipenv run python <スクリプト名>.py consume
    ```

    例:
    ```sh
    pipenv run python app.py produce
    ```

2. **特定のコマンドの実行**

    仮想環境内で特定のコマンドを実行するには、以下のコマンドを使用します。

    ```sh
    pipenv run <コマンド>
    ```

    例:

    ```sh
    pipenv run pytest
    ```
