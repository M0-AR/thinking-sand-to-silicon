"""Regression tests: every experiment must run green and every video claim stays verified."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXP = ROOT / "experiments"
RES = ROOT / "results"


def run(script):
    r = subprocess.run([sys.executable, str(EXP / script)], capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, f"{script} failed:\n{r.stdout}\n{r.stderr}"


def test_01_tta():
    run("01_tta_semantics.py")
    d = json.loads((RES / "exp01_tta_semantics.json").read_text())
    assert d["tta_add"]["moves"] == 3
    assert d["tta_add"]["issue_cycles"] == 2
    assert d["program_capacity"]["total_moves"] == 2048


def test_02_timing():
    run("02_pipelining_timing.py")
    d = json.loads((RES / "exp02_timing.json").read_text())
    comb = next(r for r in d["rows"] if r["circuit"] == "mac32_comb_mult_plus_acc")
    pipe = next(r for r in d["rows"] if r["circuit"] == "mac32_pipelined_3stage")
    assert comb["closes_20MHz_slow"] is False  # reproduces creator's violation
    assert pipe["closes_20MHz_typ"] is True   # pipelining fixes it


def test_03_flow():
    run("03_openlane_flow_model.py")
    d = json.loads((RES / "exp03_flow.json").read_text())
    assert len(d["stages"]) == 13
    assert d["drc_share_pct"] > 30  # DRC dominates


def test_04_live():
    run("04_mpw_economics_live.py")
    d = json.loads((RES / "exp04_live.json").read_text())
    assert d["snapshot"]["gfs"]["current"] == 47.59
    assert d["snapshot"]["waferspace"]["dies_per_slot"] == 1000
    assert d["snapshot"]["waferspace"]["run1_designs"] == 29


def test_05_bringup():
    run("05_verification_bringup.py")
    d = json.loads((RES / "exp05_verification.json").read_text())
    assert d["nominal_bringup"]["ok"] is True
    assert d["ground_fault_repro"]["ok"] is False
