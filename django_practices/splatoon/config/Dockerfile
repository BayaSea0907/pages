# Dockerfileのimage化:
# $ docker buildx build ./config/ -t postgres
# (Usage: docker buildx build [OPTIONS] PATH | URL | -)
#
# コンテナの起動:
# $ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
# (Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...])
#
# コンテナにアクセス:
# (Usage:  docker exec [OPTIONS] CONTAINER COMMAND [ARG...])
# $ docker exec -it CONTAINER_ID /bin/bash -c "su - postgres"

# ベースイメージ: PostgreSQLの公式イメージ
# https://hub.docker.com/_/postgres
# 19ce210d1d51
# `su - postgres` でデフォルトで用意されているユーザーに切り替え（switch user）可能
FROM postgres:18.4

# ============================
# PostgreSQLの勉強メモ
# ============================
#
# データベース一覧:
# select datname from pg_database;
# =>  datname  
#    -----------
#     postgres
#     splatoon
#
# ---------------------------------------------------------------
# psql メタコマンド一覧
# ---------------------------------------------------------------
# コマンド | 正式名称 (由来)       | 役割
# ---------+-----------------------+----------------------------------------------
# \l       | List databases        | データベースの一覧を表示する
# \c       | Connect               | データベースへ接続（切り替え）する
# \d       | Describe              | テーブル定義（列名、型など）を表示する
# \dt      | Display Tables        | テーブルの一覧を表示する
# \di      | Display Indexes       | インデックスの一覧を表示する
# \dv      | Display Views         | ビューの一覧を表示する
# \ds      | Display Sequences     | シーケンス（連番生成器）の一覧を表示する
# \du      | Display Users         | ユーザー（ロール）の一覧を表示する
# \dn      | Display Namespaces    | スキーマの一覧を表示する
# \q       | Quit                  | psqlを終了する
# \?       | （記号）               | メタコマンドの全一覧を表示する
# \h       | Help                  | SQL文の使い方のヘルプを表示する（例：\h SELECT）
# ---------------------------------------------------------------