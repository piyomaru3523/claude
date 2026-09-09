# ブランディング（全リリース共通・固定）

## アーティスト名: **Tonarine**

- 表記（配信メタデータ）: `Tonarine`（大文字始まり・ラテン文字）
- 読み: となりね
- 由来: 隣（tonari）＋ 音（ne）＝「となりの音」。作業するキミのそばで鳴っている音、という
  このカタログの役割そのもの。デビュー曲のサビ〈となりにいるよ〉と地続き。
- 造語のため名前衝突が起きにくい。

### 同名チェック（2026-09-08 実施）
| 媒体 | 結果 |
|---|---|
| Spotify 完全一致 | なし（Tonalie / トナリア / Tonarik は別物） |
| Apple Music | なし |
| Instagram `@tonarine` | 未登録（取得可能） |
| Web 検索 | アーティストとしての使用なし |

→ 全チャンネルで空き。確定。

## 固定するもの（仕様書④）
- **アーティスト名**: Tonarine（上記）— 全リリースで統一。RouteNote のプロフィール分裂を防ぐ。
- **ボーカル**: Suno の Personas 機能で初回の良いテイクをロック済み。以降のリリースで使い回す。
- **ジャケット**: 下記のビジュアルアイデンティティで統一。曲ごとに1枚、シーンだけ差し替え。

## ビジュアルアイデンティティ（ジャケット）— 全リリース固定

作風: **手描きイラスト**（アニメ寄り／Lofi Girl 系。温かいミュートな色、粒状のテクスチャ）。

### 固定ルール
- **ムード**: 夜更けの小さな灯りのある空間。静かで、少し切なく、温かい。
- **被写体**: 「気配」だけ。人物は**顔を見せない／中心に置かない**（後ろ姿・手元・シルエット・
  毛布の膨らみ等）。アーティスト名〈隣の音〉に対応。
- **光**: 暖色の実用光源（デスクランプ／間接照明／街灯）を**1つだけ**、オフセンターに。
  ハレーション・光のにじみを軽く。それ以外は暗い。
- **配色**: 影は濃紺〜藍〜ティール、灯りは琥珀色、ハイライトはやわらかい生成り。
  やや彩度を落としたフィルム調（微粒子グレイン、わずかな色被り）。
- **構図**: 三分割、光源はオフセンター、**余白を広く**、被写体は小さめ、暗部が多い。
- **フォーマット**: 3000×3000px 正方形・sRGB・JPG・25MB未満。生成は 3:2 か 16:9 で広めに
  出してから正方形にトリミング（構図に余裕を持たせる）。
- **サイン（固定・毎回入れる）**: `Tonarine` を **右下**に署名風で入れる。
  - 書体: **Sacramento**（Google Fonts / Canva にある欧風の手書きスクリプト、単一ウェイト）
  - サイズ: 文字の高さが画像の約4〜5%（3000pxなら **font size ≈ 120〜150px**、語幅はおよそ500〜650px）
  - 色・不透明度: 琥珀色（例 #F2C88C）または生成り（例 #EDE6D8）、不透明度 **75〜85%**
  - 余白: 右端・下端からそれぞれ画像の約4〜5%インセット（3000pxなら **約130px**）、位置は毎回同じ
  - **AIの画像プロンプトには文字を入れない**。生成後に本物のテキストレイヤーとして
    Canva（または Photopea / Figma 等）で重ねる。曲名は画像に入れない（ストア側に出る）。
- **反復モチーフ**（各カバーで1〜2個）: デスクランプ / 夜の窓 / 湯気の立つマグ / 椅子 /
  ヘッドフォン / ガラスの雨。

### 生成プロンプトのテンプレ（固定部＋[SCENE]差し替え）
```
soft hand-drawn illustration, anime-adjacent, warm muted palette, [SCENE],
a glowing warm desk lamp as the single light source off-center, deep indigo-navy
shadows with warm amber light, gentle linework, grainy textured shading, cozy and
quiet, person present only from behind (no visible face, not centered),
generous empty space, square, no text
```
- ネガティブ: `text, watermark, signature, harsh outlines, bright daylight, oversaturated, chibi, busy background, faces`
- 出力を正方形にし **3000×3000px** へ（Canva の Upscale / AI 拡大が望ましい。lanczos だと甘くなる）。
- 実際に使ったプロンプトは各 `releases/00N-*.md` に記録。カバー画像は `covers/` に置く。
- 001 は Canva の画像生成で作成（`releases/001` にシーン記載）。

## 曲タイトルの表記（全リリース）
- **配信メタデータのタイトルはローマ字（ヘボン式）** に統一する。RouteNote が非ASCII文字を
  「Unrecognised Characters」として警告し、海外の検索にも乗らないため。アーティスト名
  `Tonarine` がラテン文字なのとも揃う。
- 日本語表記は localized/alternative title 欄があればそこへ。SNS・ジャケット周辺では併記可。
- 例: `Yofuke no Tonari`（夜更けのとなり）／ インスト版は Title Version 欄に `Instrumental`。

## SNS
- Instagram: **`@_tonarine`**（`@tonarine` が取得不可のため）。表示名は `Tonarine` で統一。
  種別=クリエイター／カテゴリ=ミュージシャン。

## TODO
- [x] ジャケットのアートディレクション決定 → シネマティック写真（上記）
- [x] アーティスト名 → Tonarine
- [x] ボーカル Persona ロック（Suno）
- [x] Instagram `@_tonarine` を確保
- [ ] Instagram プロフィール文・キービジュアル設定
- [ ] RouteNote アカウント作成（Free プラン）※作業中
- [ ] 001 のジャケット生成（プロンプトは releases/001）
- [ ] 001 を RouteNote へ（本編＋インスト版）
