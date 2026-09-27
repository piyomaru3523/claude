# Release 013 — Shiroi Akari / 白い灯り

| 項目 | 値 |
|---|---|
| 配信タイトル | Shiroi Akari ／ 日本語ローカライズ: 白い灯り |
| slug | shiroi-akari |
| テーマ | 乾いたものも、少しずつなら潤っていく |
| 主張（論法） | 小さな積み重ねが大きな変化を生むという一般論を、加湿器が少しずつ空気を潤す様子に重ねる（演繹法） |
| 情景 | 乾燥する冬の夜、加湿器の白い光 |
| Style | 案A（ジャズ寄り） |
| ステータス | RouteNote: Album Details/Artwork/Manage Stores/日本語ローカライズ(アルバムレベル)完了。UPC 5064140424398。配信日2026-10-05。Track(Add Audio)は音楽アップロードを後でまとめて行うため未着手 — その際にTrack1/2のローカライズも要追加 |

## Suno 入力

### Style欄
```
A muted electric-piano figure glows softly like a humidifier's quiet light in the dark, jazzy sevenths leaning and resolving, very soft. Mellow lo-fi meets late-night jazz - the hush of a study playlist carrying the warmth of a small combo, chords full of sevenths and ninths, never bright, always a little wistful. A young Japanese female voice, breathy and close, half-sings the melody, close and private, recorded with pristine clarity. Brushed drums swing softly under an unhurried 104 BPM; an upright-style bass walks in slow steps; a muted electric-piano line answers the voice in the gaps. Production stays low, warm and pristine: felt-damped keys, a soft room reverb, crystal-clear, nothing sharp or forward. The arrangement breathes in slow tides - hushed verses, a chorus that lifts only a little, a bridge that thins to voice and one held chord, then eases back. Everything sits back in the mix, calm and repeatable, a loop to work beside.
```

### Exclude Styles欄
```
vinyl crackle, tape hiss, static, hum, background noise, muddy low end, hazy production, low fidelity, pop brightness, overly upbeat progressions, EDM festival bombast, big-room drops, aggressive techno, trap percussion cliches, loud belted vocals, excessive autotune, harsh compression, brittle sibilant highs, plastic synth textures, sterile digital reverb, predictable four-chord loops
```

### 歌詞欄
`work/lyrics_013_shiroiakari_suno.txt`（かな・③検証済み）
（work/ は Git 管理外なので下にも収録）:
```
[Intro]

[Verse1]
かわいたくうきのへやに
かしつきのあかりがつく
しろいひかりがゆっくり
へやのすみまでとどく
すこしずつたつゆげが
くうきをうるおしていく
なにもかわらないようで
たしかにかわっていく

[PreChorus]
かんそうするふゆのよるは
はだもこころもかわく
でもすこしずつでいい
それでじゅうぶんたりる

[Chorus]
すこしずつでいいんだよ
かわいたものもうるおう
しろいあかりがともるたび
こころがすこしかるくなる
キミといるじかんもきっと
すこしずつうるおってく

[Verse2]
かしつきのおとがする
しずかなみずのおと
キミがくしゃみをひとつ
もうふをもういちまい
ちいさなことをかさねてく
すこしずつかえていく
しろいあかりのそばでなら
それがよくわかるよ

[Chorus]
すこしずつでいいんだよ
かわいたものもうるおう
しろいあかりがともるたび
こころがすこしかるくなる
キミといるじかんもきっと
すこしずつうるおってく

[Bridge]
たんくのみずがなくなる
またあしたいれよう
こんやはこのままで
あかりをみていよう

[Chorus]
しろいあかりがきえても
キミのぬくもりはのこる
すこしずつでよかったんだ
ゆっくりうるおえばいい
あさがくるまでとなりで
ねむっていてね

[Outro]
かしつきがとまる
キミがもうねむってる
おやすみ
```


## ⑤〜⑩
`python scripts/run_audio.py --input input/shiroi-akari_stems --name "白い灯り" --instrumental`

## ⑪-a ジャケット
シーン: 乾燥した冬の部屋、後ろ姿の人物が加湿器のほのかな白い光を眺めている。湯気がゆっくり立ちのぼる。
```
Soft painterly illustration, hand-painted book cover style, thick soft brushstrokes with visible canvas grain texture, muted desaturated cool-white and warm brown color palette. Extremely dark, moody, low-key lighting. A young woman with dark hair in a loose messy bun, seen from a three-quarter angle from behind, sitting close to a small humidifier glowing softly white, gentle steam rising, in an otherwise dark winter room. Soft dark silhouette, face deep in shadow, no visible features, solid opaque clothing with no transparency. Square format, figure off-center, generous dark negative space. No text.
```
右下に `Tonarine` サイン。`covers/013-shiroi-akari.jpg`。

## ⑪-b RouteNote
`_routenote_template.md` どおり。Title `Shiroi Akari` / `Shiroi Akari (Instrumental)` / 日本語 `白い灯り`。
Audio: `output/白い灯り.flac` / `output/白い灯り (Instrumental).flac`。
