# Python Statistical Tests Samples

このリポジトリでは、SciPy を用いた t 検定とカイ二乗検定の代表的なユースケースを 3 本ずつ収録しています。いずれも単体実行でき、GitHub 上でそのまま参照できるように README で概要をまとめています。

## 使用ライブラリ
- [SciPy](https://scipy.org/) 1.10+ : `scipy.stats` の t 検定・カイ二乗検定関数を利用
- NumPy 1.24+ : サンプルデータ生成と配列演算

## 実行方法
```bash
python -m venv .venv
source .venv/bin/activate
pip install scipy numpy
python examples/<script>.py
```

---

## t 検定サンプル
| スクリプト | 内容 | 想定シナリオ |
| --- | --- | --- |
| `examples/t_test_one_sample.py` | `stats.ttest_1samp` を使い、サンプル平均と既知の母平均を比較します。 | 新ワークフローが平均 3.5 分以上の時短効果を持つか検証。 |
| `examples/t_test_independent.py` | Welch の 2 標本 t 検定 (`stats.ttest_ind ... equal_var=False`) で 2 つの独立群の平均差を評価。 | 旧 vs. 新オンボーディングフローの満足度比較。 |
| `examples/t_test_paired.py` | 対応のある t 検定 (`stats.ttest_rel`) で同一被験者の Before/After を比較。 | ドライバー訓練前後の反応時間短縮をチェック。 |

各スクリプトは t 統計量・p 値とシンプルな解釈メッセージを標準出力します。

## カイ二乗検定サンプル
| スクリプト | 内容 | 想定シナリオ |
| --- | --- | --- |
| `examples/chi_square_goodness_of_fit.py` | `stats.chisquare` により観測分布が一様分布に従うか検証。 | 曜日ごとの売上が均一かどうかの当てはまり検定。 |
| `examples/chi_square_independence.py` | `stats.chi2_contingency` で 2×2 分割表の独立性を判定。 | 性別とプロダクト色の好みの独立性検定。 |
| `examples/chi_square_homogeneity.py` | 複数群の割合が同じかを `stats.chi2_contingency` で比較。 | 広告クリエイティブ間のコンバージョン率の同質性検定。 |

出力にはカイ二乗統計量・自由度・p 値に加え、`chi2_contingency` を用いる例では期待度数も含めています。

---

## GitHub 公開メモ
- README で全スクリプトの概要と実行手順を把握できるように構成。
- サンプルデータはランダムではなく固定値なので常に同じ結果を再現します。変更や翻訳は各スクリプトを直接編集して行ってください。
