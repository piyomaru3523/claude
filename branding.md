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

作風: **シネマティック写真**（実写 or フォトリアルなAI画像）。

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
- **文字**: 画像には基本入れない（曲名はストア側に出る）。入れる場合のみ `tonarine`
  小文字・細い sans・左下・毎回同じ位置。
- **反復モチーフ**（各カバーで1〜2個）: デスクランプ / 夜の窓 / 湯気の立つマグ / 椅子 /
  ヘッドフォン / ガラスの雨。

### 生成プロンプトのテンプレ（固定部＋[SCENE]差し替え）
```
cinematic night photograph, [SCENE], a single warm amber practical light off-center,
everything else in deep indigo-teal shadow, soft halation and gentle film grain,
shallow depth of field, muted filmic color grade, person present only as an
implied presence (no visible face, not centered), generous negative space,
rule-of-thirds composition, quiet and intimate mood, shot on 35mm, 3:2 frame
```
- 使う画像ツール（Midjourney / DALL-E / SDXL / Ideogram 等）に上記を貼り、`[SCENE]` だけ
  曲ごとに差し替える。出力を正方形3000pxにトリミング＋アップスケール。
- 実際に使ったプロンプトは各 `releases/00N-*.md` に記録する。カバー画像は `covers/` に置く。

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
