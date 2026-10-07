# PAPER.md — Thesis-ready extension: hidden patterns into chapters

This companion turns README §6 into five falsifiable PhD chapters. Each states
hypothesis, method, dataset, metric, and refutation condition. All seed numbers
come from executed experiments (see `results/`).

## Ch1. The MAC is the chip (critical-path concentration on mature nodes)
H: At f ≤ 25 MHz on GF180-class nodes, ≥80% of WNS risk concentrates in ≤2
combinational datapath macros (esp. wide MAC). M: static depth estimation +
STA sampling across 2026 grid-search designs (SPM, PicoRV32, 4×4 MAC) +
BTAP MAC model (exp02: 45–52 ns comb vs 15 ns 3-stage). Metric: WNS attribution
share. Refute: outlier share <50% across ≥10 designs.

## Ch2. Density realism gap (planning derate)
H: Achieved density is 10–44% of theoretical (Run-1: best 44%, peak 62%,
typical 3–14k/mm²); planning at 25% derate predicts fit within ±30%.
M: wafer.space density table + BTAP fit audit (exp04: 90–160k est vs 18–81k
realistic FF-equiv). Refute: >60% of new Run-2/3 designs exceed 50%.

## Ch3. Interface-test escape law
H: Single-clock-domain core coverage does not predict pad/interface escapes;
directed GL+pad-model tests cut escape rate ≥2× (BTAP: SPI dead/UART broken
despite core proof via counter-to-100, exp05). M: cocotb-vs-FPGA-vs-GL
coverage matrix + fault injection. Refute: interface escapes uncorrelated
with interface-test depth.

## Ch4. Grounding masquerades as timing
H: ≥1 in 5 hobbyist bring-up "timing" scares resolves to power-integrity
(grounds), diagnosed by over-clock counting (exp05 repro). M: bring-up log
coding + probe checklist RCT. Refute: <10% hygiene root-cause in survey.

## Ch5. Compiler-as-hardware (TTA correctness stack)
H: For TTA, assembler/compiler scheduling is part of the trusted computing
base; delay-slot and bypass bugs dominate post-silicon errata vs RTL bugs.
M: TCE/OpenASIP + BTAP IDE/compiler errata taxonomy. Refute: RTL bugs dominate.

## Publication path
Target: IEEE Micro / JSSC (case-study + benchmark track) or FPL/ASPDAC open-source
silicon track. Artefact: this repo (Docker, frozen live snapshot, CSV benchmarks).
Missing datum to close Ch1–Ch2: post-layout instance/WNS report from `final/`
(GDS already public) — one OpenROAD `report` run suffices.
