# 引き継ぎノート（新チャット用）

最終更新: 2026-09-22（セッション区切り時点）

## 最初に伝えること（新チャット冒頭にこのファイルのパスを渡せばOK）

```
C:\Users\User\claude_local\billboard-bgm-pipeline\HANDOFF.md を読んで、続きから進めて。
```

これだけで基本的に状況を再構築できるように書いています。加えて以下のメモリファイルも
自動で読み込まれるはずですが、念のため：
- `billboard-bgm-pipeline`（プロジェクト概要・ユーザーの好み）
- `billboard-bgm-lyrics-methodology`（歌詞執筆の手順）

## 締め切り

**9/26までにSunoでの生成を終わらせる必要あり**（ダウンロード数がリセットされる仕様のため）。
テーマ出し→歌詞→Suno生成、をこの日までに完了させることが最優先。

---

## 現在のリリース状況（001〜021）

| # | タイトル | 状態 |
|---|---|---|
| 001〜008 | （既存曲） | 配信済み・完了 |
| 009 しめきり | RouteNote: Album Details/Artwork/Manage Stores/日本語ローカライズ(アルバム)完了。UPC 5064115416649 |
| 010 停電 | 同上。UPC 5064115276007 |
| 011 夜食 | 同上。UPC 5063941679242 |
| 012 夜のベランダ | 同上。UPC 5064140646325 |
| 013 白い灯り | 同上。UPC 5064140424398 |
| 014 耳をふさいで | 同上。UPC 5064140115425 |
| 015 まどろみ | 歌詞/Style確定→Suno生成**完了**（2テイク） |
| 016 雨あがり | 同上、Suno生成**完了** |
| 017 終電 | 同上、Suno生成**完了** |
| 018 髪を乾かす夜 | 同上、Suno生成**完了** |
| 019 夜のお茶 | 同上、Suno生成**完了** |
| 020 栞 | 同上、Suno生成**完了** |
| 021 徹夜明け | 同上、Suno生成**開始済み**（完了確認は未確認） |

009〜014は全曲、**配信日 2026-10-05** で統一。RouteNoteのAlbum Details/Artwork/Manage Stores/
日本語ローカライズ(アルバムレベル)まで完了しているが、**Add Audio（音源アップロード）と
Track単位の日本語ローカライズは未着手**（ユーザーが音源を後でまとめてアップロードする方針のため）。

009〜021の全release docは `releases/00N-*.md` にあり、テーマ／情景／Style案／Suno入力
（歌詞・Style・Exclude Styles）が記載済み。

---

## 直近のペンディングタスク（優先順）

1. **022〜033の生成結果を確認**（Sunoライブラリで再生・採用テイク選定）— 2026-09-23に
   Chrome経由でSuno生成完了（詳細は下記「022〜033の進捗」参照）。021は完了確認未のまま。
2. **015〜021の生成結果を確認**（Sunoライブラリで再生・採用テイク選定）
3. 015〜033の歌詞をSuno採用テイクから確定 → ⑤〜⑩（mixdown/mastering/QC/export）
   → ⑪ジャケット生成 → RouteNote入稿（009〜014と同じ流れ）。タイトルは歌詞確定後に決定
   （022〜033は全曲「タイトル未定」のまま生成した。テーマ名を仮タイトルとしてSunoの
   曲名欄には入力済み）
4. 009〜014のAdd Audio（音源アップロード後）＋Track単位ローカライズ

## 022〜033の進捗（2026-09-22〜23）

テーマ出しはClaudeが一括提案→ユーザー承認という流れで進めた（通常の「1曲ずつ協働」
プロセスとは異なる進め方だったが、ユーザー承認済み）。`releases/022-*.md`〜`033-*.md`
に各曲のテーマ・Suno入力（歌詞・Style・Exclude Styles）を保存済み。

**Suno生成は全12曲完了**（Chrome経由、Voice: Tonarine、v6-wild）。誤操作で一部の曲は
2回クリックしてしまい4テイク生成されている（031, 033）が問題なし、採用テイク選定時に
選べばよい。

### 030の読み修正（2026-09-26）
「白湯」を誤って「はくゆ」と読んで歌詞に書いていたため、「さゆ」に修正して再生成した。
`releases/030-hakuyu-no-nukumori.md` は `030-sayu-no-nukumori.md` にリネーム済み（slugも
`sayu-no-nukumori`）。**Sunoライブラリには旧「はくゆ」版の「白湯のぬくもり」2テイクが
残っているので採用しないこと**（新しい「さゆ」版は同日生成の2テイク）。

### Suno投入時の注意点（新たに判明）
- **歌詞のUnicodeエスケープでタイポが起きやすい**（例: `へ`(へ)と`ぺ`(ぺ)、
  `ぼ`(ぼ)と`へ`(へ)の書き間違い）。「かんぺき」→「かんへき/かんへい」、
  「もういっぺん」→「もういっぱん/もういっぽん」、「ぼやける」→「へやける」など、
  複数曲で同じパターンのミスが発生した。投入後は必ず`[Chorus]`の出現回数と
  `innerText`全文を確認し、typoがあれば`find`→`triple_click`→`type`で修正。
- **triple_click修正後にカーソル位置がずれる問題**: 修正直後に`End`キーだけでは
  正しい位置に戻らないことがある（023で発生、Chorus以降がPreChorusの前に
  挿入されてしまった）。修正後は必ずJSで文末にカーソルを移動させてから続きを入力する：
  ```js
  const el = document.querySelector('[contenteditable=true]');
  el.focus();
  const range = document.createRange();
  range.selectNodeContents(el);
  range.collapse(false);
  const sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  ```
- **元の歌詞ファイルに含まれるタイポ**: 022〜031のテーマ出し時点の歌詞に「ぶたくらを」
  「ですって」「わくがく」「つなぎたま」等の誤字があった。Suno投入前に文脈から判断して
  修正（「ふとんを」「かいで」「りんかく」「つなぎたまま」）。releases/*.mdのファイル
  自体は未修正のまま残っているので、歌詞確定時にファイルも合わせて修正すること。
- **「作成」ボタンクリックが反映されないことがある**: クリック後5秒待っても生成リストに
  出てこない場合、もう一度クリックが必要なことがある（ボタンの状態変化を見落としやすい）。
  誤って2回押すと同じ曲が2セット（4テイク）生成されるが実害はない。
- **Voice選択モーダルが誤って開くことがある**: スクロール位置によっては歌詞欄のつもりで
  クリックした座標が実際には別の要素（Voiceカードなど）に当たり、モーダルが開いて
  入力操作が全て無効になることがある（030で発生、歌詞が反映されずVoiceモーダルの中で
  操作していた）。歌詞入力前に必ずJSで`document.activeElement === contenteditable要素`
  を確認してからtype/deleteすること。
- **Chrome拡張機能が一時的に切断されることがある**（"Claude in Chrome is not connected"）。
  数秒待って`screenshot`等を再試行すれば復旧する。

---

## RouteNote入稿の重要な落とし穴（009〜014で判明・必読）

RouteNoteは激しくクセのあるUIで、素直にクリックするだけでは動かない箇所が多数ある。
以下は全て実際にハマった問題と解決策：

### 基本フロー
1. `https://www.routenote.com/rn/create_album` でタイトル入力→Create Release → UPC付きURLへ遷移
2. `https://www.routenote.com/rn/editalbum/<UPC>` でAlbum Details入力
3. `https://www.routenote.com/rn/addart/form/<UPC>` でジャケットアップロード
4. `https://www.routenote.com/rn/addstore/form/<UPC>` でManage Stores
5. `https://www.routenote.com/rn/localisation_hub/<UPC>` で日本語ローカライズ

### Album Detailsの罠
- **Cover Versionsのcheckbox「No」は `id="No3"`**。`id="No"`はCompilation Album用で紛らわしい。
  間違えると「Missing Information: cover version」エラーで保存できない。
- **Originally Released Date（アルバム個別発売日）を未来日付にすると保存時エラー**
  （"Originally Released field is required!"）。**今日の日付**を入れること（空欄も不可）。
  Sales Start Dateは将来日（配信解禁日）でOK。
- **Artist Name欄はSpotifyの既存アーティストをautocomplete候補として勝手に選択してしまう
  バグがある**（別人の名前・followers付きカードに変わる）。直後に他の操作を挟まず
  即座に「Save and Continue」を押すか、ズレたら "Change" リンクで戻してtextboxに戻し
  再入力する。
- **Composer/Lyricistの空の追加行（2人目欄）を削除すると、隠しフィールド
  `composer_value`/`lyricist_value`/`contributors_role`/`contributors_name` が
  「姓」と「名」を別人として分割保存してしまうバグがある**（例: composer_value="Yuki,,"
  composer2_value="Nishikawa,,"）。空行削除後は必ずJSで直接
  `composer_value = "Yuki,Nishikawa,"` のように結合し直す。
- ジャンルやExplicit Contentなどのカスタムドロップダウン欄は、クリックしても
  `document.activeElement`にフォーカスが乗らないことがある（1回失敗したら同じ座標で
  もう一度クリックすると成功することが多い）。

### Manage Storesの罠
- 「Select all stores」チェックボックスが既にONの場合とOFFの場合がある（都度確認）。
- YouTube Content IDは**必ず手動でOFFにする**（AI楽曲は対象外という運用ルール）。

### Localisation Hub（一番厄介）
- 「Add Localisation」ボタンをクリックしても、通常のクリックではモーダルが開かない
  ことが多い（CDP経由のクリックがページのJSハンドラーに正しく届かない模様）。
- **確実な方法**: JSコンソールで直接関数を呼ぶ。
  ```js
  recordlabel();  // モーダルを開く
  localisation_language('Japanese','26','56');  // 言語選択
  ```
- 「Select Language」ボタンも同様にクリックが効かないことが多い。以下のように
  **隠しinputを追加してform.submit()で本物のページ遷移を起こす**のが確実：
  ```js
  const form = document.getElementById('select_language').closest('form');
  let hidden = document.createElement('input');
  hidden.type = 'hidden';
  hidden.name = 'select_language';
  hidden.value = 'Select Language';
  form.appendChild(hidden);
  form.submit();
  ```
  （fetch()による疑似送信では、ボタンのname/valueが送信データに含まれず、
  サーバー側が反応しない）
- 遷移先の `/rn/add_localisation/<UPC>?language=Japanese&status=0` ページで
  Album Title/Artist Name/Composition Copyright/Sound Recording/Record Label の
  翻訳欄を埋め、同様に隠しinput(`album_save_translasion`)を追加して`form.submit()`。
- これで「Incomplete」状態のローカライズが1件追加される（Track単位の翻訳は
  Add Audioで曲を追加した後でないとできない）。

### 汎用テクニック
- ChromeのCDPクリック(`computer.left_click`)は稀に無反応になる。coordinateベースの
  クリックの前に`el.scrollIntoView({block:'center'})`→`getBoundingClientRect()`で
  座標を取り直すと成功率が上がる。ダメなら`screenshot`を1枚撮ってから再試行すると
  なぜか直ることが多い（キャリブレーションの問題らしい）。
- スクリーンショットが `CDP sendCommand "Page.captureScreenshot" timed out` で
  頻繁に失敗する。その場合は `read_page` / `get_page_text` / `javascript_exec` で
  代替すること。

---

## Suno入稿の重要な落とし穴（015〜021で判明・必読）

### 基本フロー
1. `https://suno.com/create` → 「アドバンスド」タブ
2. 「+Voice」→マイVoices→「Tonarine」カードの**テキスト部分（画像ではなく）をクリック**
   すると選択される（画像クリックはプレビュー再生になるだけで選択されない）
3. 歌詞欄・スタイル欄・Exclude Styles欄を入力
4. 「曲を作成」

### 歌詞欄（contenteditable div）の罠
- 長文を`type`アクションで一括投入すると**改行が全部消えて1行に連結される**ことがある
  （タイムアウトも頻発する: `CDP sendCommand "Input.insertText" timed out`）。
- **確実な方法**: 1行ずつ `computer.type` → `computer.key(Return)` を交互に実行する
  `browser_batch` を使う。セクション間の空行は`Return`を2回連続。歌詞全体で1回の
  browser_batchだと長すぎるので、Verse1まで/Chorus+Verse2/Bridge以降、のように
  2〜4回に分けて投げるとタイムアウトしにくい。
- 投入後は必ず `document.querySelector('[contenteditable=true]').innerText` で
  `[Chorus]`の出現回数（=3のはず）などを確認し、typoも目視チェックすること
  （ローマ字→かな変換のunicodeエスケープでtypoが混入しやすい。実際に
  「ぬぐ」を「ぬぎ」と打ち間違えた例あり）。
- typo修正は該当行を `find` → `triple_click`（1行選択）→ 正しいテキストを`type`で
  上書き、が確実。

### スタイル欄・Exclude Styles欄の罠
- これらは`textarea`/`input`要素だが、長文を`type`で打つとタイムアウトしたり
  **文字が入れ違いに壊れる**（例: "pop brightness, overly upbeat p" + "vinyl crackle..."
  が変な順序で混ざる）。
- **確実な方法**: JSのネイティブsetterで直接valueをセットし、inputイベントを発火。
  ```js
  const ta = [...document.querySelectorAll('textarea')].find(e=>e.placeholder.includes('中世'));
  const setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
  setter.call(ta, "（Style本文）");
  ta.dispatchEvent(new Event('input', {bubbles:true}));
  ```
  Exclude Styles欄（`input[placeholder="スタイルを除外"]`）も同様に
  `HTMLInputElement.prototype`のsetterで。
- 全曲共通のException Styles文言（vinyl crackle等）は使い回し可能なので、
  `releases/00N-*.md`の該当ブロックをそのままコピペしてよい。

### ページフリーズについて
- Sunoのcreateページはたまに10〜20秒程度フリーズし、`javascript_exec`や`type`が
  タイムアウトすることがある。`1+1`のような軽いJS評価で復旧確認しながら
  数回待てば大抵は復帰する（強制リロードは不要）。

---

## ディレクトリ構成メモ

- `releases/00N-*.md`: リリースごとの全情報（テーマ・Suno入力・ジャケットプロンプト・
  RouteNote情報）
- `covers/00N-*.jpg`（署名入り）/ `covers/00N-*_bg.jpg`（署名なし背景）
- `work/lyrics_0NN_<slug>_suno.txt`: Suno投入用の歌詞プレーンテキスト（Git管理外）
- `output/<曲名>.flac` / `output/<曲名> (Instrumental).flac`: マスタリング後の音源
  （後で一括アップロード予定）
- `scripts/`, `config.py` 等: 11ステップパイプラインの実装（① chart分析〜⑪配信）

## ユーザーの標準的な好み（再掲）

- 音楽理論的な判断（リファレンス曲選び、EQ、マスタリング数値）は毎回聞かずに
  Claudeが妥当な値を決めて報告するだけでよい
- Suno Styleに "vinyl crackle" / "tape hiss" 等のローファイ砂嵐系は**入れない**
  （Exclude Styles側に入れる）
- マスタリングラウドネス目標: -16 LUFS
- アーティスト名は固定で "Tonarine"
- YouTube Content IDは全曲でOFFにする（AI楽曲は対象外という運用ルール）
- テーマ・主張（論法）は**ユーザー自身が決める**。Claudeは実行・整理役に徹する

### 022〜033のマスタリング／ジャケット進捗（2026-09-27）
- マスタリング: 023〜033 の11曲は本編＋インスト版とも QC合格（-16 LUFS前後）で `output/` に出力済み
  （ファイル名は仮タイトル）。**022 はステム未DLのため未処理**。
  バッチ実行時は `run_audio.py` に `< /dev/null` を付けること（ffmpegがループの標準入力を読んで
  曲名が壊れ、loudnormの解析も失敗する）。
- ジャケット: Geminiで生成中。**参考画像（001系: 厚い筆致・グレイン・暗め・ランプ1つ）を添付**して
  「same exact art style」と指示するとブランドの雰囲気に近づく（添付なしだと明るく淡すぎる）。
  未DL。DL後は `covers/NNN-slug_bg.jpg` → `scripts/add_signature.py`。

### ジャケット生成方法の訂正（2026-09-27）
参考画像を1つのチャットで使い回すと生成のたびに画風が変わっていく。**曲ごとに新しいGeminiチャットを開き、
`covers/001-yofuke-no-tonari_bg.jpg`（署名なし）を添付して「画像を生成してください。添付画像をそのままベースに、
構図・人物・部屋・光・色・画風は一切変えず、小物だけを足した画像を作ってください」と指示する**（001に小物を足して
曲の雰囲気を出す方式）。英語で "Edit the attached image" と書くと説明文が返るだけなので、日本語で
「画像を生成してください」と明示する。022〜033を各1チャットで生成済み（Geminiのチャット履歴に残っている。DL未）。
Chrome操作の注意: 送信ボタンのクリックが1回目に効かないことがあり、URLやサイドバーの反映も30秒ほど遅れる。

### 022〜033 ジャケットDL完了・重大バグの修正（2026-09-27）
12曲すべて `covers/0NN-slug_bg.jpg`（1024×1024, 未署名）としてDL・md5で重複なしを確認済み。
途中で見つかった重大バグ：GeminiのHTML上では、添付した参考画像（001の小さいサムネイル）と
生成された本編画像が同じ `googleusercontent.com/gg/...` URLパターンを共有することがあり、
`naturalWidth` で「一番大きい画像」を選ぼうとすると、**生成画像がまだロード中でnaturalWidth=0を
返している間に、サムネイル側（naturalWidth=512等、表示は112px程度）を誤って選んでしまう**。
これにより023・030・033の3曲が同一の誤った画像（001そのまま、小物なし）で保存されていたことが
md5sumの重複から発覚。**正しい選び方は表示サイズで判定すること**：
`[...document.querySelectorAll('img')].find(i=>{const r=i.getBoundingClientRect(); return r.width>300;})`
（naturalWidthではなくgetBoundingClientRect().widthが300pxを超える＝実際に大きく表示されている
本編画像、という判定にする）。該当URLを新しいタブで直接開いてから（クロスオリジンのcanvas
tainted対策）このJSでcanvas変換・ダウンロードする。ダウンロードが `a.download` の指定名で
Downloadsフォルダに現れないことが数回あったが、リトライ（同じ手順を再実行）で成功した。
次に同じ作業をする際は、DL後に必ず `md5sum covers/*.jpg` で重複がないか確認し、疑わしい曲は
Readツールで目視確認すること（023は窓の曇り・マグ2つ・イス上のスカーフ、030は白湯、032は満月、
033はマグ2つ＋チェックのブランケット、を確認済み）。

### 022は欠番（2026-09-27）
「布団から出られない朝」(futon-kara-denerenai-asa) はステムZIPがDownloadsに存在せず、
マスタリング未実施のまま欠番とする方針にユーザーが決定。ジャケット画像（`022-*_bg.jpg`）は
存在するが、曲自体を出さないため以後の作業（署名合成・RouteNote提出）から022は除外する。
実質のリリース対象は023〜033の11曲。

### 3000×3000リサイズ＋署名合成完了（2026-09-27）
`scripts/add_signature.py` は `.venv/Scripts/python.exe` で実行する必要がある
（システムのpythonにはPillow未インストール）。023〜033の11曲分、`covers/0NN-slug_bg.jpg`
→ `covers/0NN-slug.jpg`（3000×3000、右下Tonarineロゴ）への変換完了。033で目視確認済み。
