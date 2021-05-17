#InterSystems IRIS の Python Native APIを使ってみよう
######################################
#[1] irisnative パッケージのインポート
#[2] IRISに接続＋IRISオブジェクトの作成
#[3] ^Correlationの作成
#[4] [3]で設定した値の取得
######################################

def getCorrelation(source,count):
    if count>3:
        return
    print("\n",source, " の関係者を探します")
    iter = iris_native.iterator("Correlation",source)
    nodelist=[source for source in iter.subscripts() ]
    edgelist=[(source,target) for target in nodelist]
    #表示用
    for edge in edgelist:
        print("  関係者：",edge[1])

    for target in nodelist:
        getCorrelation(target,count+1)

#[1] irisnative パッケージのインポート
import irisnative

#[2]IRISに接続＋IRISオブジェクトの作成
connection = irisnative.createConnection("localhost",1972,"user","_system","SYS")
iris_native = irisnative.createIris(connection)

#[3] 登場人物の登録
#   set ^Correlation("Eren")="主人公（エレン）
iris_native.set("主人公（エレン）","Correlation","Eren")
iris_native.set("エレンの幼馴染（アルミン）","Correlation","Armin")
iris_native.set("エレンの幼馴染（ミカサ）","Correlation","Mikasa")
iris_native.set("エレンのお父さん（グリシャ）","Correlation","Grisha")
iris_native.set("エレンの異母兄弟（ジーク）","Correlation","Zeke")
iris_native.set("鎧の巨人（ライナー）","Correlation","Reiner")
iris_native.set("超大型の巨人（ベルトルト）","Correlation","Bertolt")
iris_native.set("エレンのお母さん（カルラ）：ダイナに捕食","Correlation","Carla")
iris_native.set("ジークのお母さん（ダイナ）：レイス王家[フリッツ家]","Correlation","Dina")
iris_native.set("人類最強の兵士（リヴァイ）","Correlation","Levi")

#関係性を設定
#   set ^Correlation("Eren","Mikasa")=""
iris_native.set(None,"Correlation","Eren","Mikasa")
iris_native.set(None,"Correlation","Eren","Armin")
iris_native.set(None,"Correlation","Armin","Mikasa")
iris_native.set(None,"Correlation","Mikasa","Armin")
iris_native.set(None,"Correlation","Armin","Eren")
iris_native.set(None,"Correlation","Mikasa","Eren")
iris_native.set(None,"Correlation","Grisha","Eren")
iris_native.set(None,"Correlation","Grisha","Zeke")
iris_native.set(None,"Correlation","Eren","Zeke")
iris_native.set(None,"Correlation","Zeke","Eren")
iris_native.set(None,"Correlation","Grisha","Dina")
iris_native.set(None,"Correlation","Dina","Grisha")           
iris_native.set(None,"Correlation","Grisha","Carla")
iris_native.set(None,"Correlation","Carla","Grisha")
iris_native.set(None,"Correlation","Dina","Carla")
iris_native.set(None,"Correlation","Armin","Bertolt")
iris_native.set(None,"Correlation","Reiner","Bertolt")
iris_native.set(None,"Correlation","Bertolt","Reiner")
iris_native.set(None,"Correlation","Levi","Zeke")

#[4] 全件取得
for source,value in iris_native.iterator("Correlation"):
    print(source,"-",value)

    for target,value in iris_native.iterator("Correlation",source):
        print("  関係者：",target)

#[5] 登場人物を特定して関係者取得
print("\n******************************")
print("Leviに関連する人物を探します")
print("******************************")
getCorrelation("Levi",1)
#接続終了
connection.close()