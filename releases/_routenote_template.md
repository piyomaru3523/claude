# RouteNote 入力テンプレート（全リリース共通・001で確定した運用）

各 `releases/00N-*.md` はこのテンプレの固定値を前提に、曲固有の値だけ書く。

## リリース（Single）
```
Release title: <ローマ字タイトル>          （例 Yofuke no Tonari）
Album Version: 空欄
Does this release contain cover versions?: No
Compilation Album: No
Primary artist: Tonarine  （Role: Primary。Add Artists で確定）
Primary genre: Electronic  （RouteNote に Lo-Fi なし）
Secondary genre: Pop      （任意）
基本言語(Language): English  ← JPローカライズを載せるため
Composition Copyright: 2026 / Tonarine
Sound Recording Copyright: 2026 / Tonarine
Record Label Name: Tonarine
Originally Released Date / Sales Start Date: <配信日 金曜・提出から最短14日>
Preorder Date: なし
Explicit Content: Not Explicit
Custom Album ID: 空欄
UPC / ISRC: 空欄（RouteNote 自動発行）
```

## Publishing Information
```
Writer(s) / Composer: <あなたの法的な氏名（ローマ字・毎回同じ表記）> → Add Composer
Does this release contain lyrics?: Yes （インスト単独リリースでない限り）
Lyricist(s): 同じ実名 → Add Lyricist
```

## Contributor Information
```
任意。スキップ可。入れるなら Role=Mastering Engineer / Name=Tonarine
```

## Track 1（本編）
```
Track Name: <ローマ字タイトル>
Title Version: 空欄
Track Number: 1
Artist: Tonarine (Primary)
Explicit: Not Explicit
Language: Japanese
Preview Clip: 00:00
Instrumental: No
ISRC: 自動
Audio file: output/<slug>.flac
```

## Track 2（インスト版）
```
Track Name: <ローマ字タイトル> (Instrumental)   ※半角括弧
Title Version: Instrumental
Track Number: 2
Artist: Tonarine (Primary)
Explicit: Not Explicit
Language: Instrumental か No Linguistic Content があればそれ、無ければ Japanese
Preview Clip: 00:00
Instrumental: Yes
ISRC: 自動
Audio file: output/<slug> (Instrumental).flac
```

## Localisations（日本語）
基本言語 English → Add Localisation → Japanese。
```
Album / Track1 / Track2 タイトル翻訳: <日本語タイトル>（Track2 の Version は Instrumental）
Artist Name Translation: Tonarine（翻訳しない）
Composition/Sound Recording Copyright / Label: Tonarine（そのまま）
```

## Manage Stores
```
Select All Stores: ON
YouTube Content ID: OFF（AI楽曲は対象外。絶対に選ばない）
Pricing: すべて Default
Territories: 何も入れない（＝全世界）。store filter にチップが残っていたら Clear
```

## Add Supporting Information（Track 2 で自動フラグが出たら）
```
Track 2 "<romaji> (Instrumental)" is an intentional instrumental version of Track 1 — the same recording with the lead and backing vocals removed. Both tracks are original works. The music was generated with Suno on a paid plan that grants full commercial and distribution rights (https://suno.com). Lyrics, take selection, editing and mastering are my own. Released under my own name/label (Tonarine). No third-party or copyrighted material is used.
```
+ 可能なら Suno 有料プラン契約画面のスクショを添付。

## Terms
```
「I agree to the RouteNote Terms & Conditions」に自分でチェック → Distribute Free
（Distribute Premium=有料 は押さない。後から個別に上げられる）
```

## 提出後
- Spotify for Artists にリリースが出たら（数日）、アクセス申請＋Track1をプレイリスト申請
  （配信7日前まで。間に合わなくてもリリースは出る＝必須ではない）
